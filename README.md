# AI/Machine Learning Intern Challenge: Simple Content-Based Recommendation

**Author**: Fiona Jiang

---

## Overview

This repo build a **content-based recommendation system** that, given a **short text description** of a user’s preferences, suggests **similar items** (e.g., movies) from a small dataset. This challenge should take about **3 hours**, so keep your solution **simple** yet **functional**.

### Example Use Case

- The user inputs:  
  *"I love thrilling action movies set in space, with a comedic twist."*  
- Your system processes this description (query) and compares it to a dataset of items (e.g., movies with their plot summaries or keywords).  
- You then return the **top 3–5 “closest” matches** to the user.

---

## Details

1. **Dataset**  
   - From Kaggle (`the movie dataset` by `rounakbanik` from kaggle, specifically `movies_metadata.csv`). Includes a list of movies with plot summaries overview.  
   - We are using a subset of 500 randomly selected rows so the solution remains quick to implement and run.  
   - You can reproduce the exact dataframe we used in this project by two approachs:
     - Follow the code instruction in the jupyter notebook's dataset loading section
     - We have downloaded the specific subset we used in `movie_500.csv` in this repository, you can use that directly.

2. **Approach**  
   - **Content-Based**: At a minimum, use text similarity to recommend items.  
     - For instance, you can transform both the user’s text input and each item’s description into TF-IDF vectors and compute **cosine similarity**.  
   - Return the **top N** similar items (e.g., top 5).

3. **Output**  
   - You can see an example output in `sample_output.json`.

4. **Instructions**    
   - **Setup**: You need a python environment to run this project. You can install all dependencies with (`pip install -r requirements.txt`).  
   - **Running**: You can run the code with any user query prompt by running the first two modules of the notebook (all the way until the Testing section), then use the function `compute_similarity` to execute the program with your user input. If you want to store the results in json file, feel free to use the structure we have on exporting the second testing example on Testing Module of the notebook.  

---

## Deliverables
1. **Short Video Demo**  
   - Here's a link to a short demo explaining how an example prompt went through the system. [video link](https://youtu.be/IZDTln1CR-k)
   - Demonstrate:
     - How you run the recommendation code.  
     - A sample query and the results.
