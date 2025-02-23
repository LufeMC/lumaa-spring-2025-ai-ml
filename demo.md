Dataset :
    a spotify dataset that contains Highest Charting Position, Number of Times Charted, Song Name, number streams, artist, artist followers and genres
    Csv file is provided in git hub fork

Setup:
    The code is done Jyupter notebook which is called recommender.ipynb

Running the code and Results:
    the code can be run on using the run button and running each cell 
    It would for an input where it can be a genre , aritist, name of a song.
    It will recommend you the most similar value with the name of song, artist who sang the song, what genre it is , the highest charting position, number of time it charted, Number of followers the artist has and how similar it is to your search result.

Output :
    What music are you looking for?? Or type q to quit:  Songs from Tate McRae

    Recommend Songs:

    Song: you broke me first
    Artist: Tate McRae
    Genre: ['alt z', 'dance pop', 'pop', 'post-teen pop']
    Streams: 6,152,121
    Chart Position: 13
    Similarity Score: 0.617

    Song: working
    Artist: Tate McRae, Khalid
    Genre: ['alt z', 'dance pop', 'pop', 'post-teen pop']
    Streams: 5,666,770
    Chart Position: 146
    Similarity Score: 0.565

    Song: You
    Artist: Regard, Troye Sivan, Tate McRae
    Genre: ['dance pop', 'edm', 'pop dance', 'pop edm', 'slap house', 'tropical house']
    Streams: 4,846,549
    Chart Position: 84
    Similarity Score: 0.403
    What music are you looking for?? Or type q to quit:  Italiano music 

    Recommend Songs:

    Song: Beggin'
    Artist: Måneskin
    Genre: ['indie rock italiano', 'italian pop']
    Streams: 48,633,449
    Chart Position: 1
    Similarity Score: 0.305

    Song: CORALINE
    Artist: Måneskin
    Genre: ['indie rock italiano', 'italian pop']
    Streams: 5,241,813
    Chart Position: 127
    Similarity Score: 0.305

    Song: I WANNA BE YOUR SLAVE
    Artist: Måneskin
    Genre: ['indie rock italiano', 'italian pop']
    Streams: 24,551,591
    Chart Position: 8
    Similarity Score: 0.276

    Song: ZITTI E BUONI
    Artist: Måneskin
    Genre: ['indie rock italiano', 'italian pop']
    Streams: 7,975,148
    Chart Position: 12
    Similarity Score: 0.273

    Song: L-Gante: Bzrp Music Sessions, Vol.38
    Artist: Bizarrap, L-Gante
    Genre: ['argentine hip hop', 'pop venezolano', 'trap argentino', 'trap latino']
    Streams: 5,290,877
    Chart Position: 115
    Similarity Score: 0.175

    Song: Nicky Jam: Bzrp Music Sessions, Vol. 41
    Artist: Bizarrap, Nicky Jam
    Genre: ['argentine hip hop', 'pop venezolano', 'trap argentino', 'trap latino']
    Streams: 9,799,701
    Chart Position: 19
    Similarity Score: 0.163

    Song: Eladio Carrion: Bzrp Music Sessions, Vol. 40
    Artist: Bizarrap, Eladio Carrion
    Genre: ['argentine hip hop', 'pop venezolano', 'trap argentino', 'trap latino']
    Streams: 4,965,913
    Chart Position: 101
    Similarity Score: 0.151


https://github.com/user-attachments/assets/7b8af9dc-eb64-475d-8a22-0db8317ebbfa


    Song: Snow Tha Product: Bzrp Music Sessions, Vol. 39
    Artist: Bizarrap, Snow Tha Product
    Genre: ['argentine hip hop', 'pop venezolano', 'trap argentino', 'trap latino']
    Streams: 5,595,839
    Chart Position: 92
    Similarity Score: 0.136

    What music are you looking for?? Or type q to quit:  q


Video :
    added at the end 
    It shows the code and how I have ran it with different examples
    
Explanation for the code :
    I have created a class Recommender which contains various functions:
    - def LoadData which loads the data from the csv file 
    - def BuildVector which builds the TfIDfVectorizer
    - def getRecommendation finds the similarity between the data and user input and returns the data that are similar
    
