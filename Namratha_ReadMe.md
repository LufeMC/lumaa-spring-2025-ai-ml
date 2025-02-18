## **README Submission for Namratha Gopalabhatla**
### Dataset
- I have downloaded the dataset from [kaggle](https://www.kaggle.com/datasets/jrobischon/wikipedia-movie-plots)
- The dataset contains movie name, plot, director's name, but my focus is just the plot and the movie name for the recommendation system.

### Setup
 - The python version I have used 3.12.0
 - Run the following command in the current directory
 ```sh
 pip install -r requirements.txt
 ```
 - Open the notebook on jupter and click on **Run All**

 ### Results
 - There is a UI provided to the user to give their input query and below that the result is displayed to the user, give the top 5 results.
 - The result is printed as a table containing the Movie Name and the Similarity Scores, ordered by the Similarity Scores.
 - An example prompt and the respective result is as follows:

    ```text
     "I like action movies set in space"
     ```
| Title                   | Similarity Score|
|-------------------------|-----------------|
| A Day's Pleasure        | 0.845703        |
| A Film Johnnie          | 0.832656        |
| A Reckless Romeo        |	0.809653        |
| The Playhouse	          | 0.763868        | 
| The Masquerader	      |  0.648979       |


### Demo 
This is the link to the demo [LINK](https://drive.google.com/file/d/1bxZJRuhJjjlbtfLth8a-y0KBghmi2azI/view?usp=share_link)
