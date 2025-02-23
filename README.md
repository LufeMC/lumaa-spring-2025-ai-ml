# **Content-Based Movie Recommendation System**

## Overview
This project implements a **content-based recommendation system** that suggests **similar movies** based on a user's text input. The system analyzes **movie plot summaries and genres** to generate relevant recommendations using **TF-IDF vectorization and cosine similarity**.



## Dataset
- **Source** [IMDb Dataset of Top 1000 Movies and TV Shows - Kaggle](https://www.kaggle.com/datasets/harshitshankhdhar/imdb-dataset-of-top-1000-movies-and-tv-shows). Download the dataset from given source (data will be uploaded to repository as well) and save it in desired location. Change the path to dataset in the notebook accordingly.

## Setup Instructions
Fork the repository and do the following: 

### **Install Python (Recommended Version: `Python 3.8+`)**
Ensure you have Python installed. You can check by running:

```bash
python --version
```

### **Create a virtual environment**

**For Windows**
```bash 
python -m venv env
env\Scripts\activate
```

**For MacOS**
```bash 
python3 -m venv env
source env/bin/activate
```

### Install required dependencies
```bash
pip install -r requirements.txt
```

## Code Execution and Results
Head over to [notebook](task.ipynb) and select the appropriate Python environment for execution. Sample results are given below:

```
## Example usage and results for first TFIDF system
recommend_from_text(
    "I love thrilling action movies set in space, with a comedic twist.",
    tfidf1,  # TF-IDF vectorizer
    df,  # DataFrame with movies
    tfidf_matrix1  # TF-IDF feature matrix
)

[
    ('Amarcord', 0.2784726107555797),
    ('Aliens', 0.13616430405418317),
    ('The Man Who Would Be King', 0.13217272989380913),
    ('Barton Fink', 0.1237384750664491),
    ('Clerks', 0.11124411444494568)
]

## Example usage and results for second TFIDF system
recommend_from_text(
    "I love thrilling action movies set in space, with a comedic twist.",
    tfidf2,  # TF-IDF vectorizer
    df,  # DataFrame with movies
    tfidf_matrix2  # TF-IDF feature matrix
)

[
    ('Aliens', 0.36088016259286),
    ('Ghostbusters', 0.32641761200184327),
    ('Amarcord', 0.30567397359201156),
    ('Gattaca', 0.29298248355943465),
    ('Blade Runner', 0.2845828047168738)
]
```
**Comments**
- The reduced vector space size in the second recommendation system makes it more relevant, as we get results with higher similarity scores. It includes **Ghostbusters**, which aligns with **comedy+sci-fi** action theme. Additionally, **Gattaca** & **Blade Runner** add strong **sci-fi/thriller** elements to the second system. 
- **Aliens** is the only consistent correct recommendation among the two systems. 
- The first system's result is more focussed on **comedy**.

For accessing the video demo, refer **DEMO.md**. 
