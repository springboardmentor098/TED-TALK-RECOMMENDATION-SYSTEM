## Task - 1 Environment Setup and TED Talks Dataset Collection

Set Up the Development EnvironmentUse Python, VS Code, and Jupyter Notebook for this task.

Step 1: Create the project folder. Open VS Code, open the terminal, and execute:
mkdir ted-talks-recommender
cd ted-talks-recommender

Step 2: Create a virtual environment 
python -m venv .venv 
Activate the environment: 
.\.venv\Scripts\Activate.ps1 
If PowerShell blocks activation, use the VS Code Command Prompt terminal and run: 
.venv\Scripts\activate.bat 
Verify that Python is available: 
python --version 
Step 3: Install the required packages 
Run the following command inside the activated virtual environment: 
python -m pip install pandas numpy matplotlib seaborn jupyter scikit-learn

Verify the installation: 
python -m pip list 
Save the installed package versions: 
python -m pip freeze > requirements.txt

Create the Project Folder Structure 
Create the following folders and files: 
ted-talks-recommender/ 
│ 
├── .venv/ 
│ 
├── data/ 
│   ├── raw/ 
│   └── processed/ 
│ 
├── notebooks/ 
│   └── 01_data_exploration.ipynb 
│ 
├── requirements.txt 
└── README.md 

Collect the TED Talks Dataset:

The final TED Talks dataset has been taken from Kaggle open-source platform.

# Final column selection

# Column	        Why we need it?

# talk_id	        Unique identification of each talk
# title		        Displays the talk and helps identify its subject
# speaker_1	        Displays the primary speaker
# duration	        Supports recommendations based on available time
# topics	        Matches user interests with TED Talk topics
# url		        Provides the link to watch the recommended talk
# description		Provides a concise summary for content matching
# transcript		Provides detailed textual content for NLP-based recommendations

Performed Initial Dataset Inspection Steps

Open VS Code and launch Jupyter Notebook from the project directory: 
python -m jupyter notebook 

Create or open: 
notebooks/01_data_exploration.ipynb 

Step 1: Import the required libraries 
Step 2: Load the dataset 
Step 3: Check the dataset dimensions 
Step 4: Display column names
Step 5: Inspect data types and non-null values
Step 6: Check missing values
Step 7: Check duplicate rows
Step 8: Check whether talks have unique identifiers

## Task-2 Exploratory Data Analysis (EDA) and Data Quality Assessment. 

The objective of this task is to understand the collected TED Talks dataset, identify 
data-quality issues, analyze important patterns, and prepare the data-cleaning plan 
required for the next phase of development. 
Task Objective 
Analyze the collected dataset using Python and identify its structure, quality, 
missing values, duplicates, text characteristics, and topic distribution.

Create a new notebook: 
notebooks/02_eda_data_quality.ipynb 

Load the dataset from data/raw/ and complete the following activities. 

Activity 1: Dataset Summary 
 Display the number of rows and columns. 
 List all column names and their data types. 
 Generate descriptive statistics. 
 Identify the number of unique talks, where a suitable identifier is available. 

Activity 2: Missing Values and Duplicates 
 Calculate missing-value counts and percentages for each column. 
 Identify duplicate rows and repeated talk identifiers, if available. 
 Identify missing or empty titles, descriptions, tags, transcripts, and URLs. 
 Explain which missing fields may affect the recommendation system. 

Activity 3: Text Analysis 
Where the relevant columns are available: 
 Analyze transcript and description lengths. 
 Calculate word counts. 
 Identify empty or unusually short text entries. 
 Visualize the distribution of transcript lengths. 

Activity 4: Tag and Topic Analysis 
 Identify the most frequently occurring TED Talk tags or topics. 
 Display the top 10–15 tags in a chart. 
 Explain which topics appear most frequently. 
 Document the format in which tags are stored and how they were processed. 

Activity 5: Additional Data Analysis 
If fields such as duration or views are available: 
 Generate descriptive statistics. 
 Visualize their distributions. 
 Identify unusual values or patterns. 
 Record your observations.

## Task-3 Data Cleaning and Text Preprocessing

The raw TED Talks data is taken and is cleaned for text preprocessing.

Activity 1: Load and Review the Dataset 
 Load the original dataset from data/raw/. 
 Review the findings from Task 2. 
 Identify the fields that require cleaning. 
 Preserve the original dataset without overwriting it. 

Activity 2: Handle Missing Values 
 Identify missing or empty values in important columns. 
 Decide how to handle each issue based on the field's purpose. 
 Do not remove talks with missing transcripts if other useful information is available. 
 Document your decisions and the reason behind each decision. 

Activity 3: Remove Duplicate Records 
 Identify exact duplicate rows. 
 Check for repeated talk identifiers or URLs, where available. 
 Verify that repeated records represent the same talk before removing them. 
 Record the number of duplicates identified and removed. 

Activity 4: Clean Text Fields 
Clean the available text fields, such as title, tags, description, and transcript. 
Your preprocessing should include: 
 Converting text to lowercase where appropriate. 
 Removing unnecessary leading, trailing, and repeated whitespace. 
 Handling empty strings and missing text consistently. 
 Applying appropriate punctuation handling without damaging meaningful text.

Activity 5: Create a Combined Text Field 
Create a new column called combined_text by combining available fields such as title, tags, 
description, and transcript. 
This column will be used in the next phase to convert talk content into numerical features for 
similarity-based recommendations. 

Activity 6: Save the Cleaned Dataset 
Save the processed dataset to: 
data/processed/ted_talks_cleaned.csv

## Task-4 Text Vectorization Using TF-IDF and Similarity Analysis.

The objective is to understand and implement the feature-extraction stage of our 
recommendation system using TF-IDF vectorization. 
By completing this task, you should be able to explain how the cleaned text becomes numerical 
data, how similarity is calculated, and how the results can be used to rank related talks. 

