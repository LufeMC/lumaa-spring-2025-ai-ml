# Movie Recommender System

A content-based movie recommendation system using TF-IDF vectorization and cosine similarity to suggest movies based on user preferences.

## Dataset
- The system requires a `movies.csv` file containing movie data
- The CSV file must include:
  - `title` column: Movie titles
  - `genres` column: Pipe-separated genres (e.g., "Action|Adventure|Sci-Fi")
- Place the `movies.csv` file in the same directory as the notebook
 Link to download --> https://grouplens.org/datasets/movielens/32m/

## Setup
### Requirements
- Python 3.11.5
- Jupyter Notebook

### Virtual Environment Setup
```
# Create virtual environment
python -m venv venv

# Activate virtual environment
# For Windows:
venv\Scripts\activate
# For Unix/MacOS:
source venv/bin/activate
```

### Install Dependencies
```
pip install pandas scikit-learn
```

## Running the System
1. Launch Jupyter Notebook:
```
jupyter notebook
```

2. Open `recommender.ipynb` in your browser
3. Execute all cells in sequence
4. In the final cell, modify the `query` variable with your movie preferences

## Code Structure
The system implements four main functions:
- `load_data(filepath)`: Loads movie dataset from CSV
- `build_tfidf(corpus)`: Creates TF-IDF vectors from movie genres
- `get_recommendations(user_input, vectorizer, tfidf_matrix, data, top_n=5)`: Returns top movie matches
- `run(query, csv_path='movies.csv')`: Main function that processes input and displays results

## Example Usage
```
query = "I love action movies"
run(query)
```

### Sample Output
```
Top recommendations based on query:
title                                    genres                      similarity
[Movie Title 1]                         [Genre List 1]              [Score 1]
[Movie Title 2]                         [Genre List 2]              [Score 2]
[Movie Title 3]                         [Genre List 3]              [Score 3]
[Movie Title 4]                         [Genre List 4]              [Score 4]
[Movie Title 5]                         [Genre List 5]              [Score 5]
```

The system returns the top 5 movie recommendations sorted by similarity score, showing each movie's title, genres, and how closely it matches your query.
```
