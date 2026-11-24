# Processed Data Documentation

This folder holds the datasets and model artifacts produced by the notebook pipeline. Most files are too large for GitHub, so they are **gitignored and must be regenerated** by running the notebooks in order. The written reports live in `reports/` at the project root and are committed.

This document is the single source of truth for:

- what each notebook **takes in**
- what it **produces**
- what the data **looks like after that step**
- which later notebook or component **uses it**

---

## ✅ Final Deliverables at a Glance

| Purpose | File | Produced by |
|---------|------|-------------|
| **Final cleaned dataset** | `data/processed/ted_talks_cleaned.csv` | Notebook 03 |
| **Final recommender matrix** | `data/processed/cosine_sim_exp3.npy` | Notebook 06 |
| **Final TF-IDF matrix** | `data/processed/tfidf_matrix_exp3.npz` | Notebook 06 |
| **Final fitted vectorizer** | `data/processed/tfidf_vectorizer_exp3.joblib` | Notebook 06 |
| **Audit copy (original + cleaned text)** | `data/processed/ted_talks_cleaned_all.csv` | Notebook 03 |
| **Task 6 written report** | `reports/task_06_observations.md` + `.pdf` | Notebook 06 |

> **Use the `*_exp3` artifacts for recommendations.** The non-suffixed `tfidf_matrix.npz` / `cosine_sim.npy` / `tfidf_vectorizer.joblib` are the Task 4 **baseline** (full transcript text) and are kept only so the Task 4 experiment and the Task 6 comparison can be reproduced.

---

## 🔄 Data Flow Overview

| Step | Notebook | Input | Output | Used by |
|------|----------|-------|--------|---------|
| 1 | `01_data_exploration.ipynb` | `data/raw/ted_talks_en.csv` | `data/raw/ted_talks_selected.csv` | 02, 03 |
| 2 | `02_eda_data_quality.ipynb` | `data/raw/ted_talks_selected.csv` | *None* (analysis + inline charts) | Findings guide 03 |
| 3 | `03_data_cleaning_preprocessing.ipynb` | `data/raw/ted_talks_selected.csv` | `ted_talks_cleaned_all.csv`, `ted_talks_cleaned.csv` | 04, 05, 06, future 07/08, Streamlit |
| 4 | `04_tfidf_vectorization.ipynb` | `ted_talks_cleaned.csv` | `tfidf_matrix.npz`, `cosine_sim.npy`, `tfidf_vectorizer.joblib` | 05 (baseline), 06 (comparison) |
| 5 | `05_content_based_recommendation.ipynb` | `ted_talks_cleaned.csv` + Task 4 artifacts | *None* (`recommend_talks()` lives in the notebook) | 06, future module/app |
| 6 | `06_feature_selection_evaluation.ipynb` | `ted_talks_cleaned.csv` | `tfidf_matrix_exp3.npz`, `cosine_sim_exp3.npy`, `tfidf_vectorizer_exp3.joblib`, `reports/task_06_observations.{md,pdf}` | **Final recommender**, future hybrid/Streamlit, submission/review |
| 7 | `07_user_interaction_data.ipynb` *(planned)* | `ted_talks_cleaned.csv` | `data/interaction/user_interactions.csv` | 08 |
| 8 | `08_collaborative_filtering.ipynb` *(planned)* | `user_interactions.csv` + `ted_talks_cleaned.csv` | CF model artifacts | Future hybrid model |

### What the dataset looks like after each step

| After notebook | Rows | Columns | State |
|----------------|-----:|--------:|-------|
| 01 | 4,005 | 12 | Selected + renamed columns, list/dict fields flattened |
| 02 | 4,005 | 12 | **Unchanged** — quality findings only |
| 03 | 4,005 | 20 (audit) / 16 (final) | Cleaned text, flags, combined text fields |
| 04 | 4,005 | 16 | **Unchanged** — baseline TF-IDF + similarity artifacts added |
| 05 | 4,005 | 16 | **Unchanged** — reusable recommendation function added |
| 06 | 4,005 | 16 | **Unchanged** — final Exp3 artifacts + Task 6 report added, Exp3 selected |

---

## 📁 Folder Layout

```text
data/
├── raw/
│   ├── ted_talks_en.csv              # 46 MB  - original Kaggle download (4005 × 19)
│   └── ted_talks_selected.csv        # 43 MB  - 12 selected columns (4005 × 12)
│
├── processed/
│   ├── processed_data.md             # this document (safe to commit)
│   │
│   ├── ted_talks_cleaned_all.csv     # 165 MB - audit file (4005 × 20)
│   ├── ted_talks_cleaned.csv         # 123 MB - FINAL cleaned dataset (4005 × 16)
│   │
│   ├── tfidf_matrix_exp3.npz         # 1.6 MB - FINAL sparse TF-IDF (4005 × 23,643)
│   ├── cosine_sim_exp3.npy           # 128 MB - FINAL dense similarity (4005 × 4005)
│   ├── tfidf_vectorizer_exp3.joblib  # 0.6 MB - FINAL fitted vectorizer
│   │
│   ├── tfidf_matrix.npz              # 22 MB  - baseline sparse TF-IDF (4005 × 366,288)
│   ├── cosine_sim.npy                # 128 MB - baseline dense similarity (4005 × 4005)
│   └── tfidf_vectorizer.joblib       # 10 MB  - baseline fitted vectorizer
│
└── interaction/                      # planned (Task 7)
    └── user_interactions.csv

reports/                              # committed (not gitignored)
├── task_06_observations.md           # 4.6 KB - Task 6 written report
└── task_06_observations.pdf          # 254 KB - PDF export
```

---

## 1️⃣ `01_data_exploration.ipynb`

### Input

| File | Shape | Size | Description |
|------|------:|-----:|-------------|
| `data/raw/ted_talks_en.csv` | 4,005 × 19 | 46 MB | Original Kaggle **TED Ultimate Dataset** (English talks) |

### Processing

- Inspects rows, columns, dtypes, missing values, duplicates, and unique talk IDs.
- Selects 12 core columns from the original 19.
- Renames `speaker_1` → `speaker`, `topics` → `tags`, `occupations` → `speaker_occupation`.
- Parses dictionary/list strings into plain comma-separated values.
- **No rows are dropped and no values are imputed** — cleaning decisions are deferred to Task 3.

### Output

| File | Shape | Size | Description |
|------|------:|-----:|-------------|
| `data/raw/ted_talks_selected.csv` | 4,005 × 12 | 43 MB | Analysis-ready subset used by all later notebooks |

**Columns (12):** `talk_id`, `title`, `speaker`, `speaker_occupation`, `description`, `tags`, `transcript`, `url`, `views`, `duration`, `published_date`, `event`

### Final processed data after this notebook

A 4,005 × 12 table. All core text and URL fields are complete, and every talk has a transcript. `speaker_occupation` still has **522 missing values (13.03%)**, deliberately left for Task 3. There are no duplicate rows, duplicate `talk_id`s, or duplicate URLs.

> Note: notebook 01's inline `isnull()` output is stale relative to the saved file. The authoritative count — 522 missing `speaker_occupation` values — is confirmed in notebooks 02 and 03 and in `ted_talks_selected.csv` itself.

### Where it is used

- **Notebook 02** — EDA and data-quality assessment.
- **Notebook 03** — the only source for cleaning.

---

## 2️⃣ `02_eda_data_quality.ipynb`

### Input

| File | Shape | Size |
|------|------:|-----:|
| `data/raw/ted_talks_selected.csv` | 4,005 × 12 | 43 MB |

### Processing

- Missing-value and duplicate analysis.
- Description/transcript word-count statistics.
- Tag frequency analysis (31,700 mentions, 457 unique tags).
- Duration and views distributions.
- Charts are rendered inline in the notebook.

### Output

**No files are written.** The notebook is analysis-only and intentionally does not modify the dataset.

### Final processed data after this notebook

**The dataset is unchanged** (4,005 × 12). The value produced is the quality report that drives Task 3 decisions:

| Finding | Consequence in Task 3 |
|---------|-----------------------|
| `speaker_occupation` missing in 522 rows (13.03%) | Fill with `"unknown"` instead of dropping rows |
| 10 transcripts < 50 words | Keep + flag with `is_short_transcript` |
| No missing/duplicate core text | No row removal needed |
| Tags are free-form, mixed case | Lowercase, deduplicate, re-join |
| Views heavily skewed | Log-transform before any future popularity ranking |

### Where it is used

- **Notebook 03** — cleaning plan and documented decisions.

---

## 3️⃣ `03_data_cleaning_preprocessing.ipynb`

### Input

| File | Shape | Size |
|------|------:|-----:|
| `data/raw/ted_talks_selected.csv` | 4,005 × 12 | 43 MB |

### Processing

1. Coerce text columns to strings; empty/`"nan"`/`"none"` → `""`.
2. Fill missing `speaker_occupation` with `"unknown"`.
3. Deduplicate on `talk_id` (safe-guard; 0 rows removed).
4. Clean `title`, `description`, `transcript`, `tags`:
   - lowercase
   - remove URLs and HTML tags
   - remove TED noise markers (`(laughter)`, `(applause)`, `(music)`, `(audience)`, `(mechanical noises)`)
   - replace punctuation with spaces
   - collapse whitespace
5. Deduplicate tags and re-join with `, `.
6. Add `transcript_word_count` and `is_short_transcript`.
7. Build two combined text fields:
   - `combined_text` — plain `title + tags + description + transcript`
   - `combined_text_prefixed` — `title: … tags: … description: … transcript: …`

### Outputs

| File | Shape | Size | Description |
|------|------:|-----:|-------------|
| `data/processed/ted_talks_cleaned_all.csv` | 4,005 × 20 | 165 MB | **Audit file** — original + cleaned columns, flags, combined text |
| `data/processed/ted_talks_cleaned.csv` | 4,005 × 16 | 123 MB | **Final cleaned dataset** used by all later notebooks |

**Audit columns (20):** the 12 originals + `title_clean`, `description_clean`, `transcript_clean`, `tags_clean`, `combined_text`, `combined_text_prefixed`, `transcript_word_count`, `is_short_transcript`

**Final columns (16):** `talk_id`, `title`, `speaker`, `speaker_occupation`, `description`, `tags`, `transcript`, `url`, `views`, `duration`, `published_date`, `event`, `transcript_word_count`, `is_short_transcript`, `combined_text`, `combined_text_prefixed`

> In the final file, the cleaned `*_clean` columns are renamed back to `title`, `description`, `tags`, `transcript`. The original text survives only in `ted_talks_cleaned_all.csv`.

### Final processed data after this notebook

**4,005 rows × 16 columns**, fully cleaned and analysis-ready:

- 0 missing values (occupation filled with `"unknown"`)
- 0 duplicate rows / `talk_id` / `url`
- 10 rows flagged `is_short_transcript = True`
- `title`, `description`, `tags`, and `transcript` are lowercase, punctuation-free, and noise-free (`speaker` and `url` keep their original form)
- Two combined text variants ready for vectorization

### Where it is used

- **Notebook 04** — TF-IDF on `combined_text_prefixed`.
- **Notebook 05** — loads the dataset + artifacts for `recommend_talks()`.
- **Notebook 06** — builds all four feature experiments from `title`, `description`, `tags`, `transcript`.
- **Future Tasks 7/8** — talk metadata (`talk_id`, `title`) for interaction data and CF output.
- **Future Streamlit app** — titles, speakers, tags, views, URLs for display and filters.

---

## 4️⃣ `04_tfidf_vectorization.ipynb`

### Input

| File | Shape | Size |
|------|------:|-----:|
| `data/processed/ted_talks_cleaned.csv` | 4,005 × 16 | 123 MB |

### Processing

```python
TfidfVectorizer(
    stop_words="english",
    ngram_range=(1, 2),
    min_df=2,
    max_df=0.9,
)
```

- Fit on **`combined_text_prefixed`** (title + tags + description + transcript).
- Cosine similarity computed on the full sparse matrix.
- Diagonal set to `0.0` so a talk never recommends itself.

### Outputs (Baseline — not the final recommender)

| File | Shape | Size | Description |
|------|------:|-----:|-------------|
| `data/processed/tfidf_matrix.npz` | 4,005 × 366,288 | 22 MB | Sparse TF-IDF, 3,123,292 non-zeros |
| `data/processed/cosine_sim.npy` | 4,005 × 4,005 | 128 MB | Dense `float64` similarity, diagonal = 0 |
| `data/processed/tfidf_vectorizer.joblib` | — | 10 MB | Fitted vectorizer |

### Final processed data after this notebook

The cleaned dataset is **unchanged**. Added artifacts represent the **full-text baseline** (transcripts included). Observed limitations:

- Frequent names beat topics (`tipper` ranked above `climate`).
- Numeric tokens (`000`, `000 morning`, …) polluted the vocabulary.
- Education/creativity seed drifted off-topic by rank 3.
- Absolute cosine scores are low (0.13–0.17) because transcripts are long.

### Where it is used

- **Notebook 05** — loads these artifacts to power `recommend_talks()`.
- **Notebook 06** — the full-text setup corresponds closely to Exp4 (it uses the field-prefixed variant, so the vocabulary differs slightly) and serves as the comparison baseline.
- **Not for production** — Task 6 supersedes these with Exp3 artifacts.

---

## 5️⃣ `05_content_based_recommendation.ipynb`

### Input

| File | Shape | Size |
|------|------:|-----:|
| `data/processed/ted_talks_cleaned.csv` | 4,005 × 16 | 123 MB |
| `data/processed/tfidf_matrix.npz` | 4,005 × 366,288 | 22 MB |
| `data/processed/cosine_sim.npy` | 4,005 × 4,005 | 128 MB |
| `data/processed/tfidf_vectorizer.joblib` | — | 10 MB |

> If the three artifacts are missing, the notebook rebuilds them once and saves them back.

### Processing

- Defines `recommend_talks(title, top_n=5)`.
- Title resolution: **exact** (case-insensitive) → **partial/substring** → **fuzzy suggestion** (`difflib`).
- Validates `top_n` ∈ `[1, 20]`.
- Excludes the seed talk from its own recommendations.
- Returns a readable DataFrame: `Rank`, `Talk ID`, `Recommended Title`, `Similarity Score`.
- Tested with exact, different-case, partial, ambiguous, typo, invalid `top_n`, and custom `top_n` cases.

### Output

**No files are written.** The reusable function lives in the notebook; all test outputs are stored inline.

### Final processed data after this notebook

**The dataset and artifacts are unchanged.** The added value is the tested recommendation API and its documented matching/validation behavior.

### Where it is used

- **Notebook 06** — reuses the same matching logic in its experiment-aware `recommend(title, experiment, top_n)`.
- **Future module/app** — will be wrapped into a Python module and exposed through Streamlit.

---

## 6️⃣ `06_feature_selection_evaluation.ipynb`

### Input

| File | Shape | Size |
|------|------:|-----:|
| `data/processed/ted_talks_cleaned.csv` | 4,005 × 16 | 123 MB |

### Processing

Builds four TF-IDF + cosine pipelines **in memory** and compares them on 5 seed talks:

| Experiment | Columns | Vocabulary |
|------------|---------|-----------:|
| Exp1 | `title` | 2,515 |
| Exp2 | `title` + `tags` | 7,508 |
| **Exp3 ✅** | **`title` + `description` + `tags`** | **23,643** |
| Exp4 | `title` + `description` + `transcript` + `tags` | 363,947 |

Evaluation:

- **Average Tag Jaccard** between seed and recommended talks.
- **Qualitative review** of top-5 recommendations for each seed.
- Cosine scores compared only within each pipeline.

**Selected: Exp3 — Title + Description + Tags.**

### Outputs (Final Recommender Artifacts + Report)

| File | Shape | Size | Description |
|------|------:|-----:|-------------|
| `data/processed/tfidf_matrix_exp3.npz` | 4,005 × 23,643 | 1.6 MB | Sparse TF-IDF, 200,047 non-zeros |
| `data/processed/cosine_sim_exp3.npy` | 4,005 × 4,005 | 128 MB | Dense `float64` similarity, diagonal = 0 |
| `data/processed/tfidf_vectorizer_exp3.joblib` | — | 0.6 MB | Fitted Exp3 vectorizer |
| `reports/task_06_observations.md` | — | 4.6 KB | Written report: setup, comparison tables, evaluation, justification |
| `reports/task_06_observations.pdf` | — | 254 KB | PDF export via `markdown-pdf` |

> The Markdown report is written first; the PDF is then generated with the `markdown-pdf` package (`%pip install markdown-pdf`). The `reports/` files are committed, unlike the large `data/processed/` artifacts.

### Final processed data after this notebook

**This is the final state of the processed data:**

- Cleaned dataset: `ted_talks_cleaned.csv` (4,005 × 16)
- Final feature set: **title + description + tags**
- Final matrix: 4,005 × 23,643 (200,047 non-zeros)
- Final similarity: 4,005 × 4,005, self-similarity = 0
- Task 6 report: `reports/task_06_observations.md` + `.pdf`
- Exp3 is ~15× smaller than the Exp4 vocabulary and builds in under a second

### Where it is used

- **Final content-based recommender** — load `cosine_sim_exp3.npy` + `ted_talks_cleaned.csv`.
- **Future hybrid model** — content-based component alongside collaborative filtering.
- **Future Streamlit app** — fast, deployable similarity lookups.
- **Submission/review** — `reports/task_06_observations.md` and `.pdf` document the experiment, metrics, and final choice.

---

## 🧭 Which File Should I Use?

| Goal | Files |
|------|-------|
| **Generate recommendations (final)** | `ted_talks_cleaned.csv` + `cosine_sim_exp3.npy` |
| Vectorize a **new** query/title | `tfidf_vectorizer_exp3.joblib` |
| Inspect raw vs cleaned text | `ted_talks_cleaned_all.csv` |
| Reproduce the **Task 4 baseline** | `tfidf_matrix.npz`, `cosine_sim.npy`, `tfidf_vectorizer.joblib` |
| Read or submit the **Task 6 report** | `reports/task_06_observations.md`, `reports/task_06_observations.pdf` |
| Rebuild everything from scratch | Run notebooks 01 → 06 in order |

---

## 🧾 Cleaned Dataset Column Reference

| Column | Type | Notes |
|--------|------|-------|
| `talk_id` | int | Unique talk identifier |
| `title` | text | Cleaned, lowercase |
| `speaker` | text | Speaker name (original case) |
| `speaker_occupation` | text | Cleaned; `"unknown"` when missing |
| `description` | text | Cleaned summary |
| `tags` | text | Comma-separated, lowercased, deduplicated |
| `transcript` | text | Cleaned full transcript |
| `url` | text | Original TED talk URL |
| `views` | int | View count (skewed) |
| `duration` | int | Seconds |
| `published_date` | date | Original publication date |
| `event` | text | TED / TEDx event name |
| `transcript_word_count` | int | Word count of cleaned transcript |
| `is_short_transcript` | bool | `True` when < 50 words (10 talks) |
| `combined_text` | text | Plain join: title + tags + description + transcript |
| `combined_text_prefixed` | text | Field-prefixed join used by the Task 4 baseline |

---

## 🔁 Regeneration Instructions

### 1. Ensure the raw data exists

Place the original Kaggle file at:

```text
data/raw/ted_talks_en.csv
```

### 2. Run the notebooks in order

```bash
jupyter nbconvert --execute notebooks/01_data_exploration.ipynb --to notebook --inplace
jupyter nbconvert --execute notebooks/02_eda_data_quality.ipynb --to notebook --inplace
jupyter nbconvert --execute notebooks/03_data_cleaning_preprocessing.ipynb --to notebook --inplace
jupyter nbconvert --execute notebooks/04_tfidf_vectorization.ipynb --to notebook --inplace
jupyter nbconvert --execute notebooks/05_content_based_recommendation.ipynb --to notebook --inplace
jupyter nbconvert --execute notebooks/06_feature_selection_evaluation.ipynb --to notebook --inplace
```

Or open each notebook in Jupyter/VS Code and **Run All** cells sequentially.

### 3. Minimum path to the final recommender

If `data/raw/ted_talks_selected.csv` is already present, you can skip notebook 01:

```text
03 → 06
```

Notebook 06 only needs `ted_talks_cleaned.csv`; it does not depend on the Task 4 baseline artifacts.

### 4. PDF report

Notebook 06 writes `reports/task_06_observations.md` and then generates the PDF with `markdown-pdf`, which the notebook installs itself:

```text
%pip install markdown-pdf
```

No external `pandoc` or LaTeX installation is required. Re-running the final notebook cells regenerates both report files.

---

## 🗂️ Planned Data (Tasks 7–8)

| File | Produced by | Used by | Description |
|------|-------------|---------|-------------|
| `data/interaction/user_interactions.csv` | Notebook 07 | Notebook 08, future hybrid model | **Simulated** user–talk interactions: `user_id`, `talk_id`, `rating`, `liked`, `watched_at` |
| User–item matrix | Notebook 07/08 | Notebook 08 | Users × talks, values = ratings, missing = no interaction |
| User similarity matrix | Notebook 08 | `recommend_for_user()` | Cosine similarity between users |
| CF recommendation output | Notebook 08 | Future hybrid model | `user_id`, `talk_id`, `title`, predicted score |

> Task 7 data is **simulated for learning purposes** and must be labelled as such.

---

## 📝 Notes

- **Do not commit** the CSV/NPY/NPZ/JOBLIB files in this folder — most exceed 100 MB.
- `data/processed/` is excluded in `.gitignore`; only `processed_data.md` is meant to be committed.
- Raw data in `data/raw/` is small enough to commit.
- File sizes are approximate and use decimal MB.
- Notebook 01 writes to `data/raw/`; notebook 02 writes no files; notebooks 03–06 write to `data/processed/`.
- Notebook 06 also writes the Task 6 report to `reports/`, which **is** committed (4.6 KB Markdown + 254 KB PDF).
- `cosine_sim*.npy` files are dense `float64` (128 MB each). If disk size becomes an issue, they can be recomputed on demand from the corresponding `tfidf_matrix*.npz`.
- The Exp3 artifacts are the **final** ones. The non-suffixed artifacts are the Task 4 baseline and are intentionally retained for comparison.
