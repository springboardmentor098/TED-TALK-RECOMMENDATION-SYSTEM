# AI Personalized TED Talks Recommendation System

A content-based recommendation system that identifies TED Talks with similar textual content. The project uses Python, Pandas, Natural Language Processing (NLP), TF-IDF vectorization, and cosine similarity to represent and compare TED Talks.

## Project Overview

TED offers talks on a wide range of subjects. Finding talks related to a particular topic or an already-viewed talk can be easier with a recommendation system. This project explores a content-based approach: it analyzes the text associated with each talk and ranks other talks according to textual similarity.

The current implementation uses the talk title, topics, description, and transcript to create a combined text representation. TF-IDF converts this text into numerical feature vectors, and cosine similarity compares those vectors. The system then returns the most similar talks while excluding the selected talk itself.

> **Project scope:** The current recommendation approach is based on talk content. It does not yet model individual user preferences, viewing history, or feedback.

## Objectives

- Collect and inspect a TED Talks dataset.
- Explore data structure, quality, text characteristics, and topic distribution.
- Clean and preprocess text fields while retaining useful original information.
- Combine relevant text fields into a single representation for each talk.
- Convert talk text into numerical features using TF-IDF.
- Compare talks using cosine similarity.
- Generate and manually review sample recommendations.
- Document the limitations of a TF-IDF-based content recommendation approach.

## Technology Stack

- **Language:** Python
- **Development environment:** Visual Studio Code and Jupyter Notebook
- **Data handling:** Pandas, NumPy
- **Visualization:** Matplotlib, Seaborn
- **NLP and text processing:** NLTK
- **Feature extraction:** Scikit-learn (`TfidfVectorizer`)
- **Similarity measurement:** Scikit-learn (`cosine_similarity`)

The exact installed package versions are maintained in `requirements.txt`.

## Dataset

The project uses the TED Talks dataset collected from Kaggle. The working dataset contains 4,005 talk records.

The following fields were selected for the project:

| Column | Purpose |
|---|---|
| `talk_id` | Unique identifier for a TED Talk. |
| `title` | Talk title, used to identify and display a recommendation. |
| `speaker_1` | Primary speaker's name. |
| `duration` | Talk duration; may support future filtering by available time. |
| `topics` | Topics associated with the talk; useful for content matching. |
| `url` | Link to the original TED Talk. |
| `description` | Short description that provides contextual information about the talk. |
| `transcript` | Talk transcript, providing detailed text for NLP-based comparison. |

The original dataset is kept separately from the processed output. The selected fields and their cleaned counterparts are used during preprocessing.

## Project Structure

The repository is organized as follows. The `data` directory contains the raw and processed datasets, while the `notebooks` directory contains the notebooks for each project task.

```text
TED-TALK-RECOMMENDATION-SYSTEM/
│
├── data/
│   ├── raw/
│   │   └── ted_talks.csv
│   └── processed/
│       ├── ted_talks_eda.csv
│       ├── ted_talks_quality_checked.csv
│       └── ted_talks_cleaned.csv
│
├── notebooks/
│   ├── 01_data_exploration.ipynb
│   ├── 02_EDA_data_quality.ipynb
│   ├── 03_data_cleaning.ipynb
│   └── 04_tfidf_vectorization.ipynb
│
├── venv/                  # Local Python environment; not required in version control
├── .vscode/               # Editor configuration, if applicable
├── .gitignore
├── requirements.txt
└── README.md
```

> The processed CSV files are generated during the workflow. If a particular intermediate file is not present in your local checkout, it will be created when its corresponding notebook step is run. Do not commit large generated datasets unless the project repository specifically requires them.

## Environment Setup

The project has been developed on Windows using VS Code, Jupyter Notebook, and a Python 3.11 Conda environment located in the project folder as `venv/`.

### 1. Clone or open the repository

Open the repository folder in VS Code and open a terminal at the repository root.

### 2. Create and activate the environment

If the environment has not already been created, run:

```bash
conda create -p venv python=3.11 -y
```

Activate it:

```bash
conda activate venv/
```

### 3. Install project dependencies

```bash
python -m pip install -r requirements.txt
```

If you are setting up the environment for the first time and `requirements.txt` is not yet available or does not include a required package, install the missing dependency and update the file accordingly.

### 4. Launch Jupyter Notebook

From the repository root, run:

```bash
python -m jupyter notebook
```

Open the required notebook from the `notebooks/` directory. Ensure that the notebook is using the project's Python 3.11 environment.

## Project Workflow and Tasks

### Task 1 — Environment Setup and TED Talks Dataset Collection

**Objective:** Prepare the development environment, collect the dataset, and perform an initial inspection before analysis.

**Work completed:**

1. Set up the project using Python, VS Code, and Jupyter Notebook.
2. Prepared the project directories for raw data, processed data, and notebooks.
3. Collected the TED Talks dataset from Kaggle and stored the original file in `data/raw/ted_talks.csv`.
4. Selected the fields required for recommendation: `talk_id`, `title`, `speaker_1`, `duration`, `topics`, `url`, `description`, and `transcript`.
5. Performed an initial inspection of the dataset, including its dimensions, columns, data types, missing values, duplicate records, and talk identifiers.

**Notebook:** `notebooks/01_data_exploration.ipynb`

### Task 2 — Exploratory Data Analysis (EDA) and Data Quality Assessment

**Objective:** Understand the dataset's structure and quality, explore text characteristics and topic distribution, and identify issues to consider during cleaning.

**Activities:**

1. **Dataset summary:** Examine the number of records and columns, column names, data types, descriptive statistics, and unique talk identifiers.
2. **Missing values and duplicates:** Calculate missing-value counts and percentages, identify duplicate rows or repeated identifiers, and inspect missing or empty values in important fields such as titles, descriptions, topics, transcripts, and URLs.
3. **Text analysis:** Examine description and transcript lengths, calculate word counts, identify empty or unusually short text, and visualize transcript-length distributions where applicable.
4. **Topic analysis:** Identify frequently occurring TED Talk topics, visualize the most common topics, and inspect how topic values are stored and processed.
5. **Additional data analysis:** Explore fields such as duration or views if they are available in the dataset. Record relevant statistics, visualizations, and observations. An analysis is only applicable when the corresponding field exists.

**Notebook:** `notebooks/02_EDA_data_quality.ipynb`

**Output:** EDA and data-quality intermediate files are stored in `data/processed/`, including `ted_talks_eda.csv` and `ted_talks_quality_checked.csv`.

### Task 3 — Data Cleaning and Text Preprocessing

**Objective:** Prepare consistent text data for feature extraction while preserving the original dataset and useful source columns.

**Activities:**

1. **Load and review:** Load the raw dataset and use the findings from Task 2 to identify fields requiring attention.
2. **Handle missing values:** Inspect missing and empty values in important fields and handle them according to their purpose. A missing transcript does not automatically make a talk unusable if other useful text is available.
3. **Check duplicates:** Identify exact duplicate rows and inspect repeated talk identifiers or URLs before deciding whether records should be removed.
4. **Clean text fields:** Create cleaned versions of relevant text fields. Preprocessing includes appropriate lowercasing, whitespace normalization, handling of empty or missing text, and suitable HTML/text cleanup without removing meaningful content.
5. **Create combined text:** Build `combined_text` by combining the cleaned title, topics, description, and transcript. This provides a single text field for content-based feature extraction.
6. **Save the cleaned data:** Export the resulting dataset to `data/processed/ted_talks_cleaned.csv` without overwriting the raw source file.

The cleaned dataset retains the original fields alongside cleaned text columns, making it possible to use processed text for analysis while displaying readable original titles and speaker names in recommendation results.

**Notebook:** `notebooks/03_data_cleaning.ipynb`

**Output:** `data/processed/ted_talks_cleaned.csv`

### Task 4 — Text Vectorization Using TF-IDF and Similarity Analysis

**Objective:** Convert the cleaned text into numerical features, compare TED Talks using cosine similarity, generate sample recommendations, and examine the strengths and limitations of the approach.

**Activity 1 — Review the cleaned dataset**

- Load `data/processed/ted_talks_cleaned.csv`.
- Inspect the available columns and confirm that the required text fields are present.
- Check the number of usable talk records.

**Activity 2 — Implement TF-IDF vectorization**

- Preprocess the `combined_text` content for vectorization, including tokenization, stop-word removal, and stemming as implemented in the notebook.
- Use Scikit-learn's `TfidfVectorizer` to convert the processed talk text into a TF-IDF feature matrix.
- Inspect the vocabulary and matrix dimensions and understand that rows represent talks, columns represent vocabulary features, and values represent TF-IDF weights.

**Recorded result:** The TF-IDF matrix has a shape of **(4,005, 10,000)**, representing 4,005 talks and 10,000 vocabulary features.

**Activity 3 — Perform similarity analysis**

- Calculate pairwise cosine similarity between the TF-IDF talk vectors.
- Examine similarity scores for selected talks.
- Identify the most similar talks by ranking their scores.
- Exclude the selected talk itself from its recommendations because its similarity with itself is 1.0 and it is not a useful recommendation.

**Recorded result:** The similarity matrix has a shape of **(4,005, 4,005)**, with one row and one column for each talk.

**Activity 4 — Generate sample recommendations**

- Select at least three different TED Talks.
- Generate the five highest-ranked similar talks for each selected talk, excluding the selected talk itself.
- Record the selected talk, recommended talk titles, speaker names, ranks, and similarity scores.
- Manually review whether the recommendations appear relevant.

**Sample evaluation:** Recommendations were generated for *Averting the climate crisis*, *Black Men Ski*, and *How I swam the North Pole*. The climate-crisis and North-Pole swimming examples showed several apparently related recommendations, while the *Black Men Ski* example included recommendations whose relevance was mixed. These observations were based on the displayed titles and should be checked against descriptions or transcripts for a deeper review.

**Activity 5 — Analyze limitations**

The sample review highlighted several limitations:

- Shared words can cause talks with different main subjects to appear similar.
- Related talks that use different vocabulary may receive lower similarity scores.
- TF-IDF represents word importance but does not fully understand context, intent, or semantic meaning.
- Similarity scores rank textual matches; they do not guarantee that a user will like or find a recommendation useful.
- The current content-based approach does not incorporate individual user preferences, viewing history, or feedback.

**Notebook:** `notebooks/04_tfidf_vectorization.ipynb`

### Task 5 — Content-Based TED Talks Recommendation Engine

**Objective:** Develop a reusable Python recommendation function that accepts a TED Talk title and returns the five most similar TED Talks based on their textual content.

This task builds on the TF-IDF vectors and cosine similarity approach developed in Task 4. The recommendation logic is organized into a reusable function so recommendations can be generated for different talks without repeating the complete vectorization and similarity-calculation process each time.

**Activities:**

1. **Load the cleaned dataset:** Load `data/processed/ted_talks_cleaned.csv` and verify that the required talk titles and processed text are available.
2. **Prepare TF-IDF representations:** Generate TF-IDF vectors from the processed talk text. This preparation is performed as part of system setup, not every time a user requests recommendations.
3. **Calculate cosine similarity:** Calculate the similarity matrix so that each talk can be compared with the others.
4. **Create a reusable recommendation function:** Implement `recommend_talks(title, top_n=5)`. The function identifies the selected talk, retrieves its similarity scores, excludes the selected talk itself, and returns the top `top_n` recommendations.
5. **Handle invalid titles:** Handle a title that does not exist in the dataset appropriately, rather than returning misleading recommendations or failing unexpectedly.
6. **Test different titles:** Call the function with different TED Talk titles and inspect the returned recommendations.
7. **Display readable results:** Present recommended talk titles and relevant details, together with similarity scores, in a Pandas DataFrame.
8. **Document observations and review questions:** Record what the test cases demonstrate and explain the recommendation logic discussed during the review session.

**Important implementation principle:** TF-IDF vectorization and cosine similarity calculation should be performed once when preparing the recommendation system. The reusable function should use the prepared vectors and similarity matrix for subsequent title-based requests.

**Notebook:** `notebooks/05_content_based_recommendation.ipynb`

**Submission requirements:**
- Submit the completed notebook with its execution outputs.
- Include screenshots demonstrating successful test cases.
- Ensure that the function is reusable, clearly organized, and handles invalid TED Talk titles appropriately.

## Current Project Status

Tasks 1–5 have been completed according to the workflow documented in this README. Task 4 established the TF-IDF and cosine-similarity baseline, generated sample recommendations, and documented its limitations. Task 5 builds on that work by organizing the recommendation process into a reusable title-based function. The current project is a content-based recommendation system: it compares talk text and ranks similar talks, but does not yet model individual user preferences, viewing history, or feedback. Further improvements, evaluation methods, or application development should be documented as they are implemented and tested.

## Notes

- Keep the raw dataset unchanged in `data/raw/`.
- Run the notebooks in workflow order so that each processed output is available to the next stage.
- The row order of the DataFrame used for displaying recommendations must remain aligned with the row order used to create the TF-IDF matrix and similarity matrix.
- The selected talk's own similarity score must be excluded when generating recommendations.
- In Task 5, prepare the TF-IDF vectors and similarity matrix once; subsequent calls to `recommend_talks(title, top_n=5)` should reuse them rather than recalculating them for every request.
- The recommendation function should handle titles that are not present in the dataset and return readable recommendation results.
- Similarity scores are not percentages and should not be interpreted as measures of user satisfaction.
- Do not commit the local `venv/` environment or large generated dataset files unless repository instructions explicitly require them.

### Task 6 — Feature Selection and Recommendation Quality Evaluation

In this task, four different feature combinations were experimented with to evaluate their impact on TED Talk recommendation quality using TF-IDF vectorization and cosine similarity.

The experiments were conducted using five sample TED Talks:

1. Letting go of God
2. Do schools kill creativity?
3. My wish: A global day of film
4. The birth of Wikipedia
5. Improvising on piano, aged 14

The following observations were made:

- **Experiment 1 – Title Only:** Recommendations were primarily influenced by overlapping words in TED Talk titles. Although some relevant talks were identified, several recommendations shared individual words without necessarily discussing similar subjects. This indicated that titles alone provide limited information for generating meaningful recommendations.

- **Experiment 2 – Title + Tags:** Adding topics improved recommendation relevance by introducing additional subject-related information. Recommendations became more closely associated with the original talk's theme, particularly for religion, films and online collaboration. This demonstrated the importance of topic information in content-based recommendation.

- **Experiment 3 – Title + Description + Tags:** Including descriptions provided additional contextual information and improved recommendations for certain topics, particularly education. However, some unrelated recommendations were still generated, suggesting that descriptions may introduce additional vocabulary that does not always contribute to recommendation relevance.

- **Experiment 4 – Title + Description + Transcript + Tags:** Including transcripts provided a more comprehensive representation of each TED Talk's content. The recommendations showed stronger contextual relationships in several examples, particularly for education, films and music. However, a few irrelevant recommendations were still observed.

### Final Feature Selection

Based on the observations from all four experiments, **Experiment 4 – Title + Description + Transcript + Tags** was selected as the preferred feature combination for the TED Talks Recommendation System.

The primary reason for this selection is that it incorporates multiple sources of textual information, allowing the recommendation model to consider not only the title and topics but also the descriptions and actual spoken content of each TED Talk.

Although including transcripts increases the amount of textual data and does not guarantee that every recommendation will be relevant, it provides a richer representation of the talks and produced more meaningful contextual recommendations across most of the selected examples.

Therefore, Experiment 4 was considered the most suitable feature combination among the four approaches evaluated and will be used as the preferred feature set for further development of the recommendation system.

**Overall Learning:** The experiments demonstrated that feature selection plays an important role in content-based recommendation systems. Combining different textual features can improve the representation of content and help generate more contextually relevant recommendations than relying on titles alone.

## Task 7: Understanding User Preferences and Preparing Interaction Data 

1. A simulated user interaction dataset was created containing 20 users and 280 interactions across 50 TED Talks.

2. Each user has 14 recorded TED Talk interactions, including ratings, likes, watch status, and bookmarks.

3. The user-item matrix was successfully generated with a shape of 20 × 50.

4. Out of 1,000 possible user-talk combinations, 280 contain ratings, resulting in a matrix density of 28%.

5. The remaining 720 entries represent missing ratings, indicating that users have not rated those TED Talks.

6. The rating analysis identified TED Talks with comparatively higher average ratings and greater interaction counts.

7. Every user has rated 14 TED Talks, while their average ratings differ according to their simulated preferences.

8. The interaction patterns provide a foundation for understanding Collaborative Filtering, including user-based and item-based recommendation approaches.

**Conclusion:** Task 7 successfully demonstrates how user interaction data can be collected, analyzed, and transformed into a user-item matrix. This data can be used as the foundation for implementing Collaborative Filtering in the recommendation system.

**Dataset limitation:** All user profiles, interactions, and ratings are simulated. They are intended for learning and experimentation rather than representing real-world TED user behavior.