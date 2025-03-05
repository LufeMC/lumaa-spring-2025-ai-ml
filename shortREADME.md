# Movie Recommendation System - AI ML Challenge

This is a content-based movie recommendation system that suggests movies based on user input including a short textual description, and also takes in the minimum rating and a threshold release year (looking for movies released post this year). It uses TF-IDF vectorization and cosine similarity to find the most relevant movies.

## Dataset

The dataset was taken from Kaggle (<https://www.kaggle.com/datasets/harshitshankhdhar/imdb-dataset-of-top-1000-movies-and-tv-shows/data>) and has been preprocessed as necessary to suit our requirements. It is a IMDB movie dataset titled : 'imdb_top_1000'. It contains the following details - 
- Title
- Overview
- Genre
- Director
- Cast (Star1, Star2, Star3, Star4)
- IMDb Rating
- Release Year
- Gross
- Number of Votes
- Poster link

## Setup

- Jupyter Noteboook with Python 3.11.9 kernel
- No virtual environment was created
- May have to run 'pip install nltk' if already not present in the working environment

## Running the Recommendation System

- Ensure that the dataset is downloaded in the working directory
- Open the noteboook as a Jupyter notebook
- Run the first two cells for importing the necessary libraries and downloading essential nltk resources
- Change the path to the dataset as per your file path
- The last cell calls the recommender system and requires user input - will ask for text description, minimum rating required and movies released post which year are you looking for - enter in the 3 required inputs and you should be good to go!

## Results

- Based on the user inputs, the system recommends top 5 movies that are close enough to the user requirements.
- For a sample user input
    - Description : I like action movies set in space
    - Minimum Rating : 6.0
    - Post Release Year : 1980
  
  My system recommends the following movies -
  
![image](https://github.com/user-attachments/assets/2904f200-915d-45cb-ac6b-a64c307d0b23)



  


  

  
