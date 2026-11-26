# Task 7 - Understanding User Preferences and Preparing Interaction Data

## Objective
Build a simulated user–item interaction dataset for 500 users across 200 sampled TED Talks, convert it into a user–item matrix, and analyse the dataset's basic properties.

## Setup / Inputs
- Source catalogue: `data/processed/ted_talks_cleaned.csv` (4,005 talks).
- Deterministic sample of 200 talks (`random_state=42`), containing 323 unique tags.
- 500 users (`U0001`–`U0500`), each assigned 2–3 preferred tags.
- Rating scale: 1–5; target density ~10%.
- Stored signals: `rating`, `liked`, `saved`, `watch_pct`, `timestamp`.

## What was done
1. Sampled 200 talks and parsed their comma-separated tags into lists.
2. Assigned each user 2–3 preferred tags at random.
3. For every user–talk pair, sampled an interaction with `p_watch = 0.08 + 0.30 × tag_overlap`.
4. Generated a rating as `clip(2.5 + 0.8 × overlap + N(0, 0.7), 1, 5)`.
5. Derived `liked = rating ≥ 4`; `saved = rating == 5`, or `rating == 4` with 30% probability.
6. Derived `watch_pct = clip(N(0.2 + 0.15 × rating, 0.15), 0, 1)`.
7. Assigned timestamps uniformly across 2023-01-01 to 2024-12-31.
8. Saved the interaction CSV and pivoted it into a 500 × 200 user–item matrix.

## Results

| Metric | Value |
|---|---|
| Total interactions | 9,778 |
| Unique users | 500 |
| Unique talks | 200 |
| Matrix shape | 500 × 200 |
| Non-null entries | 9,778 |
| Missing entries | 90,222 |
| Sparsity | 90.22% |
| Min ratings per user | 7 |
| Median ratings per user | 19 |
| Missing user IDs | 0 |

The six analysis questions were answered from the executed notebook:

| # | Analysis question | Answer from the notebook |
|---|---|---|
| Q1 | Unique users | 500 |
| Q2 | Unique talks interacted with | 200 |
| Q3 | Top-rated talks (min 5 ratings) | 1534 (3.018, n=55); 1562 (3.015, n=68); 29265 (2.984, n=61); 372 (2.974, n=38); 2030 (2.957, n=46) |
| Q4 | Most-active users | U0168 (36); U0013 (35); U0035 (34); U0135 (34); U0492 (33) |
| Q5 | Most-interacted talks | 2625 (79); 1501 (73); 1826 (72); 2589 (71); 1993 (69) |
| Q6 | Meaning of a missing rating | No interaction occurred; it is not a negative rating |

## Observations
- **Tag bias concentrates the data.** Both interaction probability and rating rise with tag overlap, so users mostly see talks in their preferred topics. Even the highest-rated talks average only ~3.02, so the rating scale stays compressed toward the middle.
- **Sparsity is realistic.** Each user rates ~20 of 200 talks (median 19), leaving 90.22% of the matrix empty - a regime where collaborative filtering still has co-rating overlap to exploit.
- **Missing ≠ dislike.** A NaN means the user never saw the talk, not that they rated it low; CF must treat unobserved pairs differently from negative feedback.
- **Coverage is complete.** All 500 users and all 200 talks appear (0 missing user IDs; minimum 7 ratings per user), so there are no zero-history users or orphan talks.
- **Popularity and quality diverge.** The most-interacted talk (2625, 79 ratings) averages 2.84, while the top-rated talk (1534) has 55 ratings and averages 3.02.
- **The design supports CF.** Task 8 finds that 84.8% of user pairs share at least one co-rated talk, so neighbourhoods are available for every user.

## Limitations
- The data is simulated; no real user behaviour is represented.
- Tag overlap is the only preference driver - no explicit dislike, temporal drift, or social signal.
- The 2.5 rating base compresses ratings toward the middle, narrowing the "relevant" band.
- `watch_pct` is synthetic and correlated with rating by construction, not observed viewing behaviour.

## Deliverables produced
- `data/interaction/user_interactions.csv` - 9,778 rows.
