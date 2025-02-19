**Overview**:

This project implements a simple content-based recommendation system for movies by combining the Title, Genre, and Plot columns from a movie dataset. It uses TF-IDF vectorization and cosine similarity to suggest movies that best match a user’s query.

**Dataset**:

- **Dataset Source**: Kaggle  
- **Link to the dataset**: [Wikipedia Movie Plots](https://www.kaggle.com/datasets/jrobischon/wikipedia-movie-plots)  

*Note: In the notebook, a random sample (e.g., 500 rows) is taken from the dataset to ensure quick execution. You can adjust this number in the notebook.*

---

**Setup**:

- **Python Version**: This project was developed using Python 3.8+
- **Virtual Environment Setup**:
  - Create a virtual environment:
    - On macOS/Linux:
      ```bash
      python3 -m venv venv
      source venv/bin/activate
      ```
    - On Windows:
      ```bash
      python -m venv venv
      venv\Scripts\activate
      ```
  - Install the required packages using the provided requirements.txt:
    ```bash
      pip install -r requirements.txt
      ```  

**Running the code**:
- Open the Jupyter Notebook (recommendation.ipynb) provided in this repository.
- Run the cells sequentially.
- When prompted, enter your movie preferences description (e.g., "I love thrilling action movies set in space with a comedic twist."), and the notebook will display the top movie recommendations with similarity scores.

**Example Result:**
After entering your query, the notebook displays a table similar to:
| Title | Similarity |
|----------|----------|
| Guardians Galaxy | 0.5243  |
| Star Wars IV	  | 0.4897  |
| ... | ... |

(n- number of rows)


