Dataset: "IMDb Top 1000 Movies" from Kaggle
- source: https://www.kaggle.com/datasets/octopusteam/imdb-top-1000-movies
- colunms: id	title	genres	averageRating	numVotes	releaseYear

Setup: 
- Python version: 3.13.2
- Package used: pandas, sklearn.feature_extraction.text.TfidfVectorizer, sklearn.metrics.pairwise.cosine_similarity

Running: Please open the notebook in Jupyter.

Results: A brief example of your system’s output for a sample query.
- Example query: "I love thrilling action movies set in space, with a comedic twist."
- Output: id	title	genres	similarity
720	tt1128075	Love Exposure	Action, Comedy, Drama	0.417728
184	tt0062622	2001: A Space Odyssey	Adventure, Sci-Fi	0.386343
952	tt0113703	Love Letter	Drama, Romance	0.365917
436	tt0118694	In the Mood for Love	Drama, Romance	0.347219
723	tt22488728	Love Today	Comedy, Drama, Romance	0.335965
