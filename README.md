
# Personalized TED Talks Recommendation System Using Machine Learning

## 1. Project Overview

The Personalized TED Talks Recommendation System is a machine learning project designed to recommend TED Talks based on their content.

The system uses information such as talk titles, descriptions, topics, and transcripts to identify talks with similar content and suggest relevant talks to users.

## 2. Objectives

- Collect and inspect a TED Talks dataset.
- Explore the dataset and identify data-quality issues.
- Preprocess text data for recommendation.
- Build a content-based recommendation model.
- Recommend similar TED Talks using text similarity.
- Provide links to recommended TED Talks.

## 3. Dataset

- **Dataset:** TED Ultimate Dataset
- **Source:** Kaggle
- **Dataset URL:** https://www.kaggle.com/datasets/miguelcorraljr/ted-ultimate-dataset
- **Local dataset file:** `data/raw/ted_talks.csv`
- **Records:** 4,005
- **Columns:** 19
- **Licence:** CC BY-NC 4.0

Licence details: https://creativecommons.org/licenses/by-nc/4.0/

## 4. Technologies Used

- Python
- Jupyter Notebook
- Visual Studio Code
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Scikit-learn
- Natural Language Processing (NLP)

## 5. Project Structure

```text
ted-talks-recommender/
│
├── data/
│   ├── raw/
│   │   └── ted_talks.csv
│   └── processed/
│
├── notebooks/
│   └── 01_data_exploration.ipynb
│
├── .venv/
├── requirements.txt
└── README.md
```

## 6. Environment Setup

### Step 1: Create and activate a virtual environment

Windows PowerShell:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

### Step 2: Install the required packages

```powershell
python -m pip install -r requirements.txt
```

### Step 3: Open the project notebook

Open the project in Visual Studio Code and select the `.venv` Python interpreter.

Run the notebook:

`notebooks/01_data_exploration.ipynb`

## 7. Current Progress

### Task 1: Environment Setup and Dataset Collection

- Created the project folder structure.
- Set up the Python virtual environment.
- Installed the required libraries.
- Collected the TED Talks dataset.
- Inspected the dataset dimensions, columns, and data types.
- Checked missing values and duplicate records.
- Verified unique talk IDs and transcript availability.
- Prepared the Dataset Inspection Report.

## 8. Planned Work

- Exploratory Data Analysis (EDA)
- Data-quality assessment
- Text preprocessing
- Feature extraction using suitable NLP techniques
- Content-based recommendation model
- Similarity calculation and recommendation testing
- Evaluation of recommendation results

## 9. Expected Outcome

The expected outcome is a recommendation system that accepts a TED Talk or a user's selected interests and recommends relevant talks based on content similarity.

## 10. Licence and Attribution

The dataset is identified as being distributed under the Creative Commons Attribution-NonCommercial 4.0 International licence. Follow the licence terms and provide appropriate attribution when using or adapting the dataset.
