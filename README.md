# Minyoung Kim's Submission


## Dataset: IMDB Top 250 Movies


To make sure the dataset was easy to handle, I chose to find a small public dataset. I used the IMDB Top 250 Movies dataset from Kaggle. Each movie is ranked, and the dataset contains the name of the movie, release year, rating, genre, certificate, run time, tagline, budget, and box office.

Here is the link to the dataset.
https://www.kaggle.com/datasets/rajugc/imdb-top-250-movies-dataset?resource=download

You can download this dataset by clicking on "⬇️ Download" and selecting "📁 Download dataset as zip (53 kB). Once the zip has been downloaded, you can extract the csv file and upload it to your Jupyter environment.
    
---

### Setup

- Python Version: 3.8+
- Install Jupyter Notebook with "pip install notebook"
- After setting up Jupyter Notebook, install required libraries manually:
  
  import pandas as pd
  import numpy as np
  
  !pip install scikit-learn
  from sklearn.feature_extraction.text import TfidfVectorizer
  from sklearn.metrics.pairwise import cosine_similarity

---

## Running

I chose to run the code through Jupyter Notebook.

1. **Open Jupyter notebook**  
   - Access your terminal on your PC and type "jupyter notebook"

2. **Open the notebook and run the cells**  
   - Run each cell in order.

3. **Replace the example query with your own query**  
   - In the last cell, feel free to replace the example query with your own.
   - Run the cell to get movies recommended most similar to your query.
    
---

## Results

I chose to include both "genre" and "tagline" into TF-IDF vectors to compute cosine similarity because I realized only using the taglines lead to inaccuracy. For example, when I inputed the query "I like romance movies about teenage love", the model only focused on the word "love" or "teen" in the tagline; not necessarily the genre of the movie, which is the most important factor of determining the most similar match.

When given an input description: "I love thrilling action movies set in space, with a comedic twist."
my model recommends:
1. Alien (Horror,Sci-Fi)
2. The Shawshank Redemption (Drama)
3. Cinema Paradiso (Drama,Romance)
4. The Dark Knight (Action,Crime,Drama)
5. Amores Perros (Drama,Thriller)

When given an input description: "I like romance movies about teenage love"
my model recommends:
1. Pulp Fiction (Crime,Drama)
2. Cinema Paradiso (Drama,Romance)
3. Casablanca (Drama,Romance,War)
4. The Best Years of Our Lives (Drama,Romance,War)
5. The Apartment (Comedy,Drama,Romance)

---

**Salary Expectation** 

Regarding the "Salary expectation per month (Mandatory)" requirement under "Implement Your Solution" in the deliverables, I wanted to clarify if this refers to the expected monthly compensation for the internship? If so, my expected monthly salary is $1,600, according to "$20~$30 per hour, 20 hours a week" mentioned on Handshake. However, I found this instruction somewhat unclear, as it was not specified where exactly this information should be included. I have added it here in the README for clarity.

---

Thank you for reviewing my submission! I look forward to your guidance. 🚀
