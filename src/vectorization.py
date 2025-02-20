import numpy as np
from sklearn.metrics.pairwise import cosine_similarity

from preprocess import load_data
from sklearn.feature_extraction.text import TfidfVectorizer
from scipy.sparse import hstack

#Function that Vectorizes Data
def vectorize(input, weight=1.0):
    vectorizer = TfidfVectorizer()
    matrix = vectorizer.fit_transform(input)
    tfidf_matrix = matrix * weight
    return tfidf_matrix, vectorizer

#Main Function that perform recommendation logic
def recommendation(input, data_v, ov_vizer, g_vizer, k_vizer):
    data = load_data()
    input_vect_overview = ov_vizer.transform([input])
    input_vect_genres = g_vizer.transform([input]) * 3 #Adds Extra Weight to Genres
    input_vect_keywords = k_vizer.transform([input])

    input_vect = hstack((input_vect_overview, input_vect_genres, input_vect_keywords))

    input_data_compare = cosine_similarity(input_vect, data_v)[0]

    indices = np.argsort(input_data_compare)[-5:][::-1]

    recommended_movies = data.iloc[indices]['title'].tolist()

    return recommended_movies

"""

What vectorize() does?

The code first initializes a term frequency - inverse document frequency vectorizer.
The input is then transformed to a vector and multiplied by the weights(default to 1.0).
The TF-IDF vector and vectorizer are then return for later use.


The parameters:

input  : The data from that will be turned into a vector
weight : Applies weight to the vectorized data if specified






What does recommendation() do?

First, it loads in the data from load_data().
The input from the user is then transformed to a vector using the threes vectorizers create from when each columns data was vectorized.
Once all three transformations are combined, a cosine similarity score is computed between the two vectors, the combined data vector and the combined input vector.
This results is stored in input_data_compare which queries the first row of data, turning the data structure into a 1-Dimensional vector(making indexing easier).
I use np.argsort to store indices of the top five similarity scores, which values are then used to index the movie titles from original preprocessed data.
This is all stored as a list and returned for later use.



The recommendation function parameters:

input  : The query that will be received from the user
data_v : The matrix that combines the overview, genres, and keywords vectors
ov, g, k vizers: The vectorizers initialed when the corresponding data from the dataset was vectorized

"""