# Task 3: Data Cleaning and Text Preprocessing

**Project:** Personalized TED Talks Recommendation System Using Machine Learning

## 1. Objective

The objective of this task was to clean the TED Talks dataset, handle empty text values, remove exact duplicate records, normalize text fields, and create a combined text column for the recommendation system.

## 2. Dataset Details

- Original dataset: `ted_talks_en.csv`
- Original rows: 4005
- Original columns: 19
- Cleaned dataset: `ted_talks_cleaned.csv`
- Cleaned rows: 4005
- Cleaned columns: 20

## 3. Data Cleaning Steps

1. Loaded the original dataset from the raw data folder.
2. Checked missing values in the dataset.
3. Converted empty or whitespace-only values in the selected text columns into missing values.
4. Checked for exact duplicate rows.
5. Removed exact duplicate rows, if any.
6. Converted text in the available title, topics, description, and transcript columns to lowercase.
7. Removed leading and trailing spaces and replaced repeated whitespace with a single space.
8. Preserved the original dataset without overwriting it.
9. Created a `combined_text` column by joining the available text fields.
10. Saved the cleaned dataset in `data/processed/ted_talks_cleaned.csv`.

## 4. Duplicate Analysis

- Exact duplicate rows before removal: 0
- Exact duplicate rows removed: 0
- Rows after duplicate removal: 4005

No exact duplicate rows were found. Repeated talk IDs and URLs should be assessed separately if those columns are available.

## 5. Missing Value Handling

Empty or whitespace-only values in the selected text columns were converted to missing values. Missing values were handled when creating `combined_text` by treating them as empty strings.

No rows were deleted solely because a text field was missing. Missing values in other dataset columns were not automatically removed.

## 6. Text Preprocessing

The following fields were cleaned when available:

- `title`
- `topics`
- `description`
- `transcript`

Text was converted to lowercase, unnecessary whitespace was removed, and missing values were preserved until combined text was created.

## 7. Combined Text Creation

A new column named `combined_text` was created by combining the available title, topics, description, and transcript fields. This column can be used later for text vectorization and similarity-based TED Talk recommendations.

## 8. Output

The processed dataset was saved to:

`data/processed/ted_talks_cleaned.csv`

The saved CSV was reopened and verified. It contained 4005 rows and 20 columns, including `combined_text`.

## 9. Limitations and Future Work

- Punctuation was preserved to avoid losing meaningful text.
- Stopword removal and tokenization were not performed in this stage.
- Repeated IDs and URLs require separate verification.
- Missing values in non-text columns may still exist.
- Further preprocessing and text vectorization can be performed in later stages.

## 10. Conclusion

The TED Talks dataset was prepared for the next stage of the recommendation system. The original data was preserved, exact duplicate rows were checked, selected text fields were normalized, and the processed dataset was saved successfully.
