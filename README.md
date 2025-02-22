**Movie Search Engine Using TF-IDF**

*Description*

This project implements a movie search engine using TF-IDF (Term Frequency-Inverse Document Frequency) to rank movies based on their descriptions. The system tokenizes movie descriptions, builds an inverted index, calculates IDF and document norms, and uses cosine similarity to return the most relevant movies for a given query.

*How to Run*

1. Install Dependencies

Make sure you have Python installed. Then, install the required packages using:

pip install numpy pandas

2. Prepare the Dataset

Ensure the netflix_titles.csv file is in the same directory as the code. This file should contain columns like title and description.

3. Run the Code

Execute the script using:

python main.py

Replace main.py with the filename of your script.

4. Perform a Search

To search for movies, modify the query inside the code:

results = search("A movie about love and sorrow and hope and dreams", inv_idx, idf, doc_norms)

The results will print the top 10 most relevant movie titles and their descriptions including their scores.

Output Example

0.85 : {'title': 'Movie A', 'description': 'A heartfelt story about love and dreams.'}
0.82 : {'title': 'Movie B', 'description': 'A romantic journey through sorrow and hope.'}
...