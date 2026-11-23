# Dataset Review — `ted_talks_merged.csv`

## Inspection results

- Shape: 2,550 rows × 18 columns.
- Columns: `comments`, `description`, `duration`, `event`, `film_date`, `languages`, `main_speaker`, `name`, `num_speaker`, `published_date`, `ratings`, `related_talks`, `speaker_occupation`, `tags`, `title`, `url`, `views`, `transcript`.
- Missing `transcript`: 86 rows.
- Missing `speaker_occupation`: 6 rows.
- Other listed columns: no missing values in the supplied CSV.
- Exact duplicate rows: 0.
- Duplicate `url`: 0.
- Duplicate `name`: 0.
- Duplicate `title`: 0.
- The `ratings` field contains aggregate TED reaction categories/counts, not individual user-to-talk ratings.
- No original `id` or `talk_id` field. Task 3 derives `talk_id` from unique `name`, with `url` as a fallback.
- Tags are represented as text strings containing Python-style lists. Task 2 and Task 3 parse them with `ast.literal_eval`, not `eval`.

## Is the dataset suitable?

Yes, it is suitable for a first content-based recommendation prototype: it contains 2,550 distinct talks and provides titles, descriptions, tags, URLs and transcripts for most talks. The 86 missing transcripts do not require dropping records because the other text fields remain available.

## Limitations and checks still needed

1. The CSV does not document its upstream source or licence. Verify both before redistribution.
2. There is no original numeric talk identifier; a slug-based `talk_id` is derived.
3. There are no real user ratings or watch events. Task 7's user interactions are simulated for learning only.
4. The recommendation system is initially word-based TF-IDF; semantic relevance needs human review or a labelled evaluation dataset.
5. Views, ratings, and related-talks metadata are present as fields, but this project does not claim those represent user-level interaction histories.
