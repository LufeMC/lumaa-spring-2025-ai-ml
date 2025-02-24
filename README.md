# AI/Machine Learning Intern Challenge: Simple Content-Based Recommendation

This project implements a simple content-based movie recommendation system using TF-IDF
and cosine similarity in a Jupyter Notebook. It uses a sample of 500 movies from the
TMDB 5000 Movie Dataset and compares them to a user query, returning the most similar
movies.

## Dataset

This project uses the TMDB 5000 Movie Dataset from Kaggle, of which only a sample of 500 
is used. You can view the dataset [here](https://www.kaggle.com/tmdb/tmdb-movie-metadata).

The dataset has already been downloaded and is included in this repository, 
simply place the downloaded CSV file in the same directory as the
 `movie_recommender.ipynb` notebook.

## Setup

1. The notebook was compiled using Python 3.12.4.
2. Package installations are included in a cell at the very top of the notebook.
3. Recommend to use an application like Jupyter Notebook to interact with and run the 
notebook.
4. Ensure the dataset provided in this repository is located in the same directory as 
the notebook file before running.

## Running

To run the notebook, simply:
1. Clone the repository.
2. Using Jupyter notebook (or IDE of choice), locate the repository and open the notebook.
3. Run each cell in the order they appear, the cell for section 0 only needs to be ran once.
4. Change the user_input variable found in the last cell to adjust the input query.

## Examples

Below are a few exaples of user inputs and the resulting movie recommendations.

Query: "I want to watch a fun comedy movie"
* Top 5 movie recommendations:
   1. Knocked Up (Similarity: 0.20)
   2. Couples Retreat (Similarity: 0.19)
   3. Garfield (Similarity: 0.16)
   4. Supporting Characters (Similarity: 0.14)
   5. Don't Be Afraid of the Dark (Similarity: 0.13)

Query: "Recommend for me a movie I could watch with friends"
* Top 5 movie recommendations:
   1. Supporting Characters (Similarity: 0.17)
   2. Restless (Similarity: 0.17)
   3. What Just Happened (Similarity: 0.16)
   4. Mallrats (Similarity: 0.15)
   5. Bachelorette (Similarity: 0.15)

Query: "I want to watch something with ghosts or zombies"
* Top 5 movie recommendations:
   1. Slither (Similarity: 0.20)
   2. Garfield (Similarity: 0.13)
   3. Don't Be Afraid of the Dark (Similarity: 0.12)
   4. Away We Go (Similarity: 0.10)
   5. Scrooged (Similarity: 0.10)

## Salary Expectation
My desired salary would be in the $20-$30 an hour range, which monthly would be around 
$3000-$4000 a month with the assumption that I'm working full time during the summer.

## Additional comments
This project served as a fun and interesting refresher into the world of TFxIDF matrices and 
the likes, as I hadn't had a course cover this topic in around a year. Additionally, I greatly 
appreciated that the project was designed to not be overly complicated or take up too much time.

I would like to extend my gratitude towards Luis and the team at Lumaa for giving me this 
opportunity, and I look forwards to hearing back from you regarding my submission.

