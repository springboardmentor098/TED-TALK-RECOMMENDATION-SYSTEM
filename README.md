**PERSONALIZED TED TALKS RECOMMENDATION SYSTEM**

A content-based recommender that suggests TED Talks similar to one a viewer already likes, using text analysis and machine learning.

---

**OBJECTIVE**

Build a system that converts the text of each TED Talk into numerical features and uses similarity scores to recommend related talks. The final goal is to serve these recommendations in a Streamlit app.

---

**TECH STACK**

| Area | Tools |
|---|---|
| Language | Python 3.13 |
| Data handling | pandas, NumPy |
| Visualization | matplotlib, seaborn |
| Machine learning | scikit-learn (TF-IDF, cosine similarity) |
| Environment | Jupyter Notebook, VS Code, Git and GitHub |

---

**DATASET**

- **Source:** TED Ultimate Dataset (English file, `ted_talks_en.csv`) from Kaggle, renamed to `ted_talks.csv`
- **Size:** 4,005 talks. The raw file has 19 columns and the cleaned file has 23.
- **Key columns:** `talk_id`, `title`, `speaker_1`, `description`, `topics`, `transcript`, `views`, `url`

---

**PROJECT STRUCTURE**

```
Susmitha/
├── data/
│   ├── raw/ted_talks.csv                  original dataset, never modified
│   └── processed/ted_talks_cleaned.csv    cleaned dataset
├── notebooks/
│   ├── 01_data_exploration.ipynb
│   ├── 02_eda_data_quality.ipynb
│   ├── 03_data_cleaning_preprocessing.ipynb
│   └── 04_tfidf_vectorization.ipynb
├── requirements.txt
└── README.md
```

---

**WORKFLOW**

1. **Setup and data collection:** create the environment, download the dataset and inspect it.
2. **EDA and data quality:** find missing values, duplicates and text patterns.
3. **Cleaning and preprocessing:** clean the text and build one `combined_text` field.
4. **TF-IDF and similarity:** turn text into numbers and rank similar talks.
5. **Recommendation engine and evaluation:** coming next.
6. **Streamlit app:** coming later.

---

**PROGRESS**

| Task | Notebook | Status |
|---|---|---|
| 1. Environment setup and dataset collection | `01_data_exploration.ipynb` | Completed |
| 2. EDA and data quality assessment | `02_eda_data_quality.ipynb` | Completed |
| 3. Data cleaning and text preprocessing | `03_data_cleaning_preprocessing.ipynb` | Completed |
| 4. TF-IDF vectorization and similarity analysis | `04_tfidf_vectorization.ipynb` | Completed |

---

**KEY FINDINGS**

**Task 2: Data Quality**

- No fully duplicate rows and no repeated `talk_id`, `url` or `title`.
- The text fields needed for recommendations (title, description, topics, transcript and url) have no missing values.
- Gaps exist in comments (655), occupations (522), about_speakers (503), all_speakers (4) and recorded_date (1). These are not used for text similarity, so the impact is low.
- The remaining findings and the 14-row cleaning plan are in the notebook.

**Task 3: Cleaning**

- All 4,005 rows were kept and no duplicates were found.
- Text was lowercased, extra whitespace removed and punctuation handled, while the original columns were preserved.
- A `combined_text` column was created from the title, tags, description and transcript.

**Task 4: TF-IDF and Similarity**

- The TF-IDF matrix has shape **(4005, 71129)**: 4,005 talks and 71,129 vocabulary words.
- Cosine similarity compares talks. A talk scores 1.0 with itself, so it is skipped when recommending.

| Selected talk | Top-5 similarity scores | Review |
|---|---|---|
| Averting the climate crisis | 0.23 to 0.27 | All five are climate talks |
| A new strategy in the war on cancer | 0.48 to 0.61 | All five are cancer talks |
| Do schools kill creativity? | 0.25 to 0.32 | Mostly education, one weak match |

---

**LIMITATIONS**

- Scores can only rank the results for one talk. They should not be compared across different talks.
- Rare words and names can raise scores without describing the topic.
- The method matches words, not meaning, so weak matches can appear (for example, a business talk recommended for a schools talk).
- Numbers such as "00" and "000" became vocabulary words and add noise.
- A high similarity score does not guarantee that a viewer will like the recommendation.

---

**HOW TO RUN**

1. Create and activate a virtual environment (in Command Prompt):
   ```
   python -m venv .venv
   .venv\Scripts\activate.bat
   ```
2. Install the packages:
   ```
   python -m pip install -r requirements.txt
   ```
3. Open the notebooks in the `notebooks/` folder and run them in order, 01 to 04.

---

**NEXT STEPS**

- Build the recommendation engine more systematically.
- Evaluate the quality of the recommendations.
- Integrate the recommender into a Streamlit app.
