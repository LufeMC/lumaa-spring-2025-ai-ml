from scipy.sparse import hstack

from preprocess import load_data
from vectorization import recommendation, vectorize

"""
Section 1 : Data Vectorization
"""

data = load_data()
data_vect_overview, vectorizer_overview =  vectorize(data['overview'])
data_vect_genres, vectorizer_genres = vectorize(data['genres'], weight=3.0) #Weighted Triple: genre is overall theme
data_vect_keywords, vectorizer_keywords = vectorize(data['keywords'])
data_vect = hstack((data_vect_overview, data_vect_genres, data_vect_keywords))



"""
Section 2 : Movie Recommendation (interface)
"""

#Outputs instructions and takes input as the string which will be compared
query = input('Welcome to the Ultimate Movie Recommender!\nPlease enter your movie preferences, but please keep in mind...'
              '\nThe more detailed your answer, the better recommendations: ')

output = recommendation(query, data_vect, vectorizer_overview, vectorizer_genres, vectorizer_keywords)

#Outputs recommended movies
print('Here are some movie recommendations:')
for movie in output:
    print(f"{output.index(movie)+1}. {movie}")