# Task 10 - Model Evaluation and Optimization

## Objective
Evaluate the content-based (CB), collaborative (CF) and hybrid recommenders on held-out Precision@K, Recall@K and NDCG@K, then select the final model.

## Setup / Inputs
| Item | Value |
|---|---|
| Catalogue | 4,005 talks |
| Interactions | 9,778 ratings from 500 users |
| Candidate universe | 200 interacted talks |
| Split | 30% of each user's ratings held out |
| Relevance | rating ≥ 3 |
| Metrics | P@K, R@K, NDCG@K for K = 5 and 10 |
| α grid | 0.0, 0.3, 0.5, 0.7, 1.0 |

The split yields 7,059 training and 2,719 test interactions; 489 of 500 users are evaluable, averaging 3.30 relevant held-out talks.

## What was done
1. Held out 30% of each user's ratings (seeded), requiring at least one relevant test item.
2. **CB:** averaged TF-IDF vectors of training talks rated ≥ 4 (fallback: top-rated) into a profile and scored the 200-talk universe. The model is unchanged from Tasks 5/6; only the query moved from one seed talk to a multi-talk profile.
3. **CF:** recomputed user means and mean-centred similarity on the training matrix only, clipping predictions to [1, 5].
4. **Hybrid:** min-max fused CB with confidence-weighted CF across the α grid.
5. Counted a hit when a recommendation appeared in the held-out relevant set and averaged each metric across users.

**Matched universe.** CF can only rank talks present in the interaction matrix, so CB was restricted to the same 200 talks. The appendix runs unrestricted CB over all 4,005 talks: P@5 falls from 0.0397 to 0.0020, roughly 20× lower. That gap reflects a 20× larger candidate pool, not worse content modelling.

## Results

| Model | P@5 | R@5 | NDCG@5 | P@10 | R@10 | NDCG@10 |
|---|---:|---:|---:|---:|---:|---:|
| CB (α = 1.0) | 0.0397 | 0.0581 | 0.0476 | 0.0352 | 0.0986 | 0.0660 |
| CF (α = 0.0) | 0.0196 | 0.0309 | 0.0285 | 0.0196 | 0.0650 | 0.0426 |
| Hybrid (α = 0.5) | 0.0380 | 0.0588 | 0.0473 | 0.0335 | 0.0957 | 0.0642 |

The hybrid α sweep across 489 evaluable users:

| α | P@5 | R@5 | NDCG@5 | P@10 | R@10 | NDCG@10 |
|---:|---:|---:|---:|---:|---:|---:|
| 0.0 | 0.0196 | 0.0309 | 0.0285 | 0.0196 | 0.0650 | 0.0426 |
| 0.3 | 0.0352 | 0.0530 | 0.0439 | 0.0327 | 0.0990 | 0.0635 |
| 0.5 | 0.0380 | 0.0588 | 0.0473 | 0.0335 | 0.0957 | 0.0642 |
| 0.7 | 0.0372 | 0.0547 | 0.0455 | 0.0354 | 0.1006 | 0.0664 |
| 1.0 | 0.0397 | 0.0581 | 0.0476 | 0.0352 | 0.0986 | 0.0660 |

The α sweep peaks at **α = 1.0** (CB), with P@5 rising 0.0196 -> 0.0352 -> 0.0380 -> 0.0372 -> 0.0397. Random top-5 from the 200-talk pool would score about 0.017, so CB is roughly 2.3× random while CF sits just above it.

| Model | Strengths | Weaknesses |
|---|---|---|
| CB | Explainable; no item cold start; best P@5/NDCG@5 | Ignores other users; low diversity |
| CF | Models user preference; centring removes scale bias | Cold start; noisy at 90% sparsity; opaque |
| Hybrid | Balances relevance and personalisation; confidence weighting | Best α collapses to CB; needs tuning; two models |

## Observations
- **CB wins on the primary metrics.** It leads P@5 (0.0397), NDCG@5 (0.0476) and NDCG@10 (0.0660); CF trails at 0.0196 / 0.0285 / 0.0426.
- **The hybrid never beats CB.** At α = 0.5 it nearly matches (P@5 0.0380, NDCG@5 0.0473) and has marginally higher R@5 (0.0588 vs 0.0581), but its best α is 1.0, where it *is* CB.
- **Recall rises with K.** CB's R@5 of 0.0581 becomes 0.0986 at K = 10.
- **Candidate-universe control matters.** The appendix's 0.0020 versus 0.0397 shows that an unrestricted CB pool manufactures a 20× penalty unrelated to ranking quality.
- **No tuning forced a hybrid win.** The α sweep selects CB at 1.0 without adjusting thresholds, and CF adds no measurable value at this density.

## Limitations
- **Sparsity:** 90.22% of the matrix is missing, so CF neighbourhoods remain noisy.
- **Small holdout:** about six held-out items per user (3.30 relevant) make P/R sensitive to individual hits.
- **Fixed thresholds:** relevance is `rating ≥ 3` (58% of interactions) and the CB profile uses `rating ≥ 4`; changing either would move every metric.
- **Simulated data:** ratings come from tag overlap, not real preference; no user is cold-start.

## Deliverables produced
Final configuration:

```
Selected model:  CB (α = 1.0)
Best alpha:      1.0
Evaluable users: 489 / 500
Holdout:         30% per user
Relevance:       rating >= 3
K values:        5 and 10
P@5 / R@5 / NDCG@5: 0.0397 / 0.0581 / 0.0476
```

- Comparison, α-sweep, appendix and configuration outputs in `notebooks/10_model_evaluation.ipynb`.
- No new model file; evaluation reuses the Task 6 CB artefacts and Task 8 `cf_model.joblib`.
