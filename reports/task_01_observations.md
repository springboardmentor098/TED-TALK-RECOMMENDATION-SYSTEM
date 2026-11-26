# Task 1 - Environment Setup and Dataset Collection

**Notebook:** `notebooks/01_data_exploration.ipynb`  
**Task:** 1 of 8  
**Status:** Complete

---

## 1. Objective

Set up the Python development environment, collect a suitable TED Talks dataset, select the fields required for a content-based recommender, and perform an initial quality inspection before any cleaning.

---

## 2. Environment

| Item | Value |
|------|-------|
| Language | Python 3.11+ |
| Editor / runtime | VS Code + Jupyter Notebook |
| Virtual environment | `.venv/` (not committed) |
| Core packages | `pandas`, `numpy`, `matplotlib`, `seaborn`, `jupyter`, `scikit-learn` |
| Dependency file | `requirements.txt` |

The environment was verified with `python --version`, `python -m pip --version`, and `python -m pip list`. Notebooks are run from the `notebooks/` directory, so data paths use `../data/...`.

---

## 3. Dataset

| Item | Value |
|------|-------|
| Dataset | **TED Ultimate Dataset** |
| Source | [Kaggle - miguelcorraljr/ted-ultimate-dataset](https://www.kaggle.com/datasets/miguelcorraljr/ted-ultimate-dataset/data) |
| File used | `ted_talks_en.csv` |
| Raw shape | 4,005 rows × 19 columns |
| Language | English |
| Licence / usage | Public Kaggle dataset used for the internship project |

The raw file is stored at `data/raw/ted_talks_en.csv` and is never modified.

---

## 4. Initial Inspection

| Check | Result |
|-------|--------|
| Rows | 4,005 |
| Columns (raw) | 19 |
| Unique `talk_id` values | 4,005 |
| Duplicate `talk_id` values | 0 |
| Duplicate rows | 0 |
| Duplicate URLs | 0 |
| Missing `speaker_occupation` | 522 (13.03%) |
| Missing values in core text fields | 0 |
| Transcripts available | 4,005 / 4,005 |

The missing `speaker_occupation` values are preserved in the selected subset and handled later in Task 3. The printed null count inside the notebook is affected by cell execution order; the saved CSV and notebooks 02–03 show 522 missing values, which is the authoritative count.

---

## 5. Column Selection and Transformations

The raw 19 columns were reduced to **12 core columns**:

`talk_id`, `title`, `speaker`, `speaker_occupation`, `description`, `tags`, `transcript`, `url`, `views`, `duration`, `published_date`, `event`

Transformations applied:

1. Renamed `speaker_1` -> `speaker`.
2. Renamed `topics` -> `tags`.
3. Renamed `occupations` -> `speaker_occupation`.
4. Extracted the first speaker's occupation from the nested dictionary.
5. Converted occupation and tag lists into comma-separated strings.

No rows were dropped and no values were imputed at this stage.

---

## 6. Output

| File | Shape | Size | Description |
|------|------:|-----:|-------------|
| `data/raw/ted_talks_selected.csv` | 4,005 × 12 | ~43 MB | Analysis-ready subset used by all later notebooks |

**Used by:** notebook 02 (EDA) and notebook 03 (cleaning).

---

## 7. Limitations Identified

- **English-only** dataset; recommendations cannot serve non-English talks.
- **Tags are free-form** and may contain near-duplicates or inconsistent labels.
- **View counts are heavily skewed**, so popularity cannot be used directly without transformation.
- **No user interaction data** exists - collaborative filtering is not possible at this stage.
- **Transcript lengths vary widely**, including a small number of music/performance talks with almost no spoken text.
- The dataset has **no explicit quality or satisfaction signal**; textual similarity is only a proxy for relevance.

---

## 8. Key Takeaways

- The dataset is large enough (4,005 talks) for a meaningful first content-based prototype.
- The 12 selected columns cover titles, descriptions, tags, transcripts, and display metadata.
- Data quality is strong: no duplicate records and complete transcripts.
- Only `speaker_occupation` needs imputation, which is deferred to Task 3.
- The next step is a structured EDA and data-quality assessment before cleaning.
