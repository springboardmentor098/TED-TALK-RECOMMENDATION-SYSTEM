# Task 3 - Data Cleaning and Text Preprocessing

**Notebook:** `notebooks/03_data_cleaning_preprocessing.ipynb`  
**Task:** 3 of 8  
**Status:** Complete

---

## 1. Objective

Use the Task 2 findings to clean the TED Talks dataset, handle missing values, normalise text fields, create combined text representations, and save a clean dataset for vectorisation.

---

## 2. Input

| File | Shape | Size |
|------|------:|-----:|
| `data/raw/ted_talks_selected.csv` | 4,005 × 12 | ~43 MB |

The raw input file is preserved unchanged.

---

## 3. Missing-Value Decisions

| Column | Decision | Reason |
|--------|----------|--------|
| `speaker_occupation` | Fill with `"unknown"` | Optional context; dropping would remove 13% of talks |
| `title`, `description`, `tags`, `transcript`, `url` | Coerce to string, strip; empty/`"nan"`/`"none"` -> `""` | Consistent representation; no real empty values were found |
| Short transcripts (< 50 words) | Keep and flag with `is_short_transcript` | Performance talks still have title, tags, and description |

After imputation, the cleaned dataset has **0 missing values**.

---

## 4. Duplicate Handling

| Check | Count |
|-------|------:|
| Duplicate rows | 0 |
| Duplicate `talk_id` | 0 |
| Duplicate `url` | 0 |

A `drop_duplicates(subset="talk_id")` safeguard is kept in the pipeline. It removes 0 rows on the current dataset but protects future reruns.

---

## 5. Text Cleaning Steps

The following steps are applied to `title`, `description`, `transcript`, and `tags`:

1. **Lowercase** the text.
2. **Remove URLs** (`http…`, `www…`).
3. **Remove HTML tags** (`<em>`, `<br>`, …).
4. **Remove TED transcript noise markers** such as `(laughter)`, `(applause)`, `(music)`, `(audience)`, and `(mechanical noises)`.
5. **Replace punctuation and non-alphanumeric characters with spaces.**
6. **Collapse repeated whitespace and strip.**

Tags receive an additional step: split on commas, clean each tag, drop empty tags, deduplicate, and re-join with `, `.

### Before / after examples

| Field | Original | Cleaned |
|-------|----------|---------|
| `title` | `Averting the climate crisis` | `averting the climate crisis` |
| `description` | `With the same humor and humanity he exuded in "An Inconvenient Truth," …` | `with the same humor and humanity he exuded in an inconvenient truth …` |
| `transcript` | `Thank you so much, Chris. And it's truly a great honor …` | `thank you so much chris and it s truly a great honor …` |
| `tags` | `alternative energy, cars, climate change, …` | `alternative energy, cars, climate change, …` (lowercased/deduplicated) |

---

## 6. Derived Columns

| Column | Description |
|--------|-------------|
| `transcript_word_count` | Number of words in the cleaned transcript |
| `is_short_transcript` | `True` when the transcript has fewer than 50 words |
| `combined_text` | Plain space join of `title + tags + description + transcript` |
| `combined_text_prefixed` | Field-prefixed join: `title: … tags: … description: … transcript: …` |

`combined_text` is the simple baseline. `combined_text_prefixed` preserves field boundaries so the fields can be weighted or separated later.

---

## 7. Outputs

| File | Shape | Size | Description |
|------|------:|-----:|-------------|
| `data/processed/ted_talks_cleaned_all.csv` | 4,005 × 20 | ~165 MB | Audit file: originals + cleaned text, flags, combined fields |
| `data/processed/ted_talks_cleaned.csv` | 4,005 × 16 | ~123 MB | Final cleaned deliverable used by later notebooks |

### Final column list (16)

`talk_id`, `title`, `speaker`, `speaker_occupation`, `description`, `tags`, `transcript`, `url`, `views`, `duration`, `published_date`, `event`, `transcript_word_count`, `is_short_transcript`, `combined_text`, `combined_text_prefixed`

The cleaned `*_clean` columns are renamed back to `title`, `description`, `tags`, and `transcript` in the final file. Original text remains available only in the audit file.

---

## 8. Before / After Summary

| Metric | Before | After |
|--------|-------:|------:|
| Rows | 4,005 | 4,005 |
| Columns | 12 | 16 (final) / 20 (audit) |
| Missing `speaker_occupation` | 522 | 0 |
| Duplicate rows / IDs / URLs | 0 | 0 |
| Short transcripts flagged | 10 | 10 |
| Combined text fields | 0 | 2 |

No talks were removed: every row still has usable text.

---

## 9. Limitations

- Punctuation removal splits contractions (e.g. `it's` -> `it s`), which adds minor noise.
- Digits are retained, so numeric tokens such as `000` can enter the vocabulary.
- No stemming, lemmatisation, spell correction, or named-entity removal is applied.
- Tags remain free-form; synonyms are not merged.
- Cleaning lowers case, so proper nouns and acronyms lose their original casing.

These limitations are accepted for the first prototype and revisited in later experiments.

---

## 10. Next Step

Use `ted_talks_cleaned.csv` in **Task 4** (`04_tfidf_vectorization.ipynb`) to build the first TF-IDF and cosine-similarity pipeline.
