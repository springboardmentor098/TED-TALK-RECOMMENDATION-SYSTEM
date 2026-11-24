# Task 7 — Understanding User Preferences and Preparing Interaction Data

**Notebook:** `notebooks/07_user_interaction_data.ipynb.ipynb`  
**Task:** 7 of 8  
**Status:** Complete

> The notebook file has a duplicated `.ipynb` extension in its name; the content is valid. Renaming it to `07_user_interaction_data.ipynb` would tidy the folder.

---

## 1. Objective

Build a simulated user–item interaction dataset, convert it into a user–item matrix, run basic interaction analysis, and explain how collaborative filtering turns those interactions into personalised recommendations.

---

## 2. Input

| File | Shape | Size |
|------|------:|-----:|
| `data/processed/ted_talks_cleaned.csv` | 4,005 × 16 | ~123 MB |

The cleaned dataset is used so that tags are already normalised.

---

## 3. Simulated Data Design

| Item | Value |
|------|-------|
| Users | 50 (`U001`–`U050`) |
| Talks sampled | 200 (deterministic, `random_state=42`) |
| Interaction model | Sparse ratings, 1–5 |
| Extra signals | `liked`, `saved`, `watch_pct` (0–1), `timestamp` |
| Seed | 42 (reproducible) |

> The interaction data is **simulated for learning purposes**. No real user data is used.

### How preferences are assigned

1. Each user gets **2–3 preferred tags** drawn from the 323 unique tags present in the 200 sampled talks.
2. For every (user, talk) pair, the probability of interacting grows with tag overlap:
   `p_watch = 0.10 + 0.25 × overlap`.
3. The rating is driven by the same overlap:
   `rating = clip(round(2.5 + 0.8 × overlap + N(0, 0.7)), 1, 5)`.
4. `liked = rating ≥ 4`.
5. `saved = True` when `rating = 5`, or `rating = 4` with 30% probability.
6. `watch_pct` is drawn from a normal distribution shifted upward by rating.
7. `timestamp` is random between 2023-01-01 and 2024-12-31.

This deliberately encodes a learnable signal: users rate talks in their preferred topics higher.

---

## 4. Output Dataset

| File | Rows | Users | Talks | Description |
|------|-----:|------:|------:|-------------|
| `data/interaction/user_interactions.csv` | 1,153 | 50 | 200 | Simulated explicit ratings with behaviour signals |

### Rating schema

`user_id`, `talk_id`, `rating`, `liked`, `saved`, `watch_pct`, `timestamp`

Example rows:

| user_id | talk_id | rating | liked | saved | watch_pct | timestamp |
|---------|--------:|-------:|:-----:|:-----:|----------:|-----------|
| U001 | 1307 | 4 | True | False | 0.57 | 2023-07-02 |
| U001 | 1075 | 3 | False | False | 0.62 | 2024-09-09 |
| U001 | 2030 | 2 | False | False | 0.80 | 2023-12-01 |

---

## 5. User–Item Interaction Matrix

| Metric | Value |
|--------|------:|
| Shape | 50 × 200 (users × talks) |
| Filled entries | 1,153 |
| Missing entries | 8,847 |
| Sparsity | **88.47%** |
| Min ratings per user | 12 |

- Rows = users, columns = talks, values = rating (1–5).
- A missing value (NaN) means the user **did not interact** with that talk — not that they disliked it.

---

## 6. Basic Interaction Analysis

### Q1–Q2: Unique users and talks

| Metric | Value |
|--------|------:|
| Unique users | 50 |
| Unique talks interacted with | 200 |

### Q3: Highest-rated talks (minimum 5 ratings)

| Rank | Talk ID | Title | Avg rating | Ratings |
|-----:|--------:|-------|-----------:|--------:|
| 1 | 2265 | the surprisingly logical minds of babies | 3.80 | 5 |
| 2 | 2700 | smelfies and other experiments in synthetic biology | 3.60 | 5 |
| 3 | 2707 | a burial practice that nourishes the planet | 3.50 | 6 |
| 4 | 386 | the story of ezra | 3.43 | 7 |
| 5 | 372 | design and the elastic mind | 3.38 | 8 |

### Q4: Most-active users

| Rank | User | Interactions |
|-----:|------|-------------:|
| 1 | U035 | 35 |
| 2 | U033 | 34 |
| 3 | U001 | 33 |
| 4 | U044 | 33 |
| 5 | U026 | 32 |

### Q5: Most-interacted talks

| Rank | Talk ID | Title | Interactions | Avg rating |
|-----:|--------:|-------|-------------:|-----------:|
| 1 | 1562 | the promise of research with stem cells | 14 | 2.36 |
| 2 | 1501 | the game that can give you 10 extra years of life | 13 | 2.69 |
| 3 | 190 | the anthropology of mobile phones | 12 | 2.33 |
| 4 | 230 | 5 predictions from 1984 | 11 | 2.91 |
| 5 | 1534 | a test for parkinson's with a phone call | 11 | 3.36 |

---

## 7. What a Missing Rating Means

A missing value in the user–item matrix means **no interaction**, not a negative rating. Possible reasons:

1. The talk was never shown or recommended.
2. The user saw it but chose not to watch or rate.
3. The user watched but did not rate (implicit interaction only).
4. The talk was not released yet.

Collaborative filtering must distinguish **explicit missing** (never seen) from **implicit negative** (seen and disliked). The simulated dataset captures only the explicit side: watched talks are rated.

---

## 8. How Collaborative Filtering Uses This Data

**Core idea:** if two users rate several talks similarly, they probably share interests. A talk liked by User A but unseen by User B is a good candidate for B.

- **User-based CF** — find users similar to the target, recommend talks they liked.
- **Item-based CF** — find talks similar to ones the target already liked, recommend those.

The interaction data supplies the three things CF needs:

| Signal | Role |
|--------|------|
| `user_id` | identifies who is who |
| `talk_id` | identifies what was interacted with |
| `rating` (1–5) | quantifies preference strength |

Sparsity (~88% empty) is the realistic scenario CF is designed for: predict the missing entries from a small set of observed ratings.

---

## 9. Key Observations

1. **Simulated but realistic** — tag-preference biases create a signal CF can learn.
2. **Sparse by design** — most of the 50 × 200 matrix is empty, mirroring real systems.
3. **Ratings are modest (≈2.5–3.5)** because low-overlap talks are still sometimes watched and rated low.
4. **Long-tail behaviour** — a few users and talks dominate interactions (popularity bias, cold-start risk).
5. **Missing ≠ dislike** — NaN means no interaction, which CF must not treat as a zero rating.
6. **Extensible** — `liked`, `saved`, and `watch_pct` allow a later move from explicit to implicit feedback.
7. **Next step** — Task 8 uses this matrix to compute user similarity and predict missing ratings.

---

## 10. Limitations

- The data is synthetic; results say nothing about real TED viewers.
- Only 50 users × 200 talks, so similarity estimates are noisy.
- Ratings are generated from tags, which makes them somewhat circular with the content-based model.
- `watch_pct` and timestamps are not yet used by the recommender.
- No negative feedback (explicit dislikes) exists.
- The `timestamp` range is fixed and does not model drift in user taste.

---

## 11. Next Step

Use `data/interaction/user_interactions.csv` in **Task 8** (`08_collaborative_filtering.ipynb`) to build a user-based collaborative filtering recommender.
