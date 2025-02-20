# IMDB Movie Recommendation System 🎬

## Overview
This project is a **simple content-based movie recommendation system** that suggests movies based on user input. It uses **TF-IDF vectorization** and **cosine similarity** to match user preferences with the genres of IMDB’s **Top 250 Movies (2021)** dataset.

---

## Dataset
- **Source:** [IMDB Top 250 Movies Dataset – Kaggle](https://www.kaggle.com/datasets/rajugc/imdb-top-250-movies-dataset?resource=download)
- **Description:** The dataset contains the **top 250 movies on IMDB** as of 2021, including:
  - Movie titles
  - Genres
  - IMDB ratings
  - Votes
  - And more relevant attributes
- **Loading the Dataset:**  
  The dataset is provided as a CSV file (`imdb_top_250.csv`). In Google Colab, you can upload the file directly or mount your Google Drive to access it.
  
---

## Setup

### Python Environment
- **Python Version:** Python 3.5+
- **Using Google Colab:**  
  No local setup is needed. The notebook is ready to run in Google Colab.

### Install Dependencies
Install the required libraries using the following command in your Google Colab notebook:
- !pip install pandas scikit-learn numpy

### Import Required Libraries
In the notebook, import the necessary libraries:
1. import pandas as pd  
2. from sklearn.feature_extraction.text import TfidfVectorizer  
3. from sklearn.metrics.pairwise import cosine_similarity

## Running the Movie Recommendation System
1. **Load the Dataset:**  
   Upload the `imdb_top_250.csv` file to your Colab environment or mount your Google Drive, then load the dataset using Pandas.
2. **Preprocess the Data:**  
   Select the relevant columns (e.g., Title and Genre) and handle any missing values.
3. **Convert Text Data into Numerical Format Using TF-IDF:**  
   Vectorize the movie genres so that they can be compared numerically.
4. **Get User Input and Compute Similarity:**  
   Enter a movie preference as a short text description. The system transforms this input using TF-IDF and calculates the cosine similarity between the user input and the movie genres.
5. **Retrieve and Display Top Recommended Movies:**  
   The system sorts the similarity scores and extracts the top 5 recommended movies, displaying their titles and genres.

## Results
### Example Query:
When you run the notebook and provide an input query, for example:  
"I love thriller movies"  

### Output from the Model:
Recommended Movies:
|      | Title                        | Genre              |
|------|------------------------------|--------------------|
| 153  | Blade Runner                  | Thriller           |
| 212  | Amores perros                 | Drama \| Thriller   |
| 224  | Donnie Darko                  | Drama \| Thriller   |
| 57   | Das Leben der Anderen         | Drama \| Thriller   |
| 148  | Room                          | Drama \| Thriller   |


### Explanation:
- In this example, the user input is "I love thriller movies." The system returns the top 5 recommended movies that best match the Thriller genre. The recommendations include both pure Thriller movies and those that belong to multiple genres, such as "Drama | Thriller". 
- The model includes movies that have the Thriller genre, even if they are also classified under other genres. This ensures that the recommendations capture a broader range of thriller-related films that might still match the user's interest.
- As a result, movies such as Blade Runner (Thriller) and Amores Perros (Drama | Thriller) are recommended, as they either belong exclusively to the Thriller genre or have Thriller as one of their genres, ensuring relevant and diverse suggestions.


