# Plot based similarity search for movies: TF-IDF and cosine similarity
## Overview
This is a **content-based recommendation system** that, given a **short text description** of a user’s preferences, suggests **similar movies** from a small dataset. 

### Example Use Case

 - The user inputs:

*"A thrilling story about people traveling across the space to save humanity from destruction."*

 - Your system processes this description (query) and compares it to a dataset of items (e.g., movies with their plot summaries or keywords).

 - The program then return the **top n** to the user.
 - Example run provided as GIF in `demo.md` file 
---
## Requirements

1.  **Dataset**

- Dataset is  from https://www.kaggle.com/datasets/jrobischon/wikipedia-movie-plots/data.

- Currently, out of the ~34,000 movies, we are only taking a random 1,000 movies uniformly across top genres.

- The dataset is included in the repo, but can also be downloaded

2.  **Setup**

- Python version used during building: `3.10`
- `pip install numpy pandas scikit-learn matplotlib seaborn`

3.  **Running**

- Open the notebook in Jupyter. Run through all cells and in the last cell of the notebook, there is a sample input string. You can modify it to include your preference to get a recommendation.

4.  **Results**

- When given an input description (e.g., `"I like action movies set in space"`), the following are the top 3 recommendations:
-`Top Similar Movies: Similarity: 0.2854 Title: Bodacious Space Pirates: Abyss of Hyperspace Release Year: 2014 Genre: adventure Plot: in the far future where space travel and colonialization have become the no... -------------------------------------------------- Similarity: 0.1685 Title: Gagarin: First in Space Release Year: 2013 Genre: unknown Plot: on april 12, 1961, soviet cosmonaut yuri ... -------------------------------------------------- Similarity: 0.1327 Title: Gorath Release Year: 1962 Genre: sci-fi Plot: early in the year of 1979, japans most famed rocketship, the jx1 hawk, with its crew of 30 men, was launched from the interstellar exploration agencys rocket launch...
`