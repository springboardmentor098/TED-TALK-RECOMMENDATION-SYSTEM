
# Task 2: Exploratory Data Analysis and Data Quality Assessment

## Project Title
Personalized TED Talks Recommendation System Using Machine Learning

## 1. Objective
The objective of this task is to explore the TED Talks dataset, understand its structure, identify data-quality issues, analyze text and topic patterns, and propose a data-cleaning plan.

## 2. Dataset Overview
- Dataset: TED Talks dataset
- Number of rows: 4005
- Number of columns: 19
- Tools used: Python, Pandas, NumPy, Matplotlib, Seaborn, and Jupyter Notebook

## 3. Exploratory Data Analysis
The dataset was examined using column names, data types, descriptive statistics, and median values. The analysis also covered talk views, durations, transcript lengths, and topic frequencies.

## 4. Data Quality Assessment
Missing values were counted and their percentages calculated for each column. Duplicate rows and repeated talk IDs were checked. Important text fields, including titles, descriptions, topics, transcripts, and URLs, were checked for missing or empty values where available.

No records were deleted during this assessment.

## 5. Text Analysis
Word counts were calculated for transcripts and descriptions where available. Empty and unusually short text entries were counted. A histogram was created to visualize transcript-length distribution.

## 6. Topic Analysis
The topics column was examined to understand its format. Topic frequencies were calculated, and a chart was created to display the 15 most common topics.

## 7. Views and Duration Analysis
Descriptive statistics were generated for talk views and duration. Histograms were created to examine their distributions. Checks were also performed for zero or negative values.

## 8. Key Findings
1. The dataset contains 4005 rows and 19 columns.
2. Missing values were assessed across the dataset.
3. Duplicate rows and repeated talk IDs were checked.
4. Transcript and description word counts were analyzed.
5. Topic frequencies were calculated and visualized.
6. Views and duration distributions were examined for unusual patterns.

## 9. Proposed Data Cleaning Plan
- Investigate missing values and decide on appropriate handling for each column.
- Review duplicate rows and repeated IDs before considering any removal.
- Handle missing or empty text fields appropriately.
- Standardize whitespace and topic formatting.
- Investigate unusual views and duration values.
- Preserve the original dataset and perform future cleaning on a separate working copy.

## 10. Conclusion
This task provides an initial understanding of the TED Talks dataset and its data-quality characteristics. The findings will guide the next task, which involves data cleaning and text preprocessing.
