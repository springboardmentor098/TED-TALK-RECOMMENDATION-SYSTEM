# Task 4 — TF-IDF Vectorization and Similarity Analysis

**Notebook:** `notebooks/04_tfidf_vectorization.ipynb`  
**Task:** 4 of 8  
**Status:** Complete

---

## 1. Objective

Convert the cleaned TED Talks text into numerical vectors with TF-IDF, compute cosine similarity between all talks, and generate the first set of content-based recommendations.

---

## 2. Input

| File | Shape | Size |
|------|------:|-----:|
| `data/processed/ted_talks_cleaned.csv` | 4,005 × 16 | ~123 MB |

The notebook uses the `combined_text_prefixed` column, which contains title, tags, description, and transcript with field markers.

---

## 3. Method

### TF-IDF configuration

```python
TfidfVectorizer(
    stop_words="english",
    ngram_range=(1, 2),
    min_df=2,
    max_df=0.9,
)
```

| Parameter | Meaning |
|-----------|---------|
| `stop_words="english"` | Remove common English words such as “the” and “and” |
| `ngram_range=(1, 2)` | Use single words and two-word phrases |
| `min_df=2` | Ignore terms that appear in only one talk |
| `max_df=0.9` | Ignore terms that appear in more than 90% of talks |

### Similarity

Cosine similarity compares the angle between two TF-IDF vectors:

- `1.0` — identical term distribution
- `0.0` — no shared weighted terms

The full 4,005 × 4,005 similarity matrix is computed, and the diagonal is set to `0.0` so a talk cannot recommend itself.

---

## 4. TF-IDF Results

| Metric | Value |
|--------|------:|
| Matrix shape | 4,005 × 366,288 |
| Vocabulary size | 366,288 terms |
| Non-zero entries | 3,123,292 |
| Sparsity | ~99.8% |
| Build time | ~11.7 s |

### Example: top-weighted terms for “Averting the climate crisis”

| Rank | Term | Weight |
|-----:|------|-------:|
| 1 | `tipper` | 0.2052 |
| 2 | `carbon` | 0.1426 |
| 3 | `cars trucks` | 0.1178 |
| 4 | `nashville` | 0.1178 |
| 5 | `slideshow` | 0.1151 |
| 6 | `climate` | 0.1093 |
| 7 | `cost family` | 0.1063 |
| 8 | `family restaurant` | 0.1063 |
| 9 | `climate crisis` | 0.1032 |
| 10 | `global warming` | 0.0982 |

This already shows a key limitation: a frequently repeated person name (`tipper`) outranks the actual topic (`climate`).

---

## 5. Cosine Similarity Results

| Metric | Value |
|--------|------:|
| Matrix shape | 4,005 × 4,005 |
| Data type | `float64` |
| Value range | 0.0 – 0.9784 |
| Diagonal | 0.0 (self-similarity removed) |
| Computation time | ~2.7 s |

Absolute scores are low for most pairs because transcripts are long and the vocabulary is large. The ranking order is more meaningful than the absolute score.

---

## 6. Sample Recommendations

### Seed: “Averting the climate crisis” (`talk_id` 1)

| Rank | Talk ID | Recommended talk | Score |
|-----:|--------:|------------------|------:|
| 1 | 243 | New thinking on the climate crisis | 0.1748 |
| 2 | 54715 | How we can turn the tide on climate | 0.1643 |
| 3 | 2784 | A climate solution where all sides can win | 0.1433 |
| 4 | 2441 | The case for optimism on climate change | 0.1423 |
| 5 | 3579 | Can we stop climate change by removing CO2 from the air? | 0.1382 |

**Assessment:** 5/5 recommendations are climate-related. Strong thematic cluster.

### Seed: “Do schools kill creativity?” (`talk_id` 66)

| Rank | Talk ID | Recommended talk | Score |
|-----:|--------:|------------------|------:|
| 1 | 1738 | How to escape education's death valley | 0.1710 |
| 2 | 865 | Bring on the learning revolution | 0.1646 |
| 3 | 209 | Rebuilding a neighborhood with beauty, dignity, hope | 0.1397 |
| 4 | 61930 | It's OK to feel overwhelmed — here's what to do next | 0.1362 |
| 5 | 2182 | How to run a company with almost no rules | 0.1348 |

**Assessment:** Ranks 1–2 are strong education/creativity matches. Ranks 3–5 drift into generic “rethink/people” language.

### Seed: “Simplicity sells” (`talk_id` 7)

| Rank | Talk ID | Recommended talk | Score |
|-----:|--------:|------------------|------:|
| 1 | 495 | Cool tricks your phone can do | 0.1527 |
| 2 | 1268 | 6 ways to save the internet | 0.1413 |
| 3 | 172 | Designing for simplicity | 0.1348 |
| 4 | 2664 | Meet the inventor of the electronic spreadsheet | 0.1342 |
| 5 | 845 | Toward a science of simplicity | 0.1338 |

**Assessment:** The design/technology cluster holds, with two direct “simplicity” matches.

---

## 7. Observations and Limitations

1. **Frequent names beat topics.** `tipper` is the highest-weighted term for Al Gore's climate talk because it repeats often and is rare elsewhere.
2. **Numbers leak into the vocabulary.** Terms such as `000`, `000 morning`, and `000 100` appear because digits were not stripped in Task 3. They add noise and inflate the matrix.
3. **Off-topic drift occurs.** The creativity seed drifts by rank 3 because generic phrases (“rethink”, “people”) are shared with unrelated talks.
4. **Absolute scores are low but ranking still works.** Scores of 0.13–0.17 are normal for long documents; a fixed threshold would return nothing useful.
5. **Popularity is ignored.** Cosine similarity does not know that one talk has millions of views and another has a few thousand.
6. **Short transcripts score lower by design.** The 10 performance talks have little text, so their similarity is structurally weaker even when the match is correct.
7. **Self-recommendation is prevented twice.** The diagonal is zeroed, and the recommendation helper excludes the seed index.

---

## 8. Outputs

| File | Shape | Size | Description |
|------|------:|-----:|-------------|
| `data/processed/tfidf_matrix.npz` | 4,005 × 366,288 | ~22 MB | Sparse TF-IDF matrix |
| `data/processed/cosine_sim.npy` | 4,005 × 4,005 | ~128 MB | Dense cosine similarity, diagonal = 0 |
| `data/processed/tfidf_vectorizer.joblib` | — | ~10 MB | Fitted vectorizer |

These are the **Task 4 baseline** artifacts. They are superseded by the Exp3 artifacts selected in Task 6.

---

## 9. Next Step

Wrap the similarity lookup into a reusable `recommend_talks(title, top_n=5)` function in **Task 5** (`05_content_based_recommendation.ipynb`).
