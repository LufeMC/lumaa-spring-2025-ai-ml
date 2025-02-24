Applicant: Meenakshi Manikandan

This program is a movie recommendation system, allowing for users to find movies according to their tastes without needing to research hundreds of movies! Recommendations are based on a Tf-IDF vectorization + cosine similarity algorithm.

## Dataset
The dataset used includes the names and summaries of the top 250 IMDB movies. It is one of the public datasets found on Kaggle, and it must be downloaded and unzipped. Pandas, the dataframe-based Python library, was used to load the data into the program. 

## Setup
Python version 3.12 is used. To install the dependencies, we simply run the command:  
`pip install -r requirements.txt`

## Running
In this program, we take in a query to compare the movies with. To run the recommendation system, we run the command:  
`python tfidf_function_implementation.py "QUERY HERE"`  
The query can be replaced with one's own text.

## Results
After running the program, we expect to see the top 5 movies that are most related the given query, as well as the movies' corresponding similarity scores to the query. For example, if our query were to be "funny sci-fi movies set in space," our expected five movies would be:  
  
(1) The Iron Giant       (Similarity: 0.10)  
(2) Blade Runner         (Similarity: 0.09)  
(3) Wall-E               (Similarity: 0.09)  
(4) Some Like it Hot     (Similarity: 0.09)  
(5) Ladri di Biciclette  (Similarity: 0.09)  
  
This makes sense because the Iron Giant and Wall-E are sci-fi/space movies targeted towards a younger audience specially for its humor. Blade Runner is also a prominent sci-fi movie.  
  
Salary expectation: $20/hr (negotiable!)
