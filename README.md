# TED Talks Recommendation System

Beginner-friendly notebooks for Tasks 1–8 of the internship project.

## Dataset used

`data/raw/ted_talks_merged.csv` is the CSV supplied for this project. It has 2,550 rows and 18 columns. The notebook analysis found 86 missing transcripts, 6 missing speaker occupations, and no exact duplicate rows. Its `ratings` column is aggregated reaction counts, not person-level ratings. The file does not contain an `id` or `talk_id` column; Task 3 derives `talk_id` from the unique `name` slug (URL fallback).

The upstream download source and licence are not recorded in the CSV. Verify those with the original provider before redistributing the dataset.

## Setup (Windows PowerShell)

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
python -m jupyter notebook
```

Open the notebooks in order, from `01` to `08`. Task 3 creates `data/processed/ted_talks_cleaned.csv`; Task 7 creates `data/interaction/user_interactions.csv`. Both generated CSVs are included in this project bundle as well, but can be recreated by running their notebooks.

## Notebooks

1. `01_data_exploration.ipynb` — environment, dataset shape, columns, missing values, duplicates.
2. `02_eda_data_quality.ipynb` — EDA, missing-value percentages, text lengths, tags and plots.
3. `03_data_cleaning_preprocessing.ipynb` — preserves raw fields, creates clean text, `talk_id`, and `combined_text`.
4. `04_tfidf_vectorization.ipynb` — TF-IDF vocabulary and talk-to-talk cosine similarity.
5. `05_content_based_recommendation.ipynb` — reusable `recommend_talks(title, top_n=5)`.
6. `06_feature_selection_evaluation.ipynb` — compares the four assigned feature combinations.
7. `07_user_interaction_data.ipynb` — builds an explicitly simulated interaction dataset and user-item matrix.
8. `08_collaborative_filtering.ipynb` — user-user similarity and `recommend_for_user()`.

## Important notes

- Keep `data/raw/ted_talks_merged.csv` unchanged.
- Missing transcripts are retained; their cleaned transcript text is an empty string.
- `talk_id` is derived from `name` because the supplied file does not contain an ID field.
- Task 7 and Task 8 use simulated interactions, not real user data.
- Task 6 requires manual relevance review; similarity scores alone do not prove recommendation quality.
- Do not commit `.venv/` to Git.
