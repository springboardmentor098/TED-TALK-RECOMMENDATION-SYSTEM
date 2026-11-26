# Task 9 - Building a Hybrid Recommendation Model

## Objective
Fuse the content-based (CB) recommender from Task 6 with the mean-centred collaborative filter from Task 8 into one hybrid that ranks talks by both topical similarity and user preference.

## Setup / Inputs
| Item | Value |
|---|---|
| Talks catalogue | 4,005 × 16 |
| CB artefacts | TF-IDF (4,005 × 23,643), cosine (4,005 × 4,005) |
| CF bundle | user–item (500 × 200), similarity (500 × 500), k = 20 |
| Interactions | 9,778 (90.22% sparse) |
| Default α | 0.5 |

## What was done
1. Loaded the Task 6 CB artefacts (Title + Description + Tags, Exp3) and `cf_model.joblib`.
2. For a given user and seed title, generated a CB top-N list and a mean-centred CF top-N list.
3. Removed talks the user had already rated from both lists **before** normalization.
4. Min-max scaled each remaining list to [0, 1].
5. Attached CF confidence as `cf_conf = min(n_raters / 5, 1)`, with 0 for talks outside the CF universe.
6. Scored `hybrid = α × cb_norm + (1 − α) × cf_norm × cf_conf`, merged duplicates, and ranked.

Three fixes were applied: **filter before min-max** (removing rated items afterwards would shift the endpoints), **confidence down-weighting** (one-neighbour predictions count less than five-neighbour ones), and **duplicate merging** (one combined score per talk).

## Results
Sample user U0001, seed talk "the dead zone of the gulf of mexico", α = 0.5:

| Rank | CB talk | CB score | CF talk | CF score (n) | Hybrid talk | Hybrid score |
|---:|---|---:|---|---:|---|---:|
| 1 | 14485 | 0.1408 | 912 | 3.6303 (1) | 14485 | 0.5000 |
| 2 | 1054 | 0.1285 | 10975 | 3.3198 (4) | 1054 | 0.3929 |
| 3 | 1499 | 0.1251 | 1534 | 3.3083 (1) | 1499 | 0.3632 |
| 4 | 940 | 0.1249 | 24347 | 3.3083 (1) | 940 | 0.3615 |
| 5 | 471 | 0.1176 | 201 | 3.3037 (1) | 471 | 0.2979 |

All five hybrid slots come from CB. CF's strongest talk (10975, four raters) does not reach the hybrid top 5: after min-max scaling and the `cf_conf = 0.8` discount, its contribution at α = 0.5 stays below the fifth CB score (0.2979).

| α | Top-1 talk (score) | Top-2 talk (score) | CF-origin talks in top-5 |
|---:|---|---|---:|
| 0.0 | 10975 (0.4305) | 613 (0.2119) | 5 |
| 0.3 | 10975 (0.3014) | 14485 (0.3000) | 1 |
| 0.5 | 14485 (0.5000) | 1054 (0.3929) | 0 |
| 0.7 | 14485 (0.7000) | 1054 (0.5500) | 0 |
| 1.0 | 14485 (1.0000) | 1054 (0.7857) | 0 |

Invalid users, unknown seeds (with a suggestion), and α outside [0, 1] all return explicit messages.

## Observations
- **CB dominates at α = 0.5.** Every hybrid slot is a CB talk; the highest-scoring CF item (10975) misses the cut once its confidence discount is applied.
- **Confidence weighting is decisive.** Four of U0001's five CF recommendations rest on a single neighbour (`cf_conf = 0.2`), so their normalized scores are heavily discounted; only 10975 has four raters (`cf_conf = 0.8`).
- **α shifts the list from CF toward CB.** At α = 0.3 one CF talk enters the top 5; from α = 0.5 onward the hybrid is CB-only, and α = 1.0 reproduces CB exactly.

## Limitations
- **Scale mismatch:** CB cosine scores and CF ratings differ in scale, so min-max fusion depends on list length and candidate set.
- **Heuristic confidence:** the five-rater cap is fixed, not calibrated against outcomes.
- **Thin CF evidence:** at 90.22% sparsity most predictions rest on one or two neighbours, so the hybrid mostly mirrors CB.
- **Single-seed CB:** the CB side uses one seed talk; Task 10 replaces it with a multi-talk profile.

## Deliverables produced
- `hybrid_recommend()` and the α-sensitivity comparison in `notebooks/09_hybrid_recommendation.ipynb`.
- No new artefact was written; the hybrid reuses the Task 6 CB matrices and the Task 8 `cf_model.joblib`.
