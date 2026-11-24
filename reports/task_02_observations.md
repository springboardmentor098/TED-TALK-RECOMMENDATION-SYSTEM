# Task 2 — Exploratory Data Analysis and Data Quality Assessment

**Notebook:** `notebooks/02_eda_data_quality.ipynb`  
**Task:** 2 of 8  
**Status:** Complete

---

## 1. Objective

Analyse the selected TED Talks dataset to understand its structure, missing values, duplicates, text characteristics, tag distribution, duration, and view patterns, and produce the cleaning plan used in Task 3.

---

## 2. Input

| File | Shape | Size |
|------|------:|-----:|
| `data/raw/ted_talks_selected.csv` | 4,005 × 12 | ~43 MB |

---

## 3. Dataset Summary

| Check | Result |
|-------|--------|
| Rows | 4,005 |
| Columns | 12 |
| Unique `talk_id` | 4,005 |
| Duplicate `talk_id` | 0 |
| Duplicate rows | 0 |
| Duplicate URLs | 0 |

All core text and URL fields are present. The only column with missing values is `speaker_occupation`.

### Missing values

| Column | Missing | Percentage |
|--------|--------:|-----------:|
| `speaker_occupation` | 522 | 13.03% |
| All other columns | 0 | 0.00% |

No empty strings were detected in the core text fields.

---

## 4. Text Analysis

| Metric | Description | Transcript |
|--------|------------:|-----------:|
| Mean word count | ~58 | ~1,797 |
| Minimum | 9 | 2 |
| Maximum | 143 | 11,121 |
| Distribution | Short and consistent | Right-skewed |

- Descriptions are short summaries and rarely exceed 150 words.
- Transcripts are long and highly variable; most talks are several hundred to several thousand words.
- **10 transcripts contain fewer than 50 words.** These are music, dance, or performance pieces where the transcript is mostly stage directions.
- No empty descriptions or transcripts were found.

---

## 5. Tag Analysis

| Metric | Value |
|--------|------:|
| Total tag mentions | 31,700 |
| Unique tags | 457 |
| Average tags per talk | ~7.9 |

### Top 5 tags

| Rank | Tag | Talks |
|-----:|-----|------:|
| 1 | `science` | 993 |
| 2 | `technology` | 979 |
| 3 | `culture` | 680 |
| 4 | `tedx` | 581 |
| 5 | `global issues` | 574 |

The notebook also charts the top 15 tags. The remaining tags follow a long-tail distribution: a small set of broad topics covers many talks, while most tags appear in only a few talks.

Tags are stored as comma-separated strings after Task 1. They are free-form, so casing, spacing, and near-synonyms need normalisation.

---

## 6. Duration and Views

| Metric | Duration (seconds) | Views |
|--------|-------------------:|------:|
| Mean | ~724 s (~12 min) | ~2.15 M |
| Median | — | ~1.38 M |
| Minimum | 60 s | — |
| Maximum | 3,922 s (~65 min) | ~65 M |
| Distribution | Roughly typical talk length | Heavily right-skewed |

Views follow a power-law-like distribution. A small number of talks account for a very large share of views, so raw views should not be used as a ranking signal without a log transform.

---

## 7. Visualisations Produced

1. Distribution of description word counts.
2. Distribution of transcript word counts.
3. Top 15 most frequent tags (bar chart).
4. Distribution of talk duration.
5. Distribution of `log10(views + 1)`.

All charts are rendered inline in the notebook; no image files are saved.

---

## 8. Key Findings

1. The dataset is structurally clean: 4,005 unique talks, no duplicate rows, IDs, or URLs.
2. `speaker_occupation` is the only incomplete column (522 rows, 13.03%).
3. Transcripts are available for every talk, but 10 are effectively empty performance transcripts.
4. Descriptions are short and consistent; transcripts are long and highly variable.
5. Tags are numerous and long-tailed, with `science`, `technology`, `culture`, `tedx`, and `global issues` dominating.
6. Views are extremely skewed and need log transformation for any popularity-aware ranking.
7. Duration is concentrated around the standard TED length of roughly 12 minutes.

---

## 9. Cleaning Plan for Task 3

| Issue | Decision |
|-------|----------|
| Missing `speaker_occupation` (522) | Fill with `"unknown"`; do not drop 13% of the catalogue |
| Short transcripts (10) | Keep and flag with `is_short_transcript` |
| Tags are free-form | Lowercase, trim, deduplicate, and re-join |
| URLs/HTML/noise markers in text | Remove during text cleaning |
| Skewed views | Keep raw values; log-transform only if used for ranking |
| Duplicate records | None found; keep a dedupe safeguard in the pipeline |

---

## 10. Output

**No files are written.** The notebook is analysis-only. The dataset remains at 4,005 × 12 and is passed unchanged to Task 3.

---

## 11. Limitations

- The EDA measures text length, not text quality or semantic richness.
- Tag frequency does not reveal whether tags are consistently applied across talks.
- The analysis cannot measure recommendation relevance; that requires the vectorisation and evaluation stages.
- View counts reflect popularity on TED, not suitability for an individual user.

---

## 12. Next Step

Use these findings to clean and normalise the text in **Task 3** (`03_data_cleaning_preprocessing.ipynb`).
