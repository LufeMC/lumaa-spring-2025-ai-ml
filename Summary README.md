Dataset:  The data set is from imdb consisting of a list of 100 movie titles and a brief description of the plot. I created a csv file called "movies.csv" based off the content on the website and then imported pandas/read the file using pd.read.csv().
Setup: I ran the code on a jupyter notebook and imported key libraries like pandas and scikit-learn.
Running: Open notebook in jupyter and edit the csv_path to adjust to your device. Make edits to number of recommendation and user_query in the last cell and run it. 
Results:     
    user_query = "I want to watch a movie about the British politicians"
    top_n = 3

Top recommendations for 'I want to watch a movie about the British politicians':
1. House of Cards (similarity: 0.222)
2. We Still Kill the Old Way (similarity: 0.201)
3. Four Lions (similarity: 0.197)
