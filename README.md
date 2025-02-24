# AI/Machine Learning Intern Challenge: Simple Content-Based Recommendation

## Overview
This project implements a simple content-based recommendation system. Given a short text description of a user’s movie preferences, the system returns the top most similar movies from a small dataset. The approach uses TF-IDF vectorization to convert text into numerical vectors and cosine similarity to find the closest matches.

**Example Use Case:**  
User input:  
> "I love thrilling action movies set in space, with a comedic twist."  

The system processes the query by comparing it with movie overviews in the dataset and returns the top recommendations along with their similarity scores.

---

## Dataset
- **Source:** TMDB 5000 Movies Dataset (from Kaggle)
- **Contents:** The dataset contains movie metadata including columns such as `title` and `overview`.
- **Location:**  
  The dataset is included in this repository as a zip file at:  
  `archive (1).zip`  
  This zip file contains:
  - `tmdb_5000_movies.csv` (used for recommendations)
  - `tmdb_5000_credits.csv`

**Note:** The code loads the CSV directly from the zip archive, so no manual extraction is needed.

---

## Approach
1. **Data Loading & Preprocessing:**  
   - Load the CSV file from the zip archive.
   - Use the `overview` column as the movie description.
   - Fill in any missing values.

2. **Vectorization:**  
   - Use TF-IDF vectorization (with stop-word removal) to transform movie overviews into numerical vectors.

3. **Similarity Computation:**  
   - Convert the user query into a TF-IDF vector.
   - Compute cosine similarity between the query vector and each movie overview vector.
   - Identify and return the top N (default 5) movies with the highest similarity scores.

4. **Output:**  
   - The system outputs a list of recommended movie titles along with their similarity scores.

---

## Setup

### Requirements
- **Python Version:** Python 3.8+
- **Dependencies:**  
  - pandas
  - scikit-learn

Salary Expectation: 2000 - 4000/month

Demo video: https://youtu.be/E9u15VqvYS0

