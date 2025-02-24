# AI/Machine Learning Intern Challenge: Simple Content-Based Recommendation

**Deadline**: Sunday, Feb 23th 11:59 pm PST

---

## Overview

Build a **content-based recommendation system** that, given a **short text description** of a user’s preferences, suggests **similar items** (e.g., movies) from a small dataset. This challenge should take about **3 hours**, so keep your solution **simple** yet **functional**.

### Example Use Case

- The user inputs:  
  *"I love thrilling action movies set in space, with a comedic twist."*  
- Your system processes this description (query) and compares it to a dataset of items (e.g., movies with their plot summaries or keywords).  
- You then return the **top 3–5 “closest” matches** to the user.

---

## Requirements

1. **Dataset**  
   - This data set was found on Kaggle from Justin Robinson's dataset on movies
   - https://www.kaggle.com/datasets/jrobischon/wikipedia-movie-plots
   - It includes titles, dates, and the wikipedia description of the plot

2. **Approach**  
   - **TF-IDF**: this model uses term frequency-inverse document frequency to convert the text corpus into a matrix of numerical features.
      - First, stop words are removed, i.e. common words that don't add any relevant meaning to the sentence
      - It creates a matrix of words/terms with the documents the appear in as columns
      - It calculates a score for the term by finding the ratio of how often it appears in the document over how many documents contain it. This finds out which terms are relatively important to which documents (movies in this case).
   - Compute **cosine similarity** of an input query to a movie.  
      - Cosine similarity is used to compare the numerical vector of the input query to the documents. The closest matching documents will have a higher cosine similarity. 
   - Return the **top 5** similar items.
   - A more involved version of this code produces an AI-generated plot based on the query using Gemini and then recommends similar movies. This does improve similarity scores and overall recommendations.

3. **Code Organization**  
   - **Jupyter Notebook** 

4. **Output**  
   - When given an input description (e.g., `"I like action movies set in space"`), and a number of movies to return, the code outputs data in the following format:
      Top Movie Recommendations:

                           Title   Release Year  \
              Strange Magic          2015   
      

                                                         Plot  Similarity Score  
        A realm divided between a land of fairies and ...          0.049546  

5. **Summary & Instructions**  
   - A short `README.md` that includes:
     - **Dataset**: Kaggle  
     - **Setup**: 
      - Python version 3.11.9
      - Install dependencies: `pip install -r requirements.txt` 
     - **Running**: Open your notebook in Jupyter.  
     - **Results**: A brief example of your system’s output for a sample query.
         Top Movie Recommendations:

                              Title  Release Year  \
                 Strange Magic          2015   
             The Perfect Match          2016   
                 Hail, Caesar!          2016   
             The Good Catholic          2017   
           The Disaster Artist          2017   

                                                            Plot  Similarity Score  
           A realm divided between a land of fairies and ...          0.049546  
           Charlie is a playboy who's convinced that rela...          0.035614  
           In 1951, Eddie Mannix (Josh Brolin) is the hea...          0.026443  
           Three Catholic priests live in a rectory toget...          0.023802  
           San Francisco, 1998: 19-year-old Greg Sestero ...          0.020480  

6. **Salary Expectations***
   - $20/hours or ~$8000/mo
---

## Deliverables

https://youtu.be/PnuB-2seD_c

