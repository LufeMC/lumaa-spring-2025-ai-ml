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

# Dataset

This system uses two CSV files:

**movies.csv**: Contains movie details including movieId, title, and genres.

**ratings.csv**: Contains user ratings with columns userId, movieId, rating, and timestamp.

To run the code you must download the dataset first ```https://www.kaggle.com/datasets/parasharmanas/movie-recommendation-system/data``` and put it in the Data directory. Ensure these files are in the Data directory. If you relocate them then you must change the lines:
```
movie_file = 'Data/movies.csv'

rating_file = 'Data/ratings.csv'
```

---

# Setup

Prerequisites

Python version: 3.8+

Install dependencies using:
```
pip install -r requirements.txt
```

After installing dependencies, download the SpaCy language model:
```
python -m spacy download en_core_web_sm
```

---

# Running the Code

Run the Jupyter Notebook and execute the script interactively.

When prompted:

Enter ```1``` for content-based recommendation or ```2``` for hybrid recommendation.

For content-based filtering, enter a movie description (e.g., *"I like action movies set in space"*).

For hybrid filtering, enter your ```userId```.

---

# Example Output

```
Enter '1' for content-based or '2' for hybrid recommendation: 1
Enter movie description preferences: I love sci-fi and adventure films with lots of action.
Extracted Genres: Action Sci-Fi Animation
Recommended Movies:
I Am So Proud of You (2008) (Score: 0.64)
Alien Rising (2013) (Score: 0.57)
Parasite Dolls (2003) (Score: 0.55)
Ghost in the Shell 2.0 (2008) (Score: 0.54)
The Cure (2014) (Score: 0.54)

Enter '1' for content-based or '2' for hybrid recommendation: 1
Enter your user ID: 3
Recommended Movies:
Children of Men (2006) (Score: 468.05)
Fire From Below (2009) (Score: 456.74)
Day After Tomorrow, The (2004) (Score: 445.39)
Jumper (2008) (Score: 435.52)
Batman (1943) (Score: 435.37)
```






