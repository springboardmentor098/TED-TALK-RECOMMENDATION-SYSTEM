# Personalized TED Talks Recommendation System Using Machine Learning

## Project Description

This project aims to recommend TED Talks to users based on talk titles, descriptions, topics, and transcripts using content-based recommendation techniques.

## Technologies Used

- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Jupyter Notebook
- Scikit-learn

## Dataset Information

- **Dataset Name:** TED Talks Transcripts for NLP
- **Source:** Kaggle
- **Original File:** `ted_talks_en.csv`
- **Total Records:** 4,005
- **Total Columns:** 19
- **Unique Talk IDs:** 4,005
- **Available Transcripts:** 4,005

## Project Structure

- `data/raw/` — Original dataset files.
- `data/processed/` — Processed dataset files created during the project.
- `notebooks/` — Jupyter notebooks for data exploration, preprocessing, and feature extraction.
- `requirements.txt` — Required Python packages.
- `README.md` — Project description and progress.

## Task 1: Environment Setup and Data Inspection

### Completed Activities

- Created a Python virtual environment.
- Installed the required Python libraries.
- Created the project folder structure.
- Downloaded and loaded the English TED Talks dataset.
- Inspected dataset dimensions, column names, and data types.
- Checked missing values and duplicate records.
- Verified that all 4,005 records contain non-empty transcripts.
- Prepared a Dataset Inspection Report.

## Task 2: Exploratory Data Analysis (EDA) and Data Quality Assessment

### Completed Activities

- Performed exploratory data analysis.
- Analyzed dataset dimensions and descriptive statistics.
- Examined missing values and duplicate records.
- Analyzed transcript word counts and text distribution.
- Visualized important dataset characteristics using Matplotlib and Seaborn.

## Task 3: Data Cleaning and Text Preprocessing

### Completed Activities

- Identified and handled missing values in relevant columns.
- Checked duplicate records and talk IDs.
- Applied text preprocessing techniques.
- Converted text to lowercase.
- Removed unnecessary punctuation and special characters.
- Performed tokenization and stopword removal.
- Prepared cleaned text data for feature extraction.

## Task 4: TF-IDF Vectorization

### Completed Activities

- Applied TF-IDF (Term Frequency-Inverse Document Frequency) vectorization.
- Converted textual data into numerical feature vectors.
- Explored text feature representation for content-based recommendation.
- Prepared the feature vectors for similarity-based recommendation.

## Dataset Quality Summary

- Total rows: 4,005
- Total columns: 19
- Duplicate rows: 0
- Duplicate talk IDs: 0
- Missing values exist in some optional metadata columns.
- No missing or empty transcripts were found in the original dataset.

## Project Progress

- Task 1: Environment Setup and Initial Dataset Inspection — Completed
- Task 2: Exploratory Data Analysis (EDA) and Data Quality Assessment — Completed
- Task 3: Data Cleaning and Text Preprocessing — Completed
- Task 4: TF-IDF Vectorization — Completed

## Future Work

- Calculate similarity between TED Talks using cosine similarity.
- Develop a personalized TED Talks recommendation function.
- Test the recommendation system with different input talks.
- Evaluate the recommendation results.
- Develop a user-friendly interface for the recommendation system.

## Note

The original dataset is preserved in `data/raw/`. Processed datasets and preprocessing decisions are maintained separately. The dataset licence should be verified before redistribution or public release.