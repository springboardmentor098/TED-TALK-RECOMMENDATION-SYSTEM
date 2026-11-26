# Task 5 - Content-Based Recommendation Engine

**Notebook:** `notebooks/05_content_based_recommendation.ipynb`  
**Task:** 5 of 8  
**Status:** Complete

---

## 1. Objective

Build a reusable function, `recommend_talks(title, top_n=5)`, that returns the most similar TED Talks for a given talk title using the TF-IDF and cosine-similarity artifacts from Task 4.

---

## 2. Inputs

| File | Shape | Size |
|------|------:|-----:|
| `data/processed/ted_talks_cleaned.csv` | 4,005 × 16 | ~123 MB |
| `data/processed/tfidf_matrix.npz` | 4,005 × 366,288 | ~22 MB |
| `data/processed/cosine_sim.npy` | 4,005 × 4,005 | ~128 MB |
| `data/processed/tfidf_vectorizer.joblib` | - | ~10 MB |

The function loads the dataset and artifacts once. If an artifact is missing, the notebook rebuilds it once and saves it back to disk.

---

## 3. Function Design

### Signature

```python
recommend_talks(title, top_n=5)
```

### Title matching strategy

1. **Exact match** - case-insensitive, whitespace-stripped.
2. **Partial / substring match** - if exactly one talk contains the input, use it.
3. **Ambiguous partial match** - if several talks contain the input, `difflib` picks the closest title and prints which one was chosen.
4. **Invalid title** - suggest the closest valid title with `difflib` and return `None`.
5. **Validation** - `top_n` must be an integer between 1 and 20.
6. **Self-exclusion** - the seed talk is removed from its own recommendations.

### Output

A pandas DataFrame with:

`Rank`, `Talk ID`, `Recommended Title`, `Similarity Score`

---

## 4. Test Cases

| # | Test | Input | Observed result |
|--:|------|-------|-----------------|
| 1 | Exact title | `Averting the climate crisis` | 5 climate recommendations |
| 2 | Different case | `HOW POLICING FOR PROFIT UNDERMINES YOUR RIGHTS` | Resolved and recommended 5 talks |
| 3 | Partial title | `climate crisis` | Auto-picked “averting the climate crisis” |
| 4 | Partial + case | `SCHOOLS KILL CREATIVITY` | Resolved to “do schools kill creativity” |
| 5 | Ambiguous partial | `simplicity` | Auto-picked “simplicity sells” |
| 6 | Typo / invalid | `Simplicity sale` | Suggested “simplicity sells”; returned `None` |
| 7 | Invalid `top_n` | `top_n=0` | Error message; returned `None` |
| 8 | Custom `top_n` | `top_n=10` | Returned 10 recommendations |
| 9 | Self-exclusion | Climate seed | Seed ID not present in results |

---

## 5. Example Output

### Seed: “How policing for profit undermines your rights”

| Rank | Talk ID | Recommended talk | Score |
|-----:|--------:|------------------|------:|
| 1 | 2406 | I love being a police officer, but we need reform | 0.2173 |
| 2 | 2239 | The hidden reason for poverty the world needs to address now | 0.1719 |
| 3 | 633 | The real story of McMafia - how global crime networks work | 0.1589 |
| 4 | 45612 | How policewomen make communities safer | 0.1526 |
| 5 | 1914 | Why smart statistics are the key to fighting crime | 0.1458 |

**Assessment:** The recommendations stay within policing, crime, and justice. This is a meaningful cluster even though the scores are low in absolute terms.

### Seed: “Averting the climate crisis” - top 10

| Rank | Recommended talk | Score |
|-----:|------------------|------:|
| 1 | New thinking on the climate crisis | 0.1748 |
| 2 | How we can turn the tide on climate | 0.1643 |
| 3 | A climate solution where all sides can win | 0.1433 |
| 4 | The case for optimism on climate change | 0.1423 |
| 5 | Can we stop climate change by removing CO2 from the air? | 0.1382 |
| 6 | Climate change is happening - here's how we adapt | 0.1339 |
| 7 | How we could change the planet's climate future | 0.1338 |
| 8 | 100 solutions to reverse global warming | 0.1316 |
| 9 | This country isn't just carbon neutral - it's carbon negative | 0.1304 |
| 10 | What comes after an inconvenient truth | 0.1303 |

All 10 recommendations are climate-related, showing that the ranking remains coherent beyond the top 5.

---

## 6. Review Questions

**How does the function handle partial titles?**  
It tries an exact match first, then a substring match. If several titles contain the substring, `difflib` selects the closest one and prints the choice.

**How does it handle invalid titles?**  
It uses `difflib.get_close_matches` to suggest the nearest valid title and returns `None`.

**Why zero the diagonal?**  
`cosine_similarity(talk_i, talk_i)` is always 1.0. Zeroing the diagonal prevents self-recommendation even if the filtering logic changes.

**Is the function reusable?**  
Yes. TF-IDF and cosine similarity are computed once and persisted. Each call is a cheap array lookup, not a full re-vectorisation.

**What happens with an invalid `top_n`?**  
The function prints an error and returns `None`; it does not silently coerce the value.

---

## 7. Observations and Limitations

- **Title-based input** is convenient but fragile: the user must know or approximate an existing title.
- **Ambiguous partial titles** are resolved automatically, which can silently pick a different talk than the user intended.
- **Fuzzy suggestions are conservative** (`cutoff=0.5`); heavily misspelled titles may return no suggestion.
- **The engine uses the Task 4 baseline** (full transcript text), which later experiments show is noisier than the Exp3 feature set.
- **No diversity control** exists; recommendations can cluster around the same speaker or series.
- **No personalisation** exists; every user receives the same result for the same seed.
- **Scores are not calibrated**; a score of 0.17 can be an excellent match for long transcripts.

---

## 8. Output

**No files are written.** The reusable function and all test outputs live in the notebook. The cleaned dataset and Task 4 artifacts are unchanged.

---

## 9. Next Step

Compare feature combinations and select the best one in **Task 6** (`06_feature_selection_evaluation.ipynb`).
