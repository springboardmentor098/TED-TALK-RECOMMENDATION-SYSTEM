"""Streamlit interface for the TED Talks recommendation project."""
from pathlib import Path
import streamlit as st
from src.recommender import TEDRecommender

ROOT = Path(__file__).resolve().parent
TALKS = ROOT / "dataset" / "ted_talks_cleaned.csv"
INTERACTIONS = ROOT / "dataset" / "user_interactions.csv"

st.set_page_config(page_title="TED Talks Recommender", page_icon="🎤", layout="wide")
st.title("🎤 TED Talks Recommendation System")
st.write("Find talks related to your interests or discover talks liked by similar users.")

@st.cache_resource
def load_model():
    if not TALKS.exists() or not INTERACTIONS.exists():
        raise FileNotFoundError("Place ted_talks_cleaned.csv and user_interactions.csv in dataset/.")
    return TEDRecommender.from_csv(TALKS, INTERACTIONS)

try:
    model = load_model()
except Exception as exc:
    st.error(f"Could not load recommendation data: {exc}")
    st.stop()

mode = st.radio("Recommendation method", ["Hybrid", "Content based", "Collaborative"], horizontal=True)
if mode != "Content based":
    users = sorted(model.user_item.index.astype(str))
    user_id = st.selectbox("Choose a sample user", users)
else:
    user_id = None

talk_choices = model.talks[["talk_id", "title"]].copy()
talk_choices["label"] = talk_choices.title + " (ID " + talk_choices.talk_id + ")"
query = st.text_input("Search TED Talks", placeholder="e.g. climate, creativity, education")
filtered = talk_choices[talk_choices.title.str.contains(query, case=False, na=False)] if query else talk_choices
selected_labels = st.multiselect("Select talks you like (optional)", filtered.label.tolist(),
                                 help="Used as content seeds; already selected talks are excluded from results.")
seed_ids = talk_choices.loc[talk_choices.label.isin(selected_labels), "talk_id"].tolist()
top_n = st.slider("Number of recommendations", 5, 20, 10)
weight = st.slider("Content weight", 0.0, 1.0, 0.5, 0.05, disabled=mode != "Hybrid")

if st.button("Get recommendations", type="primary"):
    if mode == "Content based":
        results = model.content_recommendations(seed_talk_ids=seed_ids, top_n=top_n)
    elif mode == "Collaborative":
        results = model.collaborative_recommendations(user_id, top_n=top_n)
    else:
        results = model.hybrid_recommendations(user_id, top_n=top_n,
                                                content_weight=weight, seed_talk_ids=seed_ids)
    if results.empty:
        st.info("No recommendations are available. Select one or more talks or choose a user with interaction history.")
    else:
        st.subheader(f"{len(results)} recommendations")
        for rank, row in enumerate(results.itertuples(index=False), start=1):
            st.markdown(f"**{rank}. [{row.title}]({getattr(row, 'url', '')})**  ")
            meta = []
            if hasattr(row, "speaker") and row.speaker: meta.append(str(row.speaker))
            if hasattr(row, "views") and row.views: meta.append(f"{row.views:,} views")
            st.caption(" · ".join(meta) if meta else f"Talk ID {row.talk_id}")
            if hasattr(row, "description") and row.description:
                st.write(str(row.description)[:350] + ("…" if len(str(row.description)) > 350 else ""))
            st.caption(f"Model score: {row.score:.3f}")
