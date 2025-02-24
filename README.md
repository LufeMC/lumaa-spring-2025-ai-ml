# AI/Machine Learning Intern Challenge: Simple Content-Based Recommendation

**Deadline**: Sunday, Feb 23th 11:59 pm PST

---

## Pre-requisites

Python, version 3.12.2 or higher (which was the version this notebook was tested on.)\
pip, version 25.0.1 or higher

## Setup

First, clone this project to a local directory and navigate into it. You can use the command below, or use instructions to do so with the green Code button provided by GitHub.

```
git clone https://github.com/samihsq/lumaa-spring-2025-ai-ml.git movie_query
cd movie_query
```

Then, make a virtual environment for this project. Ensure you have virtualenv with the following command:

```
pip install virtualenv
```

To create and enter the virtualenv, run

```
virtualenv venv
source venv/bin/activate
```

Finally, to install the required packages, run

```
pip install -r requirements.txt
```

Perfect! You're ready to get prompting!

## Running The Code

Now, in your terminal, in the directory with the project files, run `jupyter notebook`. This will open a new window in your browser where you can look through the code behind the prompting! To navigate to the file, double click on the item called _solution.ipynb_.

From here, run all of the cells to download the movie dataset, fit to the data, and run a test comparison to a default query.

To change the query, simply edit the _input_description_ string in the second to last cell, then rerun the last two cells.

# Results

For the default query _"I love thrilling action movies set in space, with a comedic twist."_, this function returns:

```
Indices of closest movies (from closest to furthest): [461, 127, 66, 83, 67]
Distances: [0.8907968302074052, 0.8968179265380128, 0.8970058935830795, 0.9006916739419529, 0.903934328142089]

Names of closest movies: ['Lost in Space', 'Mad Max: Fury Road', 'Up', 'The Lovers', 'Monsters vs Aliens']
```

After this, the rows from the original dataset corresponding to this movie is also displayed, if a user would like more information about the most similar movies to their prompt!

# Dataset

The dataset of movies and their descriptions was found at <https://www.kaggle.com/datasets/harshshinde8/movies-csv?select=movies.csv>.

The loading of this dataset is handled by the first two cells of the notebook.
