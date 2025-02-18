# Content-Based Movie Recommendation System

## Overview
This project implements a content-based recommendation system that suggests movies based on a user's textual input describing their preferences. The system utilizes the Wikipedia Movie Plots dataset and employs TF-IDF vectorization along with cosine similarity to find the most relevant matches.

## Dataset
- **Source**: [Wikipedia Movie Plots Dataset](https://www.kaggle.com/datasets/jrobischon/wikipedia-movie-plots)
- **Description**: This dataset contains over 34,000 movie plot summaries, allowing for text-based recommendations.
- **Columns Used**: Only `Title` and `Plot` columns are considered for generating recommendations.

## Approach
1. **Preprocessing**:
   - Text is converted to lowercase.
   - Numbers and special characters are removed.
   - Lemmatization is applied to normalize words.
2. **Vectorization**:
   - TF-IDF vectorization is used to convert movie plots into numerical representations.
   - `ngram_range=(1,2)` ensures phrase-based similarity.
   - `min_df=3` filters out rare words.
3. **Similarity Computation**:
   - Cosine similarity is computed between the user's query and the dataset.
   - The top-N most similar movies are retrieved.

## Setup & Installation
### Requirements
- Python 3.x
- Required libraries:
  ```bash
  pip install kagglehub pandas numpy scikit-learn nltk
  ```

### Running the System
1. open the google colab notebook [https://colab.research.google.com/drive/1DpEoxBX3WW6Xo4cZBgbw2XA4uvmRGqUp?usp=sharing](https://colab.research.google.com/drive/18G1ccLrB8umDwhEFQvW4i-jYIhGEXOFd?usp=sharing)
2. Select runtime -> run all -> run anyway

or

1. Clone or download the repository.
2. Open `recommendation_system.ipynb` in Google Colab or Jupyter Notebook.
3. Run all cells to:
   - Download and preprocess the dataset.
   - Vectorize movie descriptions.
   - Generate recommendations based on a user query.
4. Modify the `user_input` variable to test different queries.

## Example Usage
**Input Query:**
```plaintext
"I love thrilling action movies set in space, with a comedic twist."
```
**Output Recommendations:**
```plaintext
1. Native (Score: 1.000)
2. Nine Lives Are Not Enough (Score: 0.955)
3. Power (Score: 0.924)
4. Rasta (Score: 0.828)
5. Spy (Score: 0.827)
```

## Salary Expectation
Expected monthly salary: $6,400

## Notes
- This system is **general** and does not contain hardcoded query-specific filters.
- The TF-IDF method ensures recommendations are based on text similarity but does not capture deep semantic relationships. Future improvements may involve sentence embeddings or neural network-based models.
