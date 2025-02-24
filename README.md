# AI/Machine Learning Intern Challenge: Simple Content-Based Recommendation

---

## Overview

This project implements a **content-based recommendation system** that suggests movies similar to a user's input description. It uses **TF-IDF vectorization** and **cosine similarity** to compare user input with movie descriptions and returns the most relevant matches.

## Dataset

- **Source**: The dataset used is **Top 1000 IMDb Movies**. It is available publicly on kaggle - https://www.kaggle.com/datasets/inductiveanks/top-1000-imdb-movies-dataset
- **Loading Instructions**: The dataset (`Top_1000_IMDb_movies_New_version.csv`) should be placed in the project directory.
- **Columns Used**:
  - `Movie Name`: The title of the movie.
  - `Description`: A brief summary of the movie plot.

## Code Structure

The recommendation system follows a structured pipeline:

Load Data: The dataset is read into a pandas DataFrame, and only relevant columns (Movie Name and Description) are kept.

Transform Data: The text descriptions are vectorized using TF-IDF (Term Frequency-Inverse Document Frequency), which converts them into numerical representations.

Recommend: Using cosine similarity, the system calculates the similarity between the user’s input and the movie descriptions, retrieving the top N most similar movies based on their similarity scores.

## Setup

### Prerequisites

Ensure you have **Python 3.7+** installed on your system. It is recommended to set up a virtual environment.

### Install Dependencies

1. Create a virtual environment (optional):
   ```sh
   python -m venv venv
   source venv/bin/activate  # On Windows use: venv\Scripts\activate
   ```
2. Install required packages:
   you can install manually:
   ```sh
   pip install pandas numpy scikit-learn nltk
   ```

## Running the Code

You can run the script via command line or Jupyter/Google Collab Notebook.

### Command Line Execution

Run the following command, replacing `"Some user description"` with a movie description of your choice. Below is an example:

```sh
python recommend.py "I love thrilling action movies set in space, with a comedic twist."
```

### Jupyter Notebook Execution

1. Open Jupyter Notebook:
   ```sh
   jupyter notebook
   ```
2. Run the notebook containing the recommendation system code.

## Results

Example Output for the query:


I love thrilling action movies set in space, with a comedic twist.


### Expected Output:


Recommended Movies:

Rank: 1  
Movie: Amarcord   
Similarity Score: 0.2256   
Description: A series of comedic and nostalgic vignettes set in a 1930s Italian coastal town.  

Rank: 2   
Movie: The Man Who Would Be King   
Similarity Score: 0.1249   
Description: Two former British soldiers in 1880s India decide to set themselves up as Kings in Kafiristan, a land where no white man has set foot since Alexander the Great.

Rank: 3   
Movie: Gravity   
Similarity Score: 0.1190   
Description: Two astronauts work together to survive after an accident leaves them stranded in space.

Rank: 4   
Movie: The Incredibles   
Similarity Score: 0.1113   
Description: While trying to lead a quiet suburban life, a family of undercover superheroes are forced into action to save the world.

Rank: 5   
Movie: Barton Fink   
Similarity Score: 0.1089   
Description: A renowned New York playwright is enticed to California to write for the movies and discovers the hellish truth of Hollywood.

The system ranks the movies based on similarity scores and provides detailed descriptions.

---

Salary expectation per month (Mandatory)   
$1600-2000/month

Thank you for reviewing my submission! I look forward to the opportunity to work with you and contribute my skills to your team. I appreciate your time and consideration.

Best,

Balpreet Kaur  
Master’s in Computer Science  
University of Massachusetts Amherst  
Email: bbalpreetkau@umass.edu

