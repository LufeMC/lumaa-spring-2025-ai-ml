# AI/Machine Learning Intern Challenge: Simple Content-Based Recommendation

**Deadline**: Sunday, Feb 23th 11:59 pm PST

---

## Overview

This is a **content-based recommendation system** that, given a **short text description** of a user’s preferences, suggests **similar items** (e.g., movies) from a small dataset. This challenge should take about **3 hours**, so keep your solution **simple** yet **functional**.

### Data Source
The dataset used in this project is sourced from Kaggle:  
Utkarsh, S. *Movie Dataset: Budgets, Genres, Insights*. Kaggle.  
[Source Link](https://www.kaggle.com/datasets/utkarshx27/movies-dataset)

### Use Case

- The user inputs:  
  *"I love thrilling action movies set in space, with a comedic twist."*  
- The system will 
   1. process this description (query)
   2. compare it to a dataset
   3. return the **top 3–5 “closest” matches** with title, release year, genre, cast, overview, and similarity score to the user.

### Example
- The user inputs "horror movies with zombie"
- The system recommends 5 results that match user's query the most.
- The reulst with the highest similarity score looks like:
```
Grindhouse (2007)
Genres: Thriller, Action, Horror
Cast: Kurt Russell Zo\u00eb Bell Rosario Dawson Vanessa Ferlito Sydney Tamiia Poitier
Overview: Two full length feature horror movies written by Quentin Tarantino and Robert Rodriguez put together as a two film feature. Including fake movie trailers in between both movies.
Similarity: 33.21%
```
## Demo
[Demo Video](https://drive.google.com/file/d/1hcGCMe9QOqjDnQId1qGKJEAt2lJgXr0L/view?usp=sharing)

## How to Run
This project is designed to run in **Google Colab**. Follow these steps: 

1. **Open the Notebook**:
[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/drive/1WcqlZG5BekuoPTsk7gYQpkUU-XRCtNmn?usp=sharing) or **Upload `main.ipynb` to your own Google Drive and open it with Colab.**

2. **Install Dependencies**:
Run the first code cell one time to install required dependencies

3. **Run All Cells**:
Use `Runtime > Run all` or execute cells manually.

<details>
  <summary>Salary Expectation? </summary>
    4,000 ~ 5,000 USD
</details>