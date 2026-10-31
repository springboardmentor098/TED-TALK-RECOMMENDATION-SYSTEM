# Personalized TED Talks Recommendation System Using Machine Learning

## Project Overview

The Personalized TED Talks Recommendation System is a Machine Learning and Natural Language Processing (NLP) based project that aims to recommend relevant TED Talks based on their content.

The system analyzes TED Talk titles, descriptions, topics, and transcripts to identify similarities between talks and generate recommendations using content-based filtering.

The initial implementation uses TF-IDF (Term Frequency–Inverse Document Frequency) for text feature extraction and Cosine Similarity to identify and rank similar TED Talks.

## Project Objectives

- Collect and explore a suitable TED Talks dataset.
- Perform Exploratory Data Analysis (EDA).
- Identify and handle missing values and duplicate records.
- Clean and preprocess textual data.
- Combine relevant textual attributes into a single text representation.
- Convert text into numerical features using TF-IDF.
- Calculate similarity between TED Talks using Cosine Similarity.
- Generate relevant TED Talk recommendations.
- Develop a foundation for a personalized recommendation application.

## Technologies and Tools

| Category | Technologies |
|---|---|
| Programming Language | Python |
| Development Environment | VS Code, Google Colab, Jupyter Notebook |
| Data Manipulation | Pandas, NumPy |
| Data Visualization | Matplotlib, Seaborn |
| Machine Learning | Scikit-learn |
| NLP | Text Preprocessing, TF-IDF |
| Similarity Measurement | Cosine Similarity |
| Version Control | Git, GitHub |

## Repository Structure

```text
TED-TALK-RECOMMENDATION-SYSTEM/
│
├── dataset/
│   └── ted_talks.csv
│
├── colab_notebooks/
│   ├── 01_data_exploration.ipynb
│   ├── 02_eda_data_quality.ipynb
│   ├── 03_data_cleaning_preprocessing.ipynb
│   └── 04_tfidf_vectorization.ipynb
│
├── raw/
│   └── Original dataset files
│
├── processed/
│   └── Cleaned dataset files
│
├── .gitignore
├── requirements.txt
└── README.md
```

*The repository may contain additional folders and files as development progresses.*

## Project Development Tasks

### Task 1: Environment Setup and Dataset Collection

- Set up the Python development environment.
- Install the required libraries.
- Identify and collect a suitable public TED Talks dataset.
- Inspect dataset columns, dimensions, data types, and missing values.

### Task 2: Exploratory Data Analysis and Data Quality Assessment

- Analyze dataset structure and descriptive statistics.
- Identify missing values and duplicate records.
- Analyze transcript and description lengths.
- Examine frequently occurring TED Talk topics and tags.
- Generate visualizations to identify important patterns.

### Task 3: Data Cleaning and Text Preprocessing

- Handle missing values based on field importance.
- Identify and remove verified duplicate records.
- Normalize text and clean unnecessary whitespace.
- Preprocess available text fields.
- Combine titles, tags, descriptions, and transcripts into a `combined_text` column.
- Save the cleaned dataset separately.

### Task 4: TF-IDF Vectorization and Similarity Analysis

- Convert combined text into numerical representations using TF-IDF.
- Examine vocabulary and feature dimensions.
- Calculate Cosine Similarity between TED Talks.
- Generate and rank the top five similar talks.
- Evaluate recommendation relevance through manual inspection.

## Recommendation Methodology

The initial recommendation workflow follows these steps:

1. Dataset collection.
2. Exploratory Data Analysis.
3. Data cleaning and preprocessing.
4. Combined text generation.
5. TF-IDF feature extraction.
6. Cosine Similarity calculation.
7. Ranking of similar TED Talks.
8. Recommendation generation.

## Installation and Setup

### 1. Clone the Repository

```bash
git clone https://github.com/springboardmentor098/TED-TALK-RECOMMENDATION-SYSTEM.git
```

### 2. Navigate to the Project Directory

```bash
cd TED-TALK-RECOMMENDATION-SYSTEM
```

### 3. Create a Virtual Environment

```bash
python -m venv .venv
```

### 4. Activate the Environment

Windows PowerShell:

```powershell
.venv\Scripts\Activate.ps1
```

### 5. Install Dependencies

```bash
python -m pip install -r requirements.txt
```

### 6. Launch Jupyter Notebook

```bash
python -m jupyter notebook
```

Alternatively, open the notebooks directly in Google Colab.

## Dataset Information

The project uses a publicly available TED Talks dataset.

Dataset source: Add the actual Kaggle or other original dataset URL here.

Dataset documentation should include:
- Original dataset source.
- Dataset licence and usage permissions.
- Number of records.
- Available metadata fields.
- Transcript availability.
- Any known dataset limitations.

Original dataset files are maintained separately from processed files to preserve the source data.

## Expected Outcomes

- A structured and quality-assessed TED Talks dataset.
- A cleaned textual dataset suitable for NLP.
- Numerical TF-IDF representations of TED Talks.
- Cosine similarity scores between talks.
- Content-based TED Talk recommendations.

## Limitations

- TF-IDF primarily captures lexical similarity rather than complete semantic meaning.
- Talks using different vocabulary to discuss similar ideas may receive lower similarity scores.
- Missing transcripts may reduce the available textual information.
- Content similarity does not necessarily represent individual user preferences.
- Recommendation quality requires further evaluation.

## Future Enhancements

- Semantic similarity using transformer-based language models.
- User-interest-based recommendation.
- Personalized ranking and recommendation evaluation.
- Interactive recommendation interface using Streamlit.
- Recommendation performance optimization.
- Deployment of the recommendation application.

## Contributor

**Harini**

## Acknowledgement

Developed as part of the internship project titled **Personalized TED Talks Recommendation System Using Machine Learning**.

## Dataset Licensing and Attribution

The dataset is subject to the licence and terms of its original source. TED content, particularly transcripts, must only be used and redistributed in accordance with the applicable permissions and licensing conditions.
