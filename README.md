# Simple Content-Based Recommendation System

## Overview
This project implements a simple content-based movie recommendation system using **TF-IDF** and **cosine similarity**. Given a query like:

> "I love thrilling action movies set in space, with a comedic twist."

the system returns the top matching movies based on their descriptions.

## Dataset
- **Dataset:** TMDB 5000 Movie Dataset (Kaggle)
- **Files:**  
  - `tmdb_5000_movies.csv`
  - `tmdb_5000_credits.csv`
- **Location:** These files are stored in the `data/` folder.
- **Source:** [Kaggle TMDB 5000 Movie Dataset](https://www.kaggle.com/datasets/tmdb/tmdb-movie-metadata)

## Setup & Dependencies
- **Python 3.7+**
- Install dependencies with:
  ```bash
  pip install pandas numpy scikit-learn

## How to Run:

In Jupyter Notebook / Google Colab:
Open movie_recommendation_system.ipynb.
Ensure the CSV files are in the data/ folder.
Run all cells.
EXP:
recommend_movies("I love thrilling action movies set in space, with a comedic twist.")

As a Python Script:
python recommend.py "I love thrilling action movies set in space, with a comedic twist."

Example Output:
Mission to Mars: 0.1442
Armageddon: 0.1307
2001: A Space Odyssey: 0.1207
Love and Death on Long Island: 0.1171
Wing Commander: 0.1160

## Demo Video
Watch the demo video here: https://drive.google.com/file/d/1Zs1xED7XTvaHi6oCeWmcQKToVay0YOfQ/view?usp=drive_link


Monthly Salary Expectation
$2,000 per month (negotiable, aligns with $25/hour for ~20 hours/week)

Additional Notes: 
The project uses relative paths (e.g., data/tmdb_5000_movies.csv), so ensure the data files are placed correctly.
