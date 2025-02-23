# AI/Machine Learning Intern Challenge: Simple Content-Based Recommendation

**Deadline**: Sunday, Feb 23th 11:59 pm PST
#Name
-Harman Singh
-UMBC
-CompSCI/Math
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
   - Got a small Movies Dataset with about 200 rows that has titles, genres, and plot summary
   - it is attached in the main fork of this repo, PLEASE DOWNLOAD THIS FILE AND KEEP THE NAME SAME
   - It will be used to read in the file
   - To use it, when running in the notebook PLEASE UPLOAD THE DATASET FILE "movie1_dataset.csv"
   - and the run sequentially run the code blocks
2. **Approach**  
   - My approach was simple. I first did TF-IDF vectors on both the user input, and then I did the same for each movie, in which my calculations took into account the title, genre, and summary, and computed the corresponding vector and then using that i did cosine similarity to see how similar they are with one another 

3. **Code Organization**  
   - I used Google Colab
    

4. **Output**  
   - My solution prints out 5 recommendations and the corresponding score next to it

5. **Summary & Instructions**  
   - A short `README.md` that includes:
     - **Dataset**: Where it’s from, any steps to load it: I GOT THE DATASET FROM https://www.kaggle.com/datasets/rounakbanik/the-movies-dataset/data WHICH I CLEANED THE DATA UP AND USED IT 
     - **Setup**: in this repo, it should say open with google colab, click that and once opened, please upload the dataset that is labeled "(movie1_dataset.csv), and then run the code blocks
     - **Running**: just click play on the code blocks in the notebook , make sure to have the dataset uploaded in the notebook 
     - **Results**: A cryptic message from Bond‚Äôs past sends him on a trail to uncover a sinister organization.
Here are the top 5 recommended movies based on your preference:
Title	Similarity
2	Spectre	0.580744
220	Jason Bourne	0.069612
11	Quantum of Solace	0.065424
30	Skyfall	0.061510
164	Watchmen	0.052952


---

## Deliverables

1. **Fork the Public Repository**  
   - **Fork** this repo into your own GitHub account.

2. **Implement Your Solution**  
   - MY SALARY EXPECTATIONS PER MONTH: 30 per hour * 40 hours * 4 = 4800
   - but i am content with anything above 4000 per month 

3. **Short Video Demo**  
   - In a `.md` file (e.g., `demo.md`) within your fork, paste a link to a **brief screen recording** (video link).  
   - Demonstrate:
     - How you run the recommendation code.  
     - A sample query and the results.

4. **Deadline**  
   - Submit your fork by **Sunday, Feb 23th 11:59 pm PST**.

> **Note**: This should be doable within ~3 hours. Keep it **straightforward**—you do **not** need advanced neural networks or complex pipelines. A simple TF-IDF + cosine similarity approach is sufficient.

---

## Evaluation Criteria

1. **Functionality**  
   - Does your code run without errors?  
   - When given an input query, does it successfully output relevant items?

2. **Code Quality**  
   - Clear, commented code (where it counts).  
   - Logical steps (load data → transform → recommend).

3. **Clarity**  
   - Is your `README.md` straightforward about setup, how to run, and what to expect?

4. **ML/Recommendation Understanding**  
   - Basic implementation of a content-based recommendation approach (vectorization, similarity measure).

**We look forward to seeing your solution!** Good luck!
