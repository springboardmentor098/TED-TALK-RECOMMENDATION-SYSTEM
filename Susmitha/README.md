# TED Talks Recommendation System Using Machine Learning

## About the Project

I am working on a TED Talks Recommendation System using Machine Learning. The idea is to help users find TED Talks based on the topics they are interested in.

For example, if someone likes talks about technology, motivation, education, or science, the system should eventually be able to suggest other talks related to those interests.

I am starting with collecting and understanding the dataset before moving on to data analysis and building the recommendation model.

## Objectives

- Collect a suitable TED Talks dataset.
- Explore the dataset and understand its columns.
- Check missing values, duplicate records, and text availability.
- Prepare the data for a content-based recommendation system.
- Build a model that can suggest talks with similar content.

## Technologies Used

- **Python** – for data analysis and machine learning.
- **Pandas** – for loading and inspecting the dataset.
- **NumPy** – for numerical operations.
- **Matplotlib** – for creating charts.
- **Seaborn** – for data visualisation.
- **Jupyter Notebook** – for running code and recording observations.
- **Scikit-learn** – for text processing and recommendation techniques in later stages.
- **VS Code** – as the development environment.

## Dataset

I selected the TED Ultimate Dataset available on Kaggle.

**Source:** https://www.kaggle.com/datasets/miguelcorraljr/ted-ultimate-dataset

The dataset contains information about TED Talks, including talk titles, speaker details, topics, descriptions, URLs, and transcripts.

The downloaded CSV file is stored at:

`data/raw/ted_talks.csv`

The original dataset is kept in the raw data folder so that it remains unchanged during the project.

Before using the dataset for model development, I will check the applicable licence and content usage permissions.

## Project Structure

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
├── requirements.txt
└── README.md
```

The `.venv/` folder is also present in my local project, but it is not included in the structure above because it should not be uploaded to Git.

- `data/raw/` stores the original dataset.
- `data/processed/` will store cleaned or prepared data in later tasks.
- `notebooks/` contains the Jupyter notebooks used for analysis.
- `requirements.txt` lists the Python packages required for the project.
- `README.md` contains the project overview and setup instructions.

## Setup Instructions

### 1. Create and activate the virtual environment

Open the project folder in VS Code and run the following commands in the terminal on Windows:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

If PowerShell blocks activation, use the VS Code Command Prompt terminal and run:

```bat
.venv\Scripts\activate.bat
```

### 2. Install the required packages

With the virtual environment activated, run:

```bash
python -m pip install -r requirements.txt
```

### 3. Open the Jupyter Notebook

Run:

```bash
python -m jupyter notebook
```

Open `notebooks/01_data_exploration.ipynb` and run the notebook cells.

Make sure the dataset is available at `data/raw/ted_talks.csv` before running the notebook.

## Current Progress

**Task 1 – Environment Setup and Dataset Inspection**

- Created the project folder and virtual environment.
- Installed the required Python packages.
- Downloaded the TED Ultimate Dataset from Kaggle.
- Loaded the CSV file successfully using Pandas.
- Inspected the dataset dimensions, column names, and data types.
- Checked missing values, duplicate rows, unique talk IDs, URLs, and transcript availability.
- Recorded the initial findings in the data exploration notebook.

## Next Steps

- Perform exploratory data analysis (EDA).
- Create charts to understand the dataset.
- Examine text quality and language distribution.
- Decide how to handle missing values and other data-quality issues.
- Prepare the data for the recommendation model.
- Explore content-based recommendation techniques.

## Note

This is a work in progress. The recommendation model has not been built yet. The current stage focuses on setting up the environment and understanding the dataset before making any changes to the data.