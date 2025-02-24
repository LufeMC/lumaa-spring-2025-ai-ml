# Content-based Movie Recommendation System

## Dataset

The dataset used was obtained from Kaggle's [Wikipedia Movie Plots](https://www.kaggle.com/datasets/jrobischon/wikipedia-movie-plots) dataset. For this task, we selected only the Title and Plot columns and dropped all rows where either of these contained null values. Then, we selected 500 movie title and plots at random to adhere to the small dataset requirement.

## Setup

This code was developed using Python 3.10.9. In order to install all the libraries required, one can run:

`pip install -r requirements.txt`

in their terminal (or simply run the first cell in the notebook).

## Running

To run the model, run each of the Jupyter Notebook cells in sequential order. When you run the cell with the code:

```py
if __name__ == '__main__': main()
```

You will be prompted to input a short textual description of a user's preferences in movies.

## Results

Below are the results for a prompt stating "I like comedy films":

```
Enter user review here: I like comedy films
Top 5 Movie Recommendations
1. Best Actor | Similarity Score: 0.08575388093328194
2. Alice in Wonderland | Similarity Score: 0.06601668577160774
3. The Band Wagon | Similarity Score: 0.0447180503457958
4. Major Barbara | Similarity Score: 0.03407259752676045
5. An Angel from Texas | Similarity Score: 0.03352653805024108
```

Each of these movies possesses an element of comedy, satire, or whimsiness as seen by their genre classification in the dataset and further investigation into the movies, without having actually seen the genre in the dataset!

## Discussion

For further details on model choices, different ways in which I experimented with the existing model, discussion of continued model refinement, and monthly salary expectation, see the markdown cells directly after the last code cell in the notebook.