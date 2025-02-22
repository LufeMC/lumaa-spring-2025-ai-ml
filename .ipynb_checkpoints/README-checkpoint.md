# AI/Machine Learning Intern Challenge: Simple Content-Based Recommendation

---

## Overview

This project makes a content recommendation system that suggests movies to a user based on a short description of the desired movie. The framework uses TF-IDF vectorization and cosine similarity to check a user's input with the database and return the most similar results.

## Dataset

The dataset used for this recommendation system is a list of 250 top movies from IMDB in 2022. [Dataset](https://www.kaggle.com/datasets/rounakbanik/the-movies-dataset)

## Setup

---

### Loading dataset

1. Dowlnoad **'imbd(MOVIES).csv'** from the Kaggle dataset
2. Place it in the main project directory

### Requirements
- Python 3.8+
- Jupyter Notebook
- Virtual environment

### Installation
1. Clone the repository onto your local machine:
   ```sh
   git clone git@github.com:ryl2005/lumaa-spring-2025-ai-ml.git
   ```
2. Create virtual environment:
   ```sh
   python -m venv .venv
   source .venv/bin/activate
   ```
4. Install dependencies:
   ```sh
   pip install -r requirements.txt
   ```

---

## Running the code

To run the content recommendation system open a jupyter notebook:
```sh
jupyter lab
```
Then run all the cells in **main.ipynb** sequentially.

You will be prompted to enter a descritpion of a movie that you would like a recommendation for.

---

## Results

```
Enter a movie description that you would like a movie recommendation for:  I like action movies set in space
It's a Wonderful Life: Similarity = 0.1849
Aliens: Similarity = 0.1620
Saving Private Ryan: Similarity = 0.1468
Bicycle Thieves: Similarity = 0.1396
Taxi Driver: Similarity = 0.1278
```

---

## Demo

[Demo video](https://drive.google.com/file/d/1AGzZ0wme9O2_4nKuz0cxPmHbT8n3T8lI/view?usp=sharing)

---

## Salary expectation

My salary expectation is $1200-1800 / month.
