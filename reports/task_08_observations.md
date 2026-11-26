# Task 8 - Building a Collaborative Filtering Recommendation Model

## Objective
Build a user-based collaborative filtering (CF) recommender that predicts TED Talk ratings from similar users' rating patterns, then persist the fitted model for Tasks 9 and 10.

## Setup / Inputs
| Item | Value |
|---|---|
| Interactions | `data/interaction/user_interactions.csv` - 9,778 rows |
| Users × talks | 500 × 200 |
| Matrix fill | 9,778 of 100,000 cells (90.22% sparse) |
| Rating scale | 1–5 |
| Neighbours (K) | 20 |
| Titles | `data/processed/ted_talks_cleaned.csv` |

The interaction data is simulated (Task 7); no real user behaviour is used.

## What was done
1. Built the 500 × 200 user–item matrix (NaN = unrated).
2. Computed per-user means over rated talks (2.10–3.23, median 2.67).
3. Mean-centred as `rating − user_mean`, filling gaps with 0 ("this user's average").
4. Computed cosine similarity on the centred vectors, giving 500 × 500.
5. `recommend_for_user()`: 20 neighbours, `dev̂ = Σ sim·(r − r̄) / Σ|sim|`, `r̂ = clip(r̄_u + dev̂, 1, 5)`, ties broken by `n_raters`.
6. Tested three users plus an invalid ID, ran checks, and saved the bundle.

## Results

| Similarity property | Value |
|---|---|
| Matrix shape | 500 × 500 |
| Range | −0.5958 to 0.4730 |
| Mean pairwise similarity | 0.0006 |
| Positive / negative pairs | 41.9% / 41.5% |
| Pairs sharing ≥1 co-rated talk | 84.8% (up to 13) |

Top-5 recommendations, shown as talk ID (predicted score):

| Rank | U0001 | U0002 | U0003 |
|---:|---|---|---|
| 1 | 912 (3.6303) | 91 (4.7186) | 42461 (4.6234) |
| 2 | 10975 (3.3198) | 32250 (4.2102) | 55793 (3.8643) |
| 3 | 1534 (3.3083) | 1773 (4.0365) | 1656 (3.8262) |
| 4 | 24347 (3.3083) | 2707 (4.0086) | 2508 (3.7964) |
| 5 | 201 (3.3037) | 1077 (3.9939) | 27155 (3.7249) |

Verification results:

| Verification check | U0001 | U0002 | U0003 |
|---|---|---|---|
| Already-rated talks returned | 0 | 0 | 0 |
| Sorted by predicted score | Yes | Yes | Yes |
| Rows returned (requested 5) | 5 | 5 | 5 |

U0001 and U0002 share 0 of 5 recommendations; an unknown ID returns a validation message, not a list. The ten required questions are condensed below.

| # | Question | Answer |
|---:|---|---|
| 1 | CF definition | Predictions from similar users' behaviour |
| 2 | Versus content-based | Interactions, not item features |
| 3 | User–item matrix | Users × talks, ratings, NaN = unrated |
| 4 | Why user similarity | Neighbours inform predictions |
| 5 | Cosine meaning | Relative-preference agreement after mean removal |
| 6 | Exclude rated talks | Seen items are useless |
| 7 | Predicted rating | Weighted deviation plus target mean, clipped |
| 8 | New user | Error/None - cold start |
| 9 | Cold start | No user history; no item ratings |
| 10 | CF limits | Cold start, sparsity, O(users²), popularity, manipulation |

## Observations
- **Mean-centering removes baseline bias.** Raw ratings cluster near 2.5–3.2, so generous and harsh raters would look dissimilar; centring compares each user with their own norm. U0001's top score is 3.63, while the next three (3.31–3.32) are separated by `n_raters`.
- **Similarity is signed.** The mean is 0.0006 because centred vectors sum to zero, with 41.9% positive and 41.5% negative pairs.
- **Every user has a neighbourhood.** 84.8% of pairs share a co-rated talk, so all 500 users receive five recommendations despite 90.22% sparsity.
- **Output is personalised.** U0001 and U0002 share no recommendations, and all scores are clipped to [1, 5] (maximum 4.72 for U0002).

## Limitations
- **Cold start:** users without ratings cannot be scored; the function errors.
- **Sparsity noise:** thin overlap makes similarity unstable, and 41.5% of pairs are negative.
- **Popularity and opacity:** frequent talks dominate, and choices cannot be explained.
- **No item features:** similar rating patterns hide content differences.

## Deliverables produced
- `data/processed/cf_model.joblib` - `user_item` (500 × 200), `user_means` (500,), `sim_df` (500 × 500), `k = 20`.
