# Simple Content-Based Recommendation

## Summary

This project is a content-based movie recommendation system that uses BERT embeddings and cosine similarity to suggest movies based on user input. Users can specify genres, descriptions, ratings, and release years to refine their recommendations.

## Dataset

The dataset contains 100-500 movie records, including:

- **title** (Movie name)
- **description** (Plot summary)
- **genre** (List of genres)
- **rating** (IMDb rating)
- **year** (Release year)

**Source:** IMDb dataset -> https://www.kaggle.com/datasets/shreyasur965/imdb-top-100-movies-dataset?select=top_100_movies.csv

The dataset should be stored as a CSV file (e.g., `movies.csv` or whatever name is simple).

However would be easier to just clone repository. 😁

## Setup

### Requirements

- Python 3.11+ (Recommended)
- Virtual Environment (Optional but Recommended!)

### Installation Steps

Clone the repository:

```bash
git clone https://github.com/<yourusername>/gg-lumaa-spring-2025-ai-ml.git
```

Should look like this afterwards in your terminal:

```bash
(base) gregorygrullon@MacBookAir gg-lumaa-spring-2025-ai-ml %  
```

Create and activate a virtual environment:

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

Make sure terminal looks like this before installing dependencies (if using Virtual Enviornment):
```bash
(venv) (base) gregorygrullon@MacBookAir gg-lumaa-spring-2025-ai-ml %  
```

Install dependencies:

```bash
pip install -r requirements.txt
```

## Running the Code

### Running the Script

To get movie recommendations based on user input:

```bash
python recommend.py "I like action movies after 2000 with a rating above 8.5"
```

### Running in a Jupyter Notebook

Open Jupyter Notebook:

```bash
jupyter notebook
```

Open `ContentRecommendation.ipynb` and run the notebook cells.

## Results

### Example Query:

**User Input:**

```text
"Enter the number of recommendations you want: " (type 1,2,3,4,5, etc...)
"I like action movies after year 2000 with a rating above 8.5"
```

**Output:**

Top 5 Recommended Movies:

<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>title</th>
      <th>genre</th>
      <th>rating</th>
      <th>year</th>
      <th>similarity</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>17</th>
      <td>Spider-Man: Across the Spider-Verse</td>
      <td>['Animation', 'Action', 'Adventure']</td>
      <td>8.7</td>
      <td>2023</td>
      <td>0.312188</td>
    </tr>
    <tr>
      <th>6</th>
      <td>The Lord of the Rings: The Return of the King</td>
      <td>['Action', 'Adventure', 'Drama']</td>
      <td>9.0</td>
      <td>2003</td>
      <td>0.278019</td>
    </tr>
    <tr>
      <th>8</th>
      <td>The Lord of the Rings: The Fellowship of the Ring</td>
      <td>['Action', 'Adventure', 'Drama']</td>
      <td>8.8</td>
      <td>2001</td>
      <td>0.267552</td>
    </tr>
    <tr>
      <th>2</th>
      <td>The Dark Knight</td>
      <td>['Action', 'Crime', 'Drama']</td>
      <td>9.0</td>
      <td>2008</td>
      <td>0.247245</td>
    </tr>
    <tr>
      <th>12</th>
      <td>The Lord of the Rings: The Two Towers</td>
      <td>['Action', 'Adventure', 'Drama']</td>
      <td>8.8</td>
      <td>2002</td>
      <td>0.246011</td>
    </tr>
  </tbody>
</table>
</div>

## Salary Expectation

### [$2000 - $2400] monthly

## Contributing

Feel free to fork this repository and submit pull requests with improvements or additional features! 🤝
