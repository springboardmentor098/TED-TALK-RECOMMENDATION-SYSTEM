# Task 6 - Feature Selection and Recommendation Quality Evaluation

**Notebook:** `notebooks/06_feature_selection_evaluation.ipynb`  
**Task:** 6 of 8  
**Status:** Complete

---

## 1. Objective

Compare four feature combinations for the content-based recommender and select the one that produces the most relevant TED Talk recommendations.

---

## 2. Input

| File | Shape | Size |
|------|------:|-----:|
| `data/processed/ted_talks_cleaned.csv` | 4,005 × 16 | ~123 MB |

The notebook builds its own TF-IDF matrices per experiment, so it does not depend on the Task 4 baseline artifacts.

---

## 3. Experimental Setup

| Item | Value |
|------|-------|
| Model | TF-IDF + cosine similarity |
| TF-IDF config | `stop_words='english'`, `ngram_range=(1, 2)`, `min_df=2`, `max_df=0.9` |
| Top-N | 5 recommendations per seed |
| Seeds | Averting the climate crisis · Do schools kill creativity · Simplicity sells · The best stats you've ever seen · How policing for profit undermines your rights |

### Experiment pipelines

| Experiment | Input columns | TF-IDF vocabulary |
|------------|---------------|------------------:|
| Exp1 | `title` | 2,515 terms |
| Exp2 | `title` + `tags` | 7,508 terms |
| Exp3 ✅ | `title` + `description` + `tags` | 23,643 terms |
| Exp4 | `title` + `description` + `transcript` + `tags` | 363,947 terms |

---

## 4. Metric

**Average tag Jaccard** - the overlap between the seed talk's tags and the tags of its top-5 recommendations, averaged over the seeds. It is an objective topical-relevance proxy: higher means the recommendations share the seed's subject matter.

Tag Jaccard is a **partial** signal, because tags are literally part of the Exp2 input. It is therefore read alongside qualitative review, not in isolation.

---

## 5. Results

### Average tag Jaccard (higher = better topical overlap)

| Seed | Exp1 | Exp2 | Exp3 | Exp4 |
|------|-----:|-----:|-----:|-----:|
| Averting the climate crisis | 0.1362 | 0.3806 | 0.3490 | 0.2452 |
| Do schools kill creativity | 0.1254 | 0.4306 | 0.3058 | 0.2148 |
| How policing for profit undermines your rights | 0.0512 | 0.1337 | 0.2015 | 0.1476 |
| Simplicity sells | 0.0957 | 0.2400 | 0.2305 | 0.1156 |
| **Mean** | **0.1021** | **0.2962** | **0.2717** | **0.1808** |

### Average cosine score (only comparable within an experiment)

| Seed | Exp1 | Exp2 | Exp3 | Exp4 |
|------|-----:|-----:|-----:|-----:|
| Averting the climate crisis | 0.4037 | 0.3797 | 0.2815 | 0.1526 |
| Do schools kill creativity | 0.4006 | 0.2508 | 0.1907 | 0.1493 |
| How policing for profit undermines your rights | 0.3787 | 0.1907 | 0.1639 | 0.1697 |
| Simplicity sells | 0.3110 | 0.3315 | 0.2017 | 0.1394 |

### Matrix sizes

| Artifact | Shape | Non-zeros |
|----------|------:|----------:|
| Exp3 TF-IDF matrix | 4,005 × 23,643 | 200,047 |
| Exp4 TF-IDF matrix | 4,005 × 363,947 | - |

---

## 6. Evaluation

**Relevance:** Exp2 and Exp3 returned consistently topical recommendations. Exp1 surfaced near-duplicates from the same speaker/series. Exp4 drifted into unrelated talks (for the creativity seed it returned “Rebuilding a neighborhood…” and “It's OK to feel overwhelmed…”).

**Do recommendations discuss similar topics?** Yes for Exp2 and Exp3. Exp3 showed more conceptual variety - for the policing seed it returned rule-of-law and justice-system talks, while Exp2 stayed inside the literal tag cluster.

**Where do irrelevant results come from?** Most often from Exp4. Long transcripts inflate TF-IDF weights on repeated names and filler words; for Al Gore's climate talk, `tipper` outranked `climate`.

**Does the transcript help?** No. Exp4 had high raw cosine scores but the **lowest tag Jaccard**, meaning the similarity was structural (shared long vocabulary) rather than topical.

**Best combination?** Exp3 (Title + Description + Tags) has the best balance of relevance and diversity. Exp2 wins the Jaccard metric by a small margin because tags are literally in its input.

---

## 7. Final Selection

**Selected: Exp3 - Title + Description + Tags**

| Reason | Explanation |
|--------|-------------|
| Jaccard is partial | It measures only tag overlap, which structurally favours Exp2. Descriptions capture *what the talk argues*. |
| Qualitative review | For the policing seed, Exp2 returned unrelated talks; Exp3 returned rule-of-law and justice-system talks. |
| Avoids transcript noise | Exp4 inflates scores through long shared vocabulary but causes off-topic drift. |
| Balanced diversity | Exp1 yields near-duplicates, Exp2 stays narrow, Exp3 gives conceptually related but varied results. |
| Deployment-friendly | Exp3 is ~15× smaller than Exp4 and builds in under a second. |

**Not selected:**

- **Exp1 (Title only)** - too narrow, near-duplicate results.
- **Exp2 (Title + Tags)** - strong metric, but underuses descriptive text.
- **Exp4 (full text)** - highest cosine scores, lowest real-world relevance.

---

## 8. Outputs

| File | Shape | Size | Description |
|------|------:|-----:|-------------|
| `data/processed/tfidf_matrix_exp3.npz` | 4,005 × 23,643 | ~1.6 MB | Final sparse TF-IDF matrix |
| `data/processed/cosine_sim_exp3.npy` | 4,005 × 4,005 | ~128 MB | Final dense similarity, diagonal = 0 |
| `data/processed/tfidf_vectorizer_exp3.joblib` | - | ~0.6 MB | Fitted Exp3 vectorizer |

These are the **final** recommender artifacts. The non-suffixed Task 4 baseline artifacts are retained only for comparison.

---

## 9. Limitations

- Tag Jaccard is a proxy metric and is biased toward experiments whose input includes tags.
- The comparison uses only 5 seed talks, so it is indicative rather than exhaustive.
- Qualitative review is subjective and not reproducible by a metric.
- Exp3 still ignores popularity, speaker diversity, and user history.
- Scores are not calibrated across experiments; only rankings within an experiment are comparable.

---

## 10. Next Steps

- Use the Exp3 artifacts in the final content-based recommender.
- Proceed to **Task 7** (user interaction data) and **Task 8** (collaborative filtering) for a hybrid model.
- Optionally add a diversity or popularity re-ranking layer on top of the Exp3 similarity scores.
