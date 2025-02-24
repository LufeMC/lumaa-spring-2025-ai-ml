
# Content-Based Movie Recommendation System




## 📚 Overview
This project is a simple content-based recommendation system that suggests movies based on a user's textual description of their preferences. By analyzing movie overviews and genres, the system returns the top matching movies from a dataset using TF-IDF vectorization and cosine similarity.

**🎬 Example Use Case**

User Input:"I love thrilling action movies set in space, with a comedic twist."

Sample Output:

```
Top Movie Recommendations:
                                           Series_Title  similarity
106                                             Aliens    0.852619
275                                       Blade Runner    0.802512
685                                       Ghostbusters    0.801570
10   The Lord of the Rings: The Fellowship of the Ring    0.781205
702                                   Bonnie and Clyde    0.741833N
```
## 📊 Dataset
**Dataset:** IMDb Top 1000 Movies

**Source:** [IMDb Dataset](https://www.kaggle.com/datasets/harshitshankhdhar/imdb-dataset-of-top-1000-movies-and-tv-shows)

**File Used:** imdb_top_1000.csv

**⚡ Dataset Columns Used:**

- Series_Title: Title of the movie.

- Overview: Short plot summary.

- Genre: Movie genres.

**🔗 Loading the Dataset**

Ensure the CSV file imdb_top_1000.csv is in the same directory as recommend.py. The script automatically handles missing values by removing incomplete rows.
## ⚙️ Setup Instructions
1) **Environment Setup**
- Ensure you have Python 3.8+ installed.

2) **Install Dependencies**
- Run the following command to install all required packages:
```
pip install -r requirements.txt
```


## 🚀 Running the Recommendation System
**💻 Jupyter Notebook Execution**
1) Open Jupyter Notebook:
```
jupyter notebook
```
2) Open the recommend.ipynb file.

3) Run all cells in the notebook and provide your movie preferences when prompted. 
For example:
```
Describe the type of movie you like: I like romantic movies with a dramatic twist in it.
```
The system will return the top recommended movies with similarity scores.
## 💾 Requirements

The requirements.txt includes:

```
pandas
numpy
scikit-learn
nltk
jupyter
```
## 📈 Results Example

**Sample Query:**
```
Describe the type of movie you like: I like romantic movies with a dramatic twist in it.
```
**Output:**
```
Top Movie Recommendations:
                               Series_Title  similarity
32                   It's a Wonderful Life    0.898999
736            The Broken Circle Breakdown    0.895630
371  Bom Yeoareum Gaeul Gyeoul Geurigo Bom    0.891633
913                              Die Welle    0.867158
0                 The Shawshank Redemption    0.700000
```
## 💬 Salary Expectation

**Hourly Salary Expectation :** 20-30$/hr

or

**Monthly Salary Expectation :** 4000$
## 📝 Notes

- The similarity threshold is set at 0.5; movies scoring below are not shown.

- Genre keywords are automatically extracted from user input when possible.
## ✅ Key Features

- Text preprocessing (lowercasing, stopword removal).

- Content-based recommendations using TF-IDF + Cosine Similarity.

- Genre extraction to enhance recommendation relevance.

- Handles missing data gracefully.