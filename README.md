
## **Movie Recommender System**

This *Python* project utilizes SBERT embeddings and cosine similarity to compare the top 500 most popular TMDB-rated movies to generate movie recommendations based on a user's specific query. 

### Dataset: [TMDB 5000 Movie Dataset](https://www.kaggle.com/datasets/tmdb/tmdb-movie-metadata?select=tmdb_5000_credits.csv)

- Download *tmdb_5000_**movies**.csv* and place alongside file location with recommender.ipynb

### Setup:

- VSCode with Jupyter Notebook Extensions, can also be ran in Juypter Notebook

- Python Kernel: 3.12.2,

- Runs in a Virtual Environment on VSCode


**Install Dependencies:**

```bash
pip install -r dependencies.txt
```


### Running:

This code is meant to be primarily ran through through each cell on VSCode/Jupyter Notebook. Please ensure that you have the proper dependencies installed to be able run through each cell. 


### Results:

Example Query: **"I like action movies set in space"**

Result: 
| CSV Row Value | Movie Title | 
| :---: | :---: | 
| 158 | Star Trek | 
| 2912 | Star Wars | 
| 95 | Interstellar | 
| 56 | Star Trek Beyond| 
| 300 | Starship Troopers |

