#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
import string
import nltk
from nltk.corpus import stopwords
from nltk.stem.porter import *
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


# In[2]:


# Load dataset
file_path = 'movies.csv'
train_data = pd.read_csv(file_path)
train_data.head()


# In[ ]:


# Pre Processing the data to remove stopwords, punctuations and convert it into lowercase

# stemming tool from nltk
stemmer = PorterStemmer()

# dictionary to help remove punctuations
remove_punctuation_map = dict((ord(char), None) for char in string.punctuation)

# Function to pre process the data 
def preProcessData(text):
    
  # turn document into lowercase
  lowers = text.lower()
    
  # remove punctuations
  no_punctuation = lowers.translate(remove_punctuation_map)
    
  # tokenize document
  tokens = nltk.word_tokenize(no_punctuation)
    
  # remove stop words
  filtered = [w for w in tokens if not w in stopwords.words('english')]
  
  # stemming process
  stemmed = []
  for item in filtered:
      stemmed.append(stemmer.stem(item))
    
  return stemmed


train_data["Pre_Processed_Text"] = train_data.apply(lambda x: " ".join(preProcessData(str(x["overview"]) + " " + str(x["genres"]))), axis=1)


# In[ ]:


# Find the frequent words using TF-IDF (unigrams and bigrams)
vectorizer = TfidfVectorizer(stop_words='english', max_features=5000, ngram_range=(1,2))
X_train = vectorizer.fit_transform(train_data["Pre_Processed_Text"])


# In[ ]:


# Get user input
user_input = input("What kind of movie are you looking for? ")

# Preprocess user input
test_data = " ".join(preProcessData(user_input))

# Transform into TF-IDF vector
y_test = vectorizer.transform([test_data])


# In[ ]:


# Cosine similarity to compute similarity between two rows
similairty = cosine_similarity(y_test, X_train).flatten()

#Get top 5 movies
top_similar_movies = similairty.argsort()[-5:][::-1]

print("Here are the top 5 movies recommended for you:")
for i in top_similar_movies:
    print(train_data.iloc[i]['title'],end='\n')

plot_display_input = input("\nDo you want to read the plots of these movies as well? (yes/no): ").strip().lower()

if plot_display_input == 'yes' or 'y':
    for i in top_similar_movies:
        print(f"\nMovie: {train_data.iloc[i]['title']}")
        print(f"Plot: {train_data.iloc[i]['overview']}\n")
elif plot_display_input == 'no' or 'n':
    print("Okay, happy movie time!")
else:
    print("Invalid input. Please enter a 'yes' or a 'no'.")


# In[ ]:




