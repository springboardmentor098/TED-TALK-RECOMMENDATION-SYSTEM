"""Content, user-based collaborative, and hybrid TED talk recommendations."""
from __future__ import annotations

from pathlib import Path
import numpy as np
import pandas as pd
from scipy.sparse import csr_matrix
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


def _id(value) -> str:
    if pd.isna(value):
        return ""
    value = str(value).strip()
    return value[:-2] if value.endswith(".0") else value


class TEDRecommender:
    def __init__(self, talks: pd.DataFrame, interactions: pd.DataFrame):
        required_talks = {"talk_id", "title", "combined_text"}
        required_interactions = {"user_id", "talk_id", "rating"}
        if not required_talks.issubset(talks.columns):
            raise ValueError(f"Talks need columns: {sorted(required_talks)}")
        if not required_interactions.issubset(interactions.columns):
            raise ValueError(f"Interactions need columns: {sorted(required_interactions)}")
        self.talks = talks.copy()
        self.talks["talk_id"] = self.talks.talk_id.map(_id)
        self.talks["title"] = self.talks.title.fillna("").astype(str)
        self.talks["combined_text"] = self.talks.combined_text.fillna("").astype(str)
        self.talks = self.talks.drop_duplicates("talk_id").reset_index(drop=True)
        self.interactions = interactions.copy()
        self.interactions["user_id"] = self.interactions.user_id.map(_id)
        self.interactions["talk_id"] = self.interactions.talk_id.map(_id)
        self.interactions["rating"] = pd.to_numeric(self.interactions.rating, errors="coerce")
        self.interactions = self.interactions.dropna(subset=["rating"])
        self.interactions = self.interactions[self.interactions.talk_id.isin(self.talks.talk_id)]
        self.interactions = self.interactions.drop_duplicates(["user_id", "talk_id"], keep="last")
        self.talk_index = self.talks.set_index("talk_id", drop=False)
        self.tfidf = TfidfVectorizer(stop_words="english", max_features=10000,
                                     ngram_range=(1, 2), min_df=2, max_df=0.95,
                                     sublinear_tf=True)
        self.content_matrix = self.tfidf.fit_transform(self.talks.combined_text)
        self.user_item = self.interactions.pivot(index="user_id", columns="talk_id", values="rating")
        self.user_item = self.user_item.reindex(columns=self.talks.talk_id, fill_value=np.nan)
        self.user_similarity = cosine_similarity(self.user_item.fillna(0))
        np.fill_diagonal(self.user_similarity, 0)
        self.user_positions = {u: i for i, u in enumerate(self.user_item.index)}
        self.talk_positions = {t: i for i, t in enumerate(self.talks.talk_id)}

    @classmethod
    def from_csv(cls, talks_path, interactions_path):
        return cls(pd.read_csv(talks_path), pd.read_csv(interactions_path, dtype={"user_id": str}))

    def _format(self, scores, excluded=(), top_n=10):
        excluded = set(map(_id, excluded))
        rows = [(talk_id, float(score)) for talk_id, score in scores.items()
                if talk_id in self.talk_index.index and talk_id not in excluded and np.isfinite(score)]
        rows.sort(key=lambda x: (-x[1], x[0]))
        result = self.talks.set_index("talk_id").loc[[x[0] for x in rows[:top_n]]].reset_index()
        result["score"] = [x[1] for x in rows[:top_n]]
        return result

    def content_recommendations(self, user_id=None, seed_talk_ids=None, top_n=10):
        seeds = list(map(_id, seed_talk_ids or []))
        if user_id is not None:
            user_rows = self.interactions[self.interactions.user_id == _id(user_id)]
            seeds += user_rows.loc[user_rows.rating >= 4, "talk_id"].tolist()
        seeds = list(dict.fromkeys(t for t in seeds if t in self.talk_positions))
        if not seeds:
            return pd.DataFrame(columns=[*self.talks.columns, "score"])
        weights = []
        for talk_id in seeds:
            mean_rating = self.interactions.loc[self.interactions.talk_id == talk_id, "rating"].mean()
            weights.append(max(0.1, float(mean_rating)) if pd.notna(mean_rating) else 3.0)
        weights = np.asarray(weights)
        vectors = self.content_matrix[[self.talk_positions[t] for t in seeds]]
        profile = csr_matrix(vectors.multiply(weights[:, None]).sum(axis=0))
        # TF-IDF rows are L2-normalized; normalize the weighted profile and use
        # sparse dot products instead of materializing all pairwise distances.
        norm = np.sqrt(profile.multiply(profile).sum())
        if norm:
            profile = profile / norm
        scores = (profile @ self.content_matrix.T).toarray().ravel()
        return self._format(dict(zip(self.talks.talk_id, scores)), excluded=seeds, top_n=top_n)

    def collaborative_recommendations(self, user_id, top_n=10, min_similarity=0.0):
        user_id = _id(user_id)
        if user_id not in self.user_positions:
            return pd.DataFrame(columns=[*self.talks.columns, "score"])
        pos = self.user_positions[user_id]
        weights = self.user_similarity[pos]
        ratings = self.user_item.fillna(0).to_numpy(dtype=float)
        observed = self.user_item.notna().to_numpy(dtype=float)
        weights = np.where(weights >= min_similarity, weights, 0.0)
        numerators = weights @ ratings
        denominators = weights @ observed
        predicted = np.divide(numerators, denominators, out=np.zeros_like(numerators), where=denominators > 0)
        known = self.user_item.loc[user_id].dropna().index
        scores = {talk_id: float(predicted[i]) for i, talk_id in enumerate(self.talks.talk_id)
                  if talk_id not in known and denominators[i] > 0}
        return self._format(scores, excluded=known, top_n=top_n)

    def hybrid_recommendations(self, user_id, top_n=10, content_weight=0.5, candidate_n=100,
                               seed_talk_ids=None):
        if not 0 <= content_weight <= 1:
            raise ValueError("content_weight must be between 0 and 1")
        user_id = _id(user_id)
        content = self.content_recommendations(user_id, seed_talk_ids, candidate_n)
        collab = self.collaborative_recommendations(user_id, candidate_n)
        # Min-max normalize each model before mixing unlike score scales.
        def normalized(frame):
            if frame.empty:
                return {}
            vals = frame.score.astype(float)
            span = vals.max() - vals.min()
            return dict(zip(frame.talk_id, (vals - vals.min()) / span if span else np.ones(len(vals))))
        c_scores, cf_scores = normalized(content), normalized(collab)
        known = self.interactions.loc[self.interactions.user_id == user_id, "talk_id"]
        ids = set(c_scores) | set(cf_scores)
        combined = {t: content_weight * c_scores.get(t, 0) + (1-content_weight) * cf_scores.get(t, 0) for t in ids}
        return self._format(combined, excluded=known, top_n=top_n)


def precision_recall_at_k(recommended, relevant, k=10):
    relevant = set(relevant)
    top = list(recommended)[:k]
    hits = sum(t in relevant for t in top)
    return hits / k, hits / len(relevant) if relevant else 0.0
