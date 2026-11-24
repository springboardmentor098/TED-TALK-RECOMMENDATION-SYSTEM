# 🎯 TED Talks Recommender

[![Python](https://img.shields.io/badge/Python-3.11+-blue?logo=python&logoColor=white)](https://python.org)
[![Jupyter](https://img.shields.io/badge/Jupyter-Notebook-orange?logo=jupyter&logoColor=white)](https://jupyter.org)
[![scikit-learn](https://img.shields.io/badge/scikit--learn-1.5+-F7931E?logo=scikit-learn&logoColor=white)](https://scikit-learn.org)
[![Pandas](https://img.shields.io/badge/Pandas-2.2+-150458?logo=pandas&logoColor=white)](https://pandas.pydata.org)
[![NumPy](https://img.shields.io/badge/NumPy-1.26+-013243?logo=numpy&logoColor=white)](https://numpy.org)
[![Status](https://img.shields.io/badge/Status-In%20Progress-yellow)]()
[![PRs Welcome](https://img.shields.io/badge/PRs-Welcome-brightgreen.svg)]()

> **A content-based recommendation engine for TED Talks** powered by TF-IDF and cosine similarity. Enter a talk title, get the most textually similar talks — with the feature combination chosen by an actual four-way experiment, not guesswork.

---

## 🌟 Overview

| Metric | Value |
|--------|-------|
| **Talks Processed** | 4,005 |
| **Final Feature Set** | Title + Description + Tags (Exp3) |
| **Final Vocabulary** | 23,643 terms |
| **Features** | Unigrams + Bigrams |
| **Similarity Metric** | Cosine Similarity |
| **Similarity Matrix** | 4005 × 4005 (dense) |
| **Recommendation API** | `recommend_talks(title, top_n=5)` |
| **Language** | English |
| **Pipeline Progress** | Tasks 1–6 complete · Task 7 next |

### 🎬 Demo Preview

Real output from notebook `06` using the selected **Exp3** pipeline:

```text
🔍 Seed: "Averting the climate crisis" (Al Gore)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
1. New thinking on the climate crisis                    0.3238
2. The case for optimism on climate change                0.2877
3. What comes after an inconvenient truth                 0.2730
4. Why I must speak out about climate change              0.2642
5. A critical look at geoengineering against climate…     0.2588
```

> Scores are lower than the transcript baseline by design. Cosine scores are only comparable **within** one feature set — judge by ranking and relevance, not by absolute value.

---

## 🏗️ Architecture

```mermaid
graph LR
    A[📥 Raw Data<br/>ted_talks_en.csv] --> B[🔍 Exploration<br/>01_data_exploration]
    B --> C[📊 EDA & Quality<br/>02_eda_data_quality]
    C --> D[🧹 Cleaning & Preprocessing<br/>03_data_cleaning_preprocessing]
    D --> E[🔤 TF-IDF Baseline<br/>04_tfidf_vectorization]
    E --> F[🎯 Recommendation Engine<br/>05_content_based_recommendation]
    F --> G[🧪 Feature Selection<br/>06_feature_selection_evaluation]
    G --> H[👥 User Interaction Data<br/>07 — planned]
    H -.-> I[🤝 Collaborative Filtering<br/>08 — planned]
    I -.-> J[🚀 Hybrid Model + Streamlit]

    style A fill:#ffebee,stroke:#c62828
    style B fill:#fff3e0,stroke:#ef6c00
    style C fill:#e8f5e9,stroke:#2e7d32
    style D fill:#e3f2fd,stroke:#1565c0
    style E fill:#f3e5f5,stroke:#7b1fa2
    style F fill:#fce4ec,stroke:#c2185b
    style G fill:#e0f2f1,stroke:#00695c
    style H fill:#f1f8e9,stroke:#558b2f
    style I fill:#f1f8e9,stroke:#558b2f
    style J fill:#eceff1,stroke:#455a64
```

---

## 📦 Tech Stack

### Core Libraries

| Category | Libraries |
|----------|-----------|
| **Data Processing** | `pandas`, `numpy` |
| **Visualization** | `matplotlib`, `seaborn` |
| **ML/NLP** | `scikit-learn` (TF-IDF, cosine similarity) |
| **Serialization** | `joblib`, `scipy.sparse` (installed with scikit-learn) |
| **Environment** | `jupyter`, Python 3.11+ |

### Pipeline Artifacts

```text
data/
├── raw/
│   ├── ted_talks_en.csv              # 46 MB  - Original Kaggle dataset (4005 × 19)
│   └── ted_talks_selected.csv        # 43 MB  - 12 core columns
└── processed/
    ├── ted_talks_cleaned.csv         # 123 MB - Final cleaned dataset (4005 × 16)
    ├── ted_talks_cleaned_all.csv     # 165 MB - Audit file with originals + cleaned text
    │
    ├── tfidf_matrix_exp3.npz         # 1.6 MB - FINAL sparse matrix (4005 × 23,643)
    ├── cosine_sim_exp3.npy           # 128 MB - FINAL dense similarity (4005 × 4005)
    ├── tfidf_vectorizer_exp3.joblib  # 0.6 MB - FINAL fitted vectorizer
    │
    ├── tfidf_matrix.npz              # 22 MB  - Baseline sparse matrix (4005 × 366,288)
    ├── cosine_sim.npy                # 128 MB - Baseline dense similarity
    ├── tfidf_vectorizer.joblib       # 10 MB  - Baseline fitted vectorizer
    └── processed_data.md             # Regeneration notes (committed)
```

> `data/processed/` is gitignored because the files are large. `processed_data.md` documents how to rebuild every artifact.

---

## 🔬 Data Pipeline

### 1️⃣ Exploration (`01_data_exploration.ipynb`)

- **Source**: [TED Ultimate Dataset](https://www.kaggle.com/datasets/miguelcorraljr/ted-ultimate-dataset/data) → `ted_talks_en.csv`
- **Shape**: 4,005 rows × 19 columns → **selected 12 core columns**
- Renames `speaker_1` → `speaker`, `topics` → `tags`, `occupations` → `speaker_occupation`
- Parses dict/list strings into plain comma-separated values
- **Findings**: 0 duplicate rows, 0 duplicate `talk_id`/`url`, transcripts for all 4,005 talks; `speaker_occupation` has 522 missing values (13.03%), handled in notebook 03
- **Output**: `data/raw/ted_talks_selected.csv`

### 2️⃣ EDA & Quality (`02_eda_data_quality.ipynb`)

| Check | Result |
|-------|--------|
| Missing `speaker_occupation` | 522 (13.03%) |
| Short transcripts (< 50 words) | 10 talks (music/performance) |
| Unique tags | 457 |
| Total tag mentions | 31,700 |
| Description length | ~58 words (9–143) |
| Transcript length | ~1,797 words (2–11,121), right-skewed |
| Duration | ~724 s avg (~12 min), 60–3,922 s |
| Views | Mean 2.15 M, median 1.38 M, max 65 M — heavily skewed |
| Top tags | `science` (993), `technology` (979), `culture` (680), `tedx` (581), `global issues` (574) |

### 3️⃣ Cleaning & Preprocessing (`03_data_cleaning_preprocessing.ipynb`)

```python
# Applied to title, description, transcript, tags
def clean_text(text):
    text = text.lower()                              # 1. Lowercase
    text = remove_urls_and_html(text)                # 2. Remove URLs/HTML
    text = remove_ted_noise(text)                    # 3. Remove (laughter), (applause), etc.
    text = replace_punctuation_with_space(text)      # 4. Punctuation → space
    text = collapse_whitespace(text)                 # 5. Normalize whitespace
    return text
```

**Decisions**:
- Fill missing `speaker_occupation` → `"unknown"` (keeps all 4,005 talks)
- Keep short transcripts and flag them with `is_short_transcript`
- Deduplicate tags, lowercase, re-join with `, `
- **Two combined text variants**:
  - `combined_text` — plain concatenation (baseline)
  - `combined_text_prefixed` — `title: … tags: … description: … transcript: …` ← used in Task 4
- **Outputs**: `ted_talks_cleaned_all.csv` (20 cols, audit) and `ted_talks_cleaned.csv` (16 cols, deliverable)

### 4️⃣ TF-IDF Baseline (`04_tfidf_vectorization.ipynb`)

```python
vectorizer = TfidfVectorizer(
    stop_words="english",      # Remove common English stopwords
    ngram_range=(1, 2),        # Unigrams + bigrams
    min_df=2,                  # Ignore terms in < 2 documents
    max_df=0.9                 # Ignore terms in > 90% documents
)

tfidf_matrix = vectorizer.fit_transform(df["combined_text_prefixed"])
cos_sim = cosine_similarity(tfidf_matrix, dense_output=True)
np.fill_diagonal(cos_sim, 0)   # Remove self-similarity
```

**Results**:
- **Vocabulary**: 366,288 terms · **Matrix**: 4005 × 366,288 · **Non-zeros**: 3,123,292
- **Sparsity**: ~99.8% (efficient storage with `scipy.sparse`)
- **Known limitations observed**:
  - Frequent names beat topics — top term for the climate talk was `tipper`, not `climate`
  - Numeric tokens (`000`, `000 morning`, …) polluted the vocabulary
  - Education/creativity seed drifted off-topic by rank 3
  - Absolute cosine scores are low (0.13–0.17) because transcripts are long; ranking still holds

### 5️⃣ Recommendation Engine (`05_content_based_recommendation.ipynb`)

`recommend_talks(title, top_n=5)` is reusable: TF-IDF and cosine matrices are loaded once (or rebuilt once if missing), so each call is a cheap array lookup.

**Matching strategy**:
1. **Exact** match (case-insensitive, whitespace-stripped)
2. **Partial/substring** match — if multiple candidates, `difflib` auto-picks the closest
3. **Invalid** title — suggests the closest valid title and returns `None`
4. **Validation** — `top_n` must be an integer in `[1, 20]`
5. **Self-exclusion** — diagonal is zeroed *and* the seed index is filtered out

Tested with exact, different-case, partial, ambiguous, typo, invalid `top_n`, and custom `top_n` cases.

### 6️⃣ Feature Selection (`06_feature_selection_evaluation.ipynb`)

Four TF-IDF + cosine pipelines were built and compared on 5 seed talks:

| Experiment | Columns | Vocabulary | Mean Tag Jaccard |
|------------|---------|-----------:|-----------------:|
| Exp1 | Title only | 2,515 | 0.1021 |
| Exp2 | Title + Tags | 7,508 | **0.2962** |
| Exp3 ✅ | Title + Description + Tags | 23,643 | 0.2717 |
| Exp4 | Title + Description + Transcript + Tags | 363,947 | 0.1808 |

**Metric**: average Jaccard overlap between the seed talk's tags and the recommended talks' tags — an objective topical-relevance signal.

**Selected: Exp3 — Title + Description + Tags**

Why not the metric winner (Exp2)?
- **Tag Jaccard is biased toward Exp2** — tags are literally part of its input, so it measures label overlap, not meaning.
- **Qualitative review favors Exp3** — for the policing seed, Exp2 returned unrelated talks, while Exp3 returned rule-of-law and justice-system talks.
- **Exp4 adds noise** — long transcripts let names/filler words outrank the topic; tag overlap fell to 0.1808, far below Exp2/Exp3.
- **Exp1 is too narrow** — near-duplicate talks from the same series.
- **Deployment-friendly** — Exp3 is ~15× smaller than Exp4 and builds in under a second.

---

## 📈 Key Findings

### ✅ What Works Well

| Seed Talk | Best Result | Notes |
|-----------|-------------|-------|
| Averting the climate crisis | 5/5 climate talks | Exp3 keeps a tight, meaningful cluster |
| Do schools kill creativity | Education/creativity cluster | Exp3 returns Robinson's follow-ups first; Exp2 stays in the education cluster |
| Simplicity sells | Design/tech cluster | Baseline design/tech cluster holds; Exp3 keeps conceptually related talks |
| How policing for profit… | Justice/policy cluster (Exp3) | Exp3 beats Exp2 on human-judged relevance |

### ⚠️ Known Issues

| Issue | Impact | Status |
|-------|--------|--------|
| Tag Jaccard favors Exp2 by construction | Metric alone would pick the wrong feature set | Documented; Exp3 chosen on qualitative + metric balance |
| Proper nouns overweighted | Names can outrank topics in full-text models | Mitigated by dropping transcripts (Exp3); not fully solved |
| Numeric tokens in vocabulary | Noisy features, larger matrices | Open — a `token_pattern` fix is a candidate improvement |
| Transcript noise | Off-topic drift when transcripts are included | Resolved by excluding transcripts in Exp3 |
| Cosine scores not comparable across experiments | Misleading absolute thresholds | Documented; compare rankings within a pipeline |
| Popularity/quality ignored | "Most similar" ≠ "best talk" | Planned — popularity re-ranking with log-transformed views |
| No personalization | Every user gets the same recommendations | Task 7/8 (collaborative filtering) |

---

## 🚀 Quick Start

### Prerequisites

```bash
Python 3.11+
```

### Installation

```bash
# Clone the repository
git clone https://github.com/springboardmentor098/TED-TALK-RECOMMENDATION-SYSTEM.git
cd TED-TALK-RECOMMENDATION-SYSTEM

# Create virtual environment
python -m venv .venv
source .venv/bin/activate        # Windows: .venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
```

### Run Notebooks (in order)

```bash
jupyter lab notebooks/
# Execute sequentially:
# 01_data_exploration.ipynb
# 02_eda_data_quality.ipynb
# 03_data_cleaning_preprocessing.ipynb
# 04_tfidf_vectorization.ipynb
# 05_content_based_recommendation.ipynb
# 06_feature_selection_evaluation.ipynb
```

Or run them headless:

```bash
jupyter nbconvert --execute notebooks/01_data_exploration.ipynb --to notebook --inplace
jupyter nbconvert --execute notebooks/02_eda_data_quality.ipynb --to notebook --inplace
jupyter nbconvert --execute notebooks/03_data_cleaning_preprocessing.ipynb --to notebook --inplace
jupyter nbconvert --execute notebooks/04_tfidf_vectorization.ipynb --to notebook --inplace
jupyter nbconvert --execute notebooks/05_content_based_recommendation.ipynb --to notebook --inplace
jupyter nbconvert --execute notebooks/06_feature_selection_evaluation.ipynb --to notebook --inplace
```

> Notebooks 01 and 02 need `data/raw/ted_talks_en.csv`. Notebook 03 can start from the checked-in `data/raw/ted_talks_selected.csv`; notebooks 04–06 depend on the `data/processed/ted_talks_cleaned.csv` it produces. If you only have the raw Kaggle file, run notebook 01 first.

### Use the Final (Exp3) Recommender

```python
import difflib
import numpy as np
import pandas as pd

df = pd.read_csv("data/processed/ted_talks_cleaned.csv")
cos_sim = np.load("data/processed/cosine_sim_exp3.npy")   # final feature set

def recommend_talks(title, top_n=5):
    """Top-N most similar talks for a title (case-insensitive, fuzzy fallback)."""
    if not isinstance(top_n, int) or not 1 <= top_n <= 20:
        raise ValueError("top_n must be an integer between 1 and 20")

    titles = df["title"].str.lower()
    matches = df.index[titles == title.strip().lower()].tolist()

    if not matches:  # partial match
        partial = df.index[titles.str.contains(title.strip().lower(), regex=False, na=False)].tolist()
        if len(partial) == 1:
            matches = partial
        elif partial:
            best = difflib.get_close_matches(title, df.loc[partial, "title"], n=1, cutoff=0.0)[0]
            matches = df.index[df["title"] == best].tolist()

    if not matches:  # invalid title
        suggestion = difflib.get_close_matches(title, df["title"], n=1, cutoff=0.5)
        print(f"Title not found. Did you mean: {suggestion[0] if suggestion else '—'}?")
        return None

    seed = matches[0]
    scores = cos_sim[seed]
    top_idx = [i for i in scores.argsort()[::-1] if i != seed][:top_n]

    return pd.DataFrame({
        "Rank": range(1, len(top_idx) + 1),
        "Talk ID": df.loc[top_idx, "talk_id"].to_numpy(),
        "Recommended Title": df.loc[top_idx, "title"].to_numpy(),
        "Similarity Score": np.round(scores[top_idx], 4),
    })

print(recommend_talks("Averting the climate crisis", top_n=5))
```

The baseline artifacts (`tfidf_matrix.npz`, `cosine_sim.npy`, `tfidf_vectorizer.joblib`) are kept for reproducing the Task 4 experiment; the `*_exp3` files are the ones to use going forward.

---

## 📁 Project Structure

```text
ted-talks-recommender/
├── 📓 notebooks/
│   ├── 01_data_exploration.ipynb
│   ├── 02_eda_data_quality.ipynb
│   ├── 03_data_cleaning_preprocessing.ipynb
│   ├── 04_tfidf_vectorization.ipynb
│   ├── 05_content_based_recommendation.ipynb
│   └── 06_feature_selection_evaluation.ipynb
├── 📊 data/
│   ├── raw/
│   │   ├── ted_talks_en.csv
│   │   └── ted_talks_selected.csv
│   └── processed/                  # gitignored, see processed_data.md
│       ├── ted_talks_cleaned.csv
│       ├── ted_talks_cleaned_all.csv
│       ├── tfidf_matrix_exp3.npz
│       ├── cosine_sim_exp3.npy
│       ├── tfidf_vectorizer_exp3.joblib
│       ├── tfidf_matrix.npz
│       ├── cosine_sim.npy
│       ├── tfidf_vectorizer.joblib
│       └── processed_data.md
├── ⚙️ .venv/                       # not committed
├── 📋 requirements.txt
├── 🚫 .gitignore
├── 📝 TED talk tasks.docx          # local task brief, gitignored
└── 📖 README.md
```

---

## 🗺️ Roadmap

### ✅ Completed

| Task | Deliverable | Key Result |
|------|-------------|------------|
| 1 | `01_data_exploration.ipynb` | 4,005 talks, 12 selected columns, no missing/duplicate IDs |
| 2 | `02_eda_data_quality.ipynb` | Quality report, tag/text/duration/view analysis |
| 3 | `03_data_cleaning_preprocessing.ipynb` | Cleaned dataset + combined text fields |
| 4 | `04_tfidf_vectorization.ipynb` | 366,288-term baseline + cosine similarity |
| 5 | `05_content_based_recommendation.ipynb` | Reusable `recommend_talks(title, top_n=5)` |
| 6 | `06_feature_selection_evaluation.ipynb` | Exp1–Exp4 comparison → **Exp3 selected** |

### 🎯 Task 7: User Preferences & Interaction Data (Next)
- [ ] Design a **simulated** user–talk interaction dataset (`user_id`, `talk_id`, `rating`, `liked`, `watched_at`)
- [ ] Save to `data/interaction/user_interactions.csv`
- [ ] Build the user–item interaction matrix
- [ ] Analyse top-rated talks, most active users, most-interacted talks
- [ ] Explain collaborative filtering and the cold-start problem
- [ ] Notebook: `07_user_interaction_data.ipynb`

### 🎯 Task 8: Collaborative Filtering
- [ ] User-based CF with cosine similarity between users
- [ ] `recommend_for_user(user_id, top_n=5)`
- [ ] Exclude already-rated talks, handle invalid users
- [ ] Join recommendations back to talk titles
- [ ] Notebook: `08_collaborative_filtering.ipynb`

### 🔮 Future Enhancements

| Priority | Feature | Description |
|----------|---------|-------------|
| 🔥 High | **Hybrid Model** | Combine content-based (Exp3) + collaborative signals |
| 🔥 High | **Streamlit App** | Search, filters, and recommendation display |
| 🟡 Medium | **Semantic Search** | Sentence-BERT embeddings for meaning-level matching |
| 🟡 Medium | **Diversity Reranking** | MMR to avoid near-duplicate recommendations |
| 🟡 Medium | **Field Weighting** | Tags ×3, title ×2, description ×1.5 instead of plain concatenation |
| 🟢 Low | **Real-time API** | FastAPI service with caching |
| 🟢 Low | **Explainability** | Highlight matching phrases behind each recommendation |
| 🟢 Low | **Tokenizer Cleanup** | Strip digits / proper nouns, tune `token_pattern` |

---

## 📊 Evaluation

**Implemented** (notebook 06):
- **Average Tag Jaccard** — objective topical overlap between seed and recommendations
- **Qualitative review** — manual relevance judgment across 5 seeds × 4 experiments
- **Cosine score inspection** — used only for ranking within a pipeline

**Planned**:

```python
metrics = {
    "precision_at_k": "Relevance of top-k recommendations",
    "diversity": "Intra-list diversity (1 - avg pairwise similarity)",
    "novelty": "How obscure/surprising are recommendations",
    "coverage": "% of catalog that can be recommended",
    "serendipity": "Unexpected but relevant recommendations"
}
```

---

## 🤝 Contributing

Contributions are welcome.

```bash
# 1. Fork the repo
# 2. Create a feature branch
git checkout -b feature/amazing-feature
# 3. Commit changes
git commit -m "Add amazing feature"
# 4. Push to branch
git push origin feature/amazing-feature
# 5. Open a Pull Request
```

Please keep notebooks executed with visible outputs, avoid committing `data/processed/` or `.venv/`, and document any new experiment with its metric and seed talks.

---

## 🙏 Acknowledgments

| Resource | Link |
|----------|------|
| **Dataset** | [TED Ultimate Dataset on Kaggle](https://www.kaggle.com/datasets/miguelcorraljr/ted-ultimate-dataset/data) |
| **TF-IDF Theory** | [scikit-learn Documentation](https://scikit-learn.org/stable/modules/feature_extraction.html#tfidf-term-weighting) |
| **Cosine Similarity** | [Wikipedia](https://en.wikipedia.org/wiki/Cosine_similarity) |
| **TED Talks** | [TED.com](https://www.ted.com/talks) |

---

## 📬 Contact

<p align="center">
  <a href="https://github.com/balabhadra3141">
    <img src="https://img.shields.io/badge/GitHub-100000?style=for-the-badge&logo=github&logoColor=white" alt="GitHub">
  </a>
</p>

---

<p align="center">
  <b>Made with ❤️ for TED enthusiasts everywhere</b><br>
  <sub>Star ⭐ this repo if you found it helpful!</sub>
</p>

<!--
  Badge references:
  https://shields.io/
  https://github.com/Ileriayo/markdown-badges
-->
