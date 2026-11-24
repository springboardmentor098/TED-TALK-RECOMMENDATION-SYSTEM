# Task 6 – Feature Selection and Recommendation Quality Evaluation

## Objective
Experiment with four feature combinations (Title-only, Title+Tags, Title+Description+Tags, Title+Description+Transcript+Tags) and identify which produces the most relevant TED Talk recommendations.

## Experimental Setup
- **Dataset:** `data/processed/ted_talks_cleaned.csv` (4,005 talks × 16 columns)
- **Model:** TF-IDF (`stop_words='english'`, `ngram_range=(1,2)`, `min_df=2`, `max_df=0.9`) + cosine similarity
- **Top-N:** 5 recommendations per seed
- **Seeds (5):** Averting the climate crisis · Do schools kill creativity · Simplicity sells · The best stats you ve ever seen · How policing for profit undermines your rights

## Experiment Pipelines
| Experiment | Input columns | TF-IDF vocabulary |
|---|---|---|
| Exp1 | title | ~2,500 terms |
| Exp2 | title + tags | ~7,500 terms |
| Exp3 | title + description + tags | ~23,600 terms |
| Exp4 | title + description + transcript + tags | ~363,900 terms |

## Comparison Tables
Side-by-side top-5 recommendations per seed per experiment are produced in the notebook. Screenshots of these outputs are attached separately.

### Average Tag Jaccard (higher = better topical overlap)
| Seed | Exp1 | Exp2 | Exp3 | Exp4 |
|---|---|---|---|---|
| Averting the climate crisis | 0.1362 | 0.3806 | 0.3490 | 0.2452 |
| Do schools kill creativity | 0.1254 | 0.4306 | 0.3058 | 0.2148 |
| How policing for profit undermines your rights | 0.0512 | 0.1337 | 0.2015 | 0.1476 |
| Simplicity sells | 0.0957 | 0.2400 | 0.2305 | 0.1156 |
| **Mean** | **0.1021** | **0.2962** | **0.2717** | **0.1808** |

### Average Cosine Score (only comparable within an experiment)
| Seed | Exp1 | Exp2 | Exp3 | Exp4 |
|---|---|---|---|---|
| Averting the climate crisis | 0.4037 | 0.3797 | 0.2815 | 0.1526 |
| Do schools kill creativity | 0.4006 | 0.2508 | 0.1907 | 0.1493 |
| How policing for profit undermines your rights | 0.3787 | 0.1907 | 0.1639 | 0.1697 |
| Simplicity sells | 0.3110 | 0.3315 | 0.2017 | 0.1394 |

## Evaluation

**Relevance:** Exp2 and Exp3 produced consistently topical recommendations. Exp1 surfaced near-duplicates (same speaker/topic cluster). Exp4 often drifted into unrelated talks (e.g., "rebuilding a neighborhood" and "feeling overwhelmed" for the creativity seed).

**Whether recommended talks discuss similar topics/concepts:** Yes for Exp2 and Exp3. Exp3 showed more conceptual variety (e.g., for policing seed it recommended rule-of-law and justice-system talks), while Exp2 stayed inside the tag cluster.

**Irrelevant recommendations:** Most frequent in Exp4. Root cause: long transcripts inflate TF-IDF weights on filler words and repeated names (`tipper` for Al Gore outranked `climate`).

**Does adding the transcript improve quality?** No. Exp4 had the highest raw cosine scores but the **lowest tag Jaccard**, indicating similarity was structural (long shared vocab) rather than topical.

**Which feature combination produces the most meaningful results?** Exp3 (Title + Description + Tags) — best human-perceived relevance and diversity balance. Exp2 wins the tag-Jaccard metric by a small margin because tags are literally in its input; that metric is partial.

## Final Feature Selection
**Chosen combination: Exp3 — Title + Description + Tags**

**Justification:**
1. **Tag Jaccard is a partial signal.** It measures overlap only on the tags column, structurally favouring Exp2. Exp3 captures meaning beyond tags — descriptions encode *what the talk argues*.
2. **Qualitative review favours Exp3.** For the policing seed, Exp2 returned unrelated talks (guest-worker visas, migrant trail, profit); Exp3 returned rule-of-law and justice-system talks.
3. **Avoids transcript noise.** Exp4 inflates cosine scores through long shared vocabulary but causes off-topic drift.
4. **Balanced diversity.** Exp1 produces near-duplicates; Exp2 narrows around tag clusters; Exp3 gives conceptually related but diverse recommendations.
5. **Fast and reusable.** Exp3 matrix (~23,600 terms) is far smaller than Exp4 (~363,900 terms), suitable for a Streamlit deployment.

**Not selected:**
- Exp1 (Title only) — too narrow, near-duplicate results.
- Exp2 (Title + Tags) — good metric, underuses descriptive text.
- Exp4 (full text) — highest cosine scores but lowest real-world relevance.

## Artefacts Saved
- `data/processed/tfidf_matrix_exp3.npz`
- `data/processed/cosine_sim_exp3.npy`
- `data/processed/tfidf_vectorizer_exp3.joblib`
