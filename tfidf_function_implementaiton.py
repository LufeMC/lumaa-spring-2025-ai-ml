# -*- coding: utf-8 -*-
"""
Created on Sun Feb 23 12:05:56 2025

@author: manid
"""


import pandas as pd
import numpy as np
import sys
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity



def tf_idf_function(query):

   #load dataset
   df=pd.read_csv("./dataset/top_250_shows.csv")
   num_movies_needed=5



   #add query to list of movies
   documents=df["Description"]
   append_query=pd.Series([query])
   documents=pd.concat([append_query, documents])

   #tf-idf vectorization 
   vec=TfidfVectorizer()
   vectors=vec.fit_transform(documents).toarray()


   #cosine similarity with query
   scores=(cosine_similarity(vectors[0:1], vectors[1:], dense_output=True))

   #get the top five scores
   #associate scores with movie
   sorted_scores={}
   movie_scores = {key:value for key,value in zip(list(df["Title"]),list(scores[0]))}
   sorted_scores=sorted(movie_scores.items(), key=lambda x:x[1], reverse=True)


   #output scores
   print("RECOMMENDED MOVIES: ")
   count=0
   for movie, score in sorted_scores:
       count+=1
       print(movie, "(Similarity: {})".format('{0:.2f}'.format(score)).rjust(50-len(movie)," "))
    
       if count==num_movies_needed:
           break
    



def main():
   #get input query
   query=None
   if len(sys.argv)<2:
       print("Please Input a Query")
   else:
       query=sys.argv[1]

   tf_idf_function(query)


if __name__ == "__main__":
   main()


   #Notes:
       #the movie ratings are the 'documents'
       #a list of vectors are returned, each one corresponding to a movie
