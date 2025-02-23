## Environment setup
`pip install -r requirements.txt`

## [Dataset information](https://www.kaggle.com/datasets/rounakbanik/the-movies-dataset?select=movies_metadata.csv)
- Movies_metadata.csv: The main Movies Metadata file. Contains information on 45,000 movies featured in the Full MovieLens dataset.
- We select the **original_title** and **overview** column.
- Remember to change the file path into yours 

## Running
#### Go to `tfidf_baseline.ipynb` Jupyter Notebook, and then run each cell.
#### Three main parts:
1. Data preprocessing
2. Text vectorization using TF-IDF
3. Computing the similarity with cosine similarity

## Results
#### Calculate the similarity based on the input query and tfidf matrix.
#### Choose the top 5 score as the recommendations.
#### You can also input your own query. We will give you recommendations.

## [Demo link](https://youtu.be/MlJdljEc2tc)