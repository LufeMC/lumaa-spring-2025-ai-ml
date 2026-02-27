# Content Based Movie Recommender System

## Overview

This project shows a simple yet effective content-based movie recommendation system. Given a short text description of the user's taste, the system compares this with film descriptions in a small dataset and returns the closest 3–5 matches. TF-IDF vectorization and cosine similarity are used for identifying the nearest matches based on text similarity.

## Example Use Case

For instance, if a user inputs:

> "I love thrilling action movies set in space, with a comedic twist."

The system receives the input query, transforms it to a TF-IDF vector, and compares the latter with description of each film. It responds with a list of ranked movies that best match the description, each accompanied with a similarity score.

## Dataset

- **Source:** The dataset is derived from the publicly available "IMDB Movie Dataset" on Kaggle.
- **Details:**  
  - A toy dataset (with 10 entries) is included for quick review of the dataset.
  - For full data, please refer to the [link](https://drive.google.com/file/d/1iTK_Z80gzNagzo9e-NxT8IIZWQ-2q3FI/view?usp=drive_link).
  
For details on loading the full dataset, please refer to the notebook’s instructions where a Google Drive URL is used to read the CSV data.

## Approach

1. **Preprocessing:**  
   - Convert movie overviews to lowercase.
   - Remove punctuation and extra whitespace.
   - Drop any missing entries in the key text column.
2. **Vectorization:**  
   - Use TF-IDF to convert both the movie overviews and the user query into vectors.
   - Remove English stop words to focus on significant terms.
3. **Similarity Computation:**  
   - Compute cosine similarity between the user's query vector and each movie overview vector.
   - Select and return the top N movies (default is 5) with the highest similarity scores.

## Code Organization

- **Data Loading:**  
  The dataset is loaded directly from a CSV (via a Google Drive link) into a pandas DataFrame.
- **Preprocessing Pipeline:**  
  Contains helper functions for cleaning the text (e.g., converting to lowercase, removing punctuation).
- **Vectorization & Similarity:**  
  Implements TF-IDF vectorization for the movie overviews and defines the `recommend_movies(query, df, top_n=5)` function to compute cosine similarity.
- **Testing:**  
  A sample query is provided to demonstrate how the system outputs recommended movies along with their similarity scores.

## Setup

### Prerequisites

- **Python Version:** Python 3.x or higher  
- **Libraries:**  
  - pandas  
  - numpy  
  - scikit-learn  

### Installation

1. **Clone the Repository:**
   ```bash
   git clone https://github.com/Shreyas-bellary/lumaa-spring-2025-ai-ml.git
   cd lumaa-spring-2025-ai-ml 
   ```

2. **Create a Virtual Environment:**
   ```bash
   python -m venv movie_recommender
    source movie_recommender/bin/activate  # On Windows: movie_recommender\Scripts\activate
    ```
3. **Install Dependencies:**
   ```bash
   pip install -r requirements.txt
   ```
4. **Running the Application:**
   ```bash
   jupyter notebook movie_recommender.ipynb
   ```
   - Run the cells sequentially to load the data, process it, and test the recommender system.

## Results

For example, running a sample query such as:

> "I love adventure and action movies."

it might yield the following recommendations:

| Movie_Title              | similarity |
|--------------------------|------------|
| Saving Private Ryan      | 0.177024   |
| Barton Fink              | 0.162293   |
| Clerks                   | 0.138101   |
| Veer-Zaara               | 0.130706   |
| The Secret of Kells      | 0.121724   |

These results demonstrate how the system ranks movies based on their textual similarity to the query.

## Demo Video

A short demo video is available in the repository. Please refer to the [demo.md](demo.md) file for the video link and instructions, where a brief screen recording shows:
- How to run the recommendation code.
- A sample query and the corresponding output.
