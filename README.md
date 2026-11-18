# Personalized TED Talks Recommendation System Using Machine Learning

## 1. Project Overview

The **Personalized TED Talks Recommendation System** is a Machine Learning and Natural Language Processing (NLP)-based project that aims to recommend relevant TED Talks based on their content and user interests.

The system analyzes TED Talk titles, descriptions, topics, tags, and available transcripts to identify relationships between talks and generate recommendations.

The project initially implements content-based filtering using **TF-IDF (Term Frequency–Inverse Document Frequency)** and **Cosine Similarity**. It is further extended with feature selection experiments, user interaction data generation, and collaborative filtering to explore personalized recommendation approaches.

The overall objective is to develop a recommendation framework that combines textual similarity and user preference information to suggest relevant TED Talks.

## 2. Project Objectives

- Collect and explore a suitable TED Talks dataset.
- Perform Exploratory Data Analysis (EDA).
- Identify and handle missing values and duplicate records.
- Clean and preprocess textual data.
- Combine relevant textual attributes into a single text representation.
- Convert text into numerical features using TF-IDF.
- Calculate similarity between TED Talks using Cosine Similarity.
- Develop content-based recommendation functionality.
- Compare different textual feature combinations.
- Generate and analyze user interaction data.
- Implement collaborative filtering using user similarity.
- Establish a foundation for a personalized TED Talks recommendation application.

## 3. Technologies and Tools

| Category | Technologies |
|---|---|
| Programming Language | Python |
| Development Environment | VS Code, Google Colab, Jupyter Notebook |
| Data Manipulation | Pandas, NumPy |
| Data Visualization | Matplotlib, Seaborn |
| Machine Learning | Scikit-learn |
| Natural Language Processing | Text Preprocessing, TF-IDF |
| Similarity Measurement | Cosine Similarity |
| Recommendation Techniques | Content-Based Filtering, Collaborative Filtering |
| Clustering | K-Means |
| Version Control | Git, GitHub |

## 4. Repository Structure

The repository is organized into notebooks, datasets, and supporting project files.

```text
TED-TALK-RECOMMENDATION-SYSTEM/
│
├── colab_notebooks/
│   ├── TASK1_DATA_EXPLORE.ipynb
│   ├── TASK2_EDA.ipynb
│   ├── TASK3_DATA_CLEAN.ipynb
│   ├── TASK4_TFIDF.ipynb
│   ├── 05_content_based_recommendation.ipynb
│   ├── 06_feature_selection_evaluation.ipynb
│   ├── 07_user_interaction_data.ipynb
│   └── 08_collaborative_filtering.ipynb
│
├── dataset/
│   ├── ted_talks_en.csv
│   ├── ted_talks_cleaned.csv
│   ├── task5_recommendation_results.csv
│   ├── task6_feature_comparison.csv
│   ├── task6_manual_relevance_evaluation.csv
│   ├── task6_recommendation_overlap.csv
│   ├── user_interactions.csv
│   ├── user_item_matrix.csv
│   ├── task8_collaborative_recommendations.csv
│   ├── task8_user_item_matrix.csv
│   └── task8_user_similarity_matrix.csv
│
├── raw/
│   └── Original dataset files
│
├── processed/
│   └── Processed dataset files
│
├── .gitignore
├── requriements.txt
└── README.md
```

**Note:** The cleaned dataset may be maintained locally rather than uploaded to GitHub because it exceeds GitHub's 100 MB individual file limit. The original dataset and generated outputs should be maintained according to their respective licensing and storage requirements. The exact files available in each directory may change as development progresses.

## 5. Project Development Tasks

### Task 1: Environment Setup and Dataset Collection

- Set up the Python development environment.
- Install the required libraries.
- Identify and collect a suitable public TED Talks dataset.
- Inspect dataset columns, dimensions, data types, and missing values.
- Understand the available metadata and textual attributes.

**Expected output:** Initial dataset inspection and environment setup.

### Task 2: Exploratory Data Analysis and Data Quality Assessment

- Analyze dataset structure and descriptive statistics.
- Identify missing values and duplicate records.
- Analyze transcript and description lengths.
- Examine frequently occurring TED Talk topics and tags.
- Generate visualizations to identify important patterns.
- Assess the quality and availability of textual attributes.

**Expected output:** Data quality assessment, statistical summaries, and visualizations.

### Task 3: Data Cleaning and Text Preprocessing

- Handle missing values based on field importance.
- Identify and remove verified duplicate records.
- Normalize text and clean unnecessary whitespace.
- Preprocess available text fields.
- Combine relevant textual attributes into a `combined_text` representation.
- Save the cleaned dataset separately for subsequent tasks.

**Expected output:** A cleaned and preprocessed TED Talks dataset.

### Task 4: TF-IDF Vectorization and Similarity Analysis

- Convert combined text into numerical representations using TF-IDF.
- Examine vocabulary and feature dimensions.
- Calculate Cosine Similarity between TED Talks.
- Identify and rank the top five similar talks.
- Evaluate recommendation relevance through manual inspection.

**Expected output:** TF-IDF feature representations and similarity-based results.

### Task 5: Content-Based Recommendation System

- Load the cleaned TED Talks dataset.
- Generate textual features using TF-IDF.
- Calculate similarities between talks using Cosine Similarity.
- Develop a reusable recommendation function.
- Recommend the most similar talks based on a selected TED Talk.
- Implement title-based searching and recommendation testing.
- Save recommendation results for further analysis.

**Expected output:** A content-based recommendation system that suggests similar TED Talks based on textual content.

### Task 6: Feature Selection and Recommendation Evaluation

- Identify relevant textual attributes for recommendation.
- Experiment with different combinations of titles, descriptions, tags, and transcripts.
- Generate recommendations using different feature combinations.
- Compare recommendation outputs.
- Analyze recommendation overlap and Jaccard similarity.
- Prepare a manual relevance evaluation dataset.

**Expected output:** Feature comparison results and recommendation evaluation files.

**Evaluation note:** Similarity scores and recommendation overlap provide useful comparison measures, but they do not independently establish recommendation quality. Manual relevance evaluation is also required.

### Task 7: User Interaction Data Generation and Analysis

- Develop a user interaction dataset for recommendation experiments.
- Generate user-level interactions with TED Talks.
- Associate interaction information with actual TED Talk identifiers.
- Construct a user-item interaction matrix.
- Apply clustering to explore similarities between TED Talks.
- Analyze user preferences and interaction patterns.

**Expected output:** User interaction records and a user-item matrix.

**Note:** Generated or simulated interactions are experimental data and should not be interpreted as actual user behaviour.

### Task 8: Collaborative Filtering Recommendation System

- Load the generated user interaction dataset.
- Construct the user-item interaction matrix.
- Calculate similarities between users using Cosine Similarity.
- Identify users with similar preferences.
- Generate recommendations based on similar users' interactions.
- Exclude talks already rated or interacted with by the target user.
- Apply a fallback recommendation approach when sufficient similar-user information is unavailable.
- Save collaborative recommendation results and similarity matrices.

**Expected output:** A collaborative filtering recommendation system that generates recommendations based on similarities between users.

## 6. Recommendation Methodology

The project follows two main recommendation approaches.

### 6.1 Content-Based Filtering

Content-based filtering recommends TED Talks based on similarities in their textual attributes.

The workflow is:

1. Load the cleaned TED Talks dataset.
2. Select relevant textual attributes.
3. Combine text fields into a unified representation.
4. Apply text preprocessing.
5. Extract TF-IDF features.
6. Calculate Cosine Similarity.
7. Rank talks based on similarity scores.
8. Generate recommendations for a selected TED Talk.

**TF-IDF:** Converts textual information into numerical feature representations based on term importance.

**Cosine Similarity:** Measures the similarity between two numerical feature vectors.

### 6.2 Collaborative Filtering

Collaborative filtering generates recommendations based on user interaction patterns.

The workflow is:

1. Generate or load user interaction records.
2. Construct a user-item interaction matrix.
3. Calculate similarities between users.
4. Identify users with similar interaction patterns.
5. Predict potential preferences using similar users' interactions.
6. Exclude previously interacted-with talks.
7. Generate personalized recommendations.

This implementation uses user-based collaborative filtering as an experimental extension to the content-based approach.

## 7. Installation and Setup

### Prerequisites

- Python 3.9 or a compatible version supported by the selected dependencies.
- Git.
- VS Code, Jupyter Notebook, or Google Colab.
- Sufficient memory for processing the TED Talks dataset.

### Step 1: Clone the Repository

```bash
git clone https://github.com/springboardmentor098/TED-TALK-RECOMMENDATION-SYSTEM.git
```

### Step 2: Navigate to the Project Directory

```bash
cd TED-TALK-RECOMMENDATION-SYSTEM
```

### Step 3: Create a Virtual Environment

```bash
python -m venv .venv
```

### Step 4: Activate the Environment

Windows PowerShell:

```powershell
.venv\Scripts\Activate.ps1
```

### Step 5: Install Dependencies

The repository currently contains a dependency file named `requriements.txt`.

```bash
python -m pip install -r requriements.txt
```

### Step 6: Launch Jupyter Notebook

```bash
python -m pip install notebook
python -m jupyter notebook
```

Alternatively, upload the notebooks and required datasets to Google Colab and execute them there.

## 8. Dataset Information

The project uses a publicly available TED Talks dataset containing textual and descriptive information about TED Talks.

**Dataset source:** Add the original Kaggle or other dataset URL here after verifying the exact source.

The dataset may include attributes such as:

- Talk ID
- Talk title
- Description
- Topics or tags
- Transcript
- Speaker information
- Other available metadata

The exact attributes depend on the original dataset version.

### Dataset Preparation

The project maintains a distinction between:

- **Original dataset:** Source data collected from the dataset provider.
- **Cleaned dataset:** Data after preprocessing and quality checks.
- **Recommendation outputs:** Results generated during recommendation experiments.
- **User interaction data:** Experimental interaction records used for collaborative filtering.

### Dataset Licensing and Attribution

The dataset is subject to the licence and usage terms of its original source. TED content, particularly transcripts, must only be used, stored, and redistributed in accordance with applicable permissions and licensing conditions.

The original source, licence, and attribution information should be documented before redistributing dataset files.

## 9. Expected Outcomes

The project aims to produce the following outcomes:

- A structured and quality-assessed TED Talks dataset.
- A cleaned textual dataset suitable for NLP.
- Numerical TF-IDF representations of TED Talks.
- Cosine Similarity scores between talks.
- Content-based TED Talk recommendations.
- Feature selection and comparison results.
- User interaction records and user-item matrices.
- Collaborative filtering recommendations.
- A foundation for developing a personalized recommendation application.

## 10. Limitations

- TF-IDF primarily captures lexical similarity rather than complete semantic meaning.
- Talks using different vocabulary to discuss similar ideas may receive lower similarity scores.
- Missing transcripts may reduce the available textual information.
- Content similarity does not necessarily represent individual user preferences.
- Simulated user interactions may not represent real-world user behaviour.
- Collaborative filtering performance depends on the availability and quality of interaction data.
- Similarity scores alone do not establish recommendation relevance.
- Large datasets and similarity matrices may require considerable memory and computational resources.

## 11. Future Enhancements

The project can be extended through the following improvements:

- Semantic similarity using transformer-based language models such as BERT or Sentence-BERT.
- Hybrid recommendation combining content-based and collaborative filtering.
- Real user feedback and interaction collection.
- Improved recommendation evaluation using precision, recall, F1-score, and ranking metrics.
- Personalized ranking based on user interests.
- Interactive recommendation interface using Streamlit.
- Recommendation performance optimization.
- Deployment of the recommendation application.

## 12. Version Control

The project uses Git and GitHub for version control and collaboration.

**GitHub Repository:**  
https://github.com/springboardmentor098/TED-TALK-RECOMMENDATION-SYSTEM

**Development Branch:** `harini`

Project notebooks and supporting outputs are maintained in the repository. Large datasets exceeding GitHub's file size restrictions are excluded from normal Git commits and must be obtained or generated separately.

## 13. Contributor

**Harini**

## 14. Acknowledgement

Developed as part of the internship project titled **Personalized TED Talks Recommendation System Using Machine Learning**.

The project explores NLP, machine learning, content-based recommendation, and collaborative filtering techniques for recommending relevant TED Talks.

---

*Project status: Eight development tasks covering dataset exploration, preprocessing, feature extraction, content-based recommendation, feature evaluation, user interaction analysis, and collaborative filtering.*
