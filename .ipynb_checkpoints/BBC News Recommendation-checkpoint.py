#!/usr/bin/env python
# coding: utf-8

# In[4]:


import numpy as np
import pandas as pd


# In[6]:


df = pd.read_csv('bbc-news-data.csv', sep='\t').sample(500, random_state = 115)

df.head()


# In[20]:


df['category'].unique()


# In[22]:


#checking missing value

df.isnull().sum()


# In[30]:


from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


# Apply TF-IDF Vectorizer to the 'content' column
tfidf = TfidfVectorizer(analyzer='word', ngram_range=(1, 3), min_df=2, stop_words='english')
tfidf_matrix = tfidf.fit_transform(df['content'])

# Function to get user input
def get_user_input():
    user_input = input("Enter a news topic or description: ")
    tf_idf_input = tfidf.transform([user_input])
    return tf_idf_input

# Function to get top matching articles
def get_news(tfidf_matrix, tf_idf_input):
    cosine_similarities = cosine_similarity(tf_idf_input, tfidf_matrix)
    top_n = 5

    # Get top indices and corresponding similarity scores
    top_indices = cosine_similarities.argsort()[0][-top_n:]
    top_scores = cosine_similarities[0][top_indices]

    results = [
        (
            df['title'].iloc[i],
            df['category'].iloc[i],
            df['content'].iloc[i],
            score,
        )
        for i, score in zip(top_indices, top_scores)
    ]
    return results

if __name__ == '__main__':
    flag = True
    while flag:
        tf_idf_input = get_user_input()
        result = get_news(tfidf_matrix, tf_idf_input)

        print("\nTop 5 Recommended News:")
        for title, category, description, score in result[::-1]:  # Reverse to show highest scores first
            print(f"-> {title} (Category: {category}, Similarity: {round(score, 2)})\n   {description[:300]}...")  # Limit description to 200 chars

        print("\nDo you want to find more NEWS? (yes/no)")
        user_choice = input().lower()
        if user_choice != "yes":
            flag = False


# ## Usage examples:
# 
# 
# * Business:
# 
# 
# "latest trends in the stock market"
# 
# "global trade agreements and their effects"
# 
# 
# * Politics:
# 
# "current political events in the UK"
# 
# "the latest developments in international relations"
# 
# 
# * Entertainment:
# 
# "upcoming award shows and nominations"
# 
# "interviews with popular musicians"
# 
# 
# 
# * Tech
# 
# "cybersecurity threats and prevention"
# 
# "the impact of technology on education"
# 
# 
# * Sport:
# 
# "latest football scores and highlights"
# 
# "news and analysis of the Premier League"
