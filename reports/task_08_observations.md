# Task 8 — Building a Collaborative Filtering Recommendation Model

**Notebook:** `notebooks/08_collaborative_filtering.ipynb`  
**Task:** 8 of 8  
**Status:** Complete

---

## 1. Objective

Build a **user-based collaborative filtering** recommender that suggests TED Talks from similar users' rating patterns, then verify that it recommends unseen talks correctly and gives different users different results.

---

## 2. Inputs

| File | Shape | Size |
|------|------:|-----:|
| `data/interaction/user_interactions.csv` | 1,153 × 7 | ~50 KB |
| `data/processed/ted_talks_cleaned.csv` | 4,005 × 16 | ~123 MB |

Only `talk_id` and `title` are taken from the cleaned dataset, for display.

> The interactions were simulated in Task 7. No real user data is used.

---

## 3. Method

1. Load interactions and pivot into the user–item matrix.
2. Fill missing ratings with **0** for cosine similarity — 0 means "not rated", not "rated 0".
3. Compute **user–user cosine similarity**.
4. For a target user, take the **top-K most similar users** (default `K = 10`).
5. Predict a score for each talk the target has **not** rated, using a similarity-weighted average of the neighbours' ratings:

$$\hat{r}_{u,i} = \frac{\sum_{v \in N} \text{sim}(u,v) \cdot r_{v,i}}{\sum_{v \in N} |\text{sim}(u,v)|}$$

where *N* is the set of neighbours who actually rated talk *i*.

6. Sort by predicted score and return the **top-N** (default 5).

### Prediction details

- Self-similarity is zeroed (`np.fill_diagonal(..., 0.0)`).
- Talks the target has already rated are excluded.
- Ties are broken by the number of neighbours who rated the talk (`n_raters`), making results deterministic.
- `top_n` is validated to be an integer between 1 and 20; invalid users and cold-start users return `None` with a message.

### Function signature

```python
recommend_for_user(user_id, top_n=5, k_neighbors=10)
```

Returns a DataFrame with `Rank`, `talk_id`, `title`, and `Predicted Score`.

---

## 4. User–Item Matrix

| Metric | Value |
|--------|------:|
| Shape | 50 × 200 (users × talks) |
| Filled entries | 1,153 |
| Missing entries | 8,847 |
| Sparsity | 88.47% |
| Rating range | 1–5 |

---

## 5. User Similarity Results

| Metric | Value |
|--------|------:|
| Similarity matrix shape | 50 × 50 |
| Similarity range | 0.0000 – 0.3343 |
| Average pairwise similarity | 0.1079 |

Similarities are low because the matrix is 88.47% sparse — two users rarely rate the same talks. This is the central constraint on CF quality here: predictions rest on a handful of co-rated items.

### Top 10 users most similar to U001

| Rank | User | Similarity |
|-----:|------|-----------:|
| 1 | U040 | 0.2738 |
| 2 | U008 | 0.2652 |
| 3 | U048 | 0.2518 |
| 4 | U041 | 0.2462 |
| 5 | U039 | 0.2328 |
| 6 | U009 | 0.2308 |
| 7 | U007 | 0.2216 |
| 8 | U030 | 0.2066 |
| 9 | U003 | 0.1979 |
| 10 | U026 | 0.1968 |

---

## 6. Recommendation Results

### U001

| Rank | Talk ID | Title | Predicted Score |
|-----:|--------:|-------|----------------:|
| 1 | 386 | the story of ezra | 4.0 |
| 2 | 27 | organic design inspired by nature | 4.0 |
| 3 | 2368 | forget wi fi meet the new li fi internet | 4.0 |
| 4 | 2883 | lessons from the longest study on human development | 4.0 |
| 5 | 32269 | the uncomplicated truth about women s sexuality | 4.0 |

All five score 4.0 because the neighbours gave these talks identical ratings; the `n_raters` tiebreaker orders them deterministically.

### U006

| Rank | Talk ID | Title | Predicted Score |
|-----:|--------:|-------|----------------:|
| 1 | 2265 | the surprisingly logical minds of babies | 5.0 |
| 2 | 27 | organic design inspired by nature | 4.0 |
| 3 | 246 | inventing instruments that unlock new music | 4.0 |
| 4 | 1656 | a new kind of job market | 4.0 |
| 5 | 1993 | comics that ask what if | 4.0 |

### U042

| Rank | Talk ID | Title | Predicted Score |
|-----:|--------:|-------|----------------:|
| 1 | 1140 | the hidden beauty of pollination | 4.5193 |
| 2 | 246 | inventing instruments that unlock new music | 4.0 |
| 3 | 359 | the blur building and other tech empowered architecture | 4.0 |
| 4 | 675 | compassion at the dinner table | 4.0 |
| 5 | 1800 | the voices in my head | 4.0 |

### Invalid user

`recommend_for_user("U999")` prints `Invalid user_id: 'U999'. Not found in the interaction dataset.` and returns `None`.

---

## 7. Verification

| Check | U001 | U006 | U042 |
|-------|:----:|:----:|:----:|
| Already-rated talks excluded | ✔ (0) | ✔ (0) | ✔ (0) |
| Sorted by predicted score | ✔ | ✔ | ✔ |
| Returns exactly `top_n` rows | ✔ (5) | ✔ (5) | ✔ (5) |

**Different users get different results:** U001 and U006 share only **1 of 5** recommendations (talk 27), a popular talk that appears across many neighbourhoods.

- U001 → `[386, 27, 2368, 2883, 32269]`
- U006 → `[2265, 27, 246, 1656, 1993]`

---

## 8. Required Questions

**1. What is collaborative filtering?**  
A technique that predicts a user's preferences from the behaviour of similar users, without analysing item content — "users like you liked X, so you might too."

**2. How is it different from content-based filtering?**

| Aspect | Content-based | Collaborative |
|--------|---------------|---------------|
| Uses | Item features (title, tags, transcript) | User–item interactions |
| Asks | "What is this talk about?" | "Who else liked this talk?" |
| New item | Works (features exist) | Fails (no ratings — cold item) |
| New user | Works with a seed item | Fails (no history — cold user) |

**3. What is a user–item interaction matrix?**  
A 2-D table: rows = users, columns = talks, values = ratings. A missing value means the user did not rate that talk.

**4. Why calculate similarity between users?**  
To find users whose rating patterns match the target, then use their ratings to predict scores for unseen talks.

**5. What does cosine similarity represent here?**  
The angle between two users' rating vectors, from 0 (no shared behaviour) to 1 (identical patterns). With zero-filled missing values, only co-rated talks contribute meaningfully.

**6. Why exclude talks the user already rated?**  
Recommending something already seen is useless; CF should surface new items.

**7. What is a predicted rating?**  
An estimate of how the target would rate a talk, computed as the similarity-weighted average of their top-K neighbours' ratings.

**8. What happens for a new user with no history?**  
The function returns `None` with a cold-start message — there is no data to compute similarity or predictions.

**9. What is the cold-start problem?**  
The inability to recommend well for new users (no history) or new items (no ratings). Mitigations: onboarding preferences, popularity fallback, or content-based/hybrid features.

**10. What are the limitations of user-based CF?**  
Cold start, sparsity, O(users²) scalability, popularity bias, shilling/manipulation, stale tastes over time, and information loss from zero-filling.

---

## 9. Output

**No files are written.** The recommender function and all test outputs live in the notebook.

---

## 10. Observations and Limitations

- **Similar users are found** via cosine similarity on zero-filled rating vectors.
- **Predictions use only the top-K neighbours** (default 10) and only talks the target has not rated.
- **Users receive different lists** — U001 and U006 overlap on just one talk.
- **Preferences propagate** — a user with strong overlap with a neighbour inherits that neighbour's tastes; sparse overlaps give noisier predictions.
- **Observed limitations:**
  - **Cold start** — users with zero ratings cannot receive CF recommendations.
  - **Sparsity** — at 88.47% missing, most user pairs share very few co-rated talks.
  - **Zero-fill approximation** — treating NaN as 0 lowers similarity even when the few shared ratings agree.
  - **Popularity bias** — widely rated talks appear in predictions simply because they have data.
  - **No item features** — two very different talks with similar rating patterns look identical to the model.
  - **Tie-heavy scores** — with few neighbours, many predictions collapse to the same value (e.g. 4.0), so the tiebreaker does most of the ranking.

---

## 11. Next Step

Combine this CF model with the content-based recommender from Task 6 into a **hybrid** system: CF supplies personalisation, while content-based similarity handles cold-start users/items and semantic diversity.
