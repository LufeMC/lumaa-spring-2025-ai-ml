## Dataset
<b>Dataset Chosen:</b> [Movies dataset details | Kaggle](https://www.kaggle.com/datasets/sachinkumar62/movies-details) <br>
<b>Description from Kaggle Page:</b> "This dataset contains information on 8,551 movies, including titles, release dates, popularity scores, and user ratings. It features vote counts and average ratings, making it useful for analyzing top-rated films and audience preferences. The dataset also includes movie overviews, providing a brief summary of each film. Ideal for recommendation systems, trend analysis, and sentiment studies in the film industry."

Download this dataset and place the CSV file ("movies.csv") in the same folder as the Jupyter Notebook file.

## Setup

My solution runs on Python 3.11.5, so you will need that version to run it. It may work on other versions, but using this one minimizes the chances that you'll have problems.

Download the Jupyter Notebook file, run the Jupyter Notebook program (install it if you do not have it yet), open the file in the web interface that shows up, then click Cell -> Run All to execute. 

The function to find recommendations takes two parameters: The user query, and the number of recommendations desired. In the call to the function at the bottom of the notebook, either or both of these can be edited at will for different output.

Here are a few potential queries:

`provide_recommendations("I like action movies set in space", 5)` <br>
`provide_recommendations("I love romcoms", 3)` <br>
`provide_recommendations("I'm a big fan of murder mysteries", 4)` <br>

## Results

<b>Function Call:</b> `provide_recommendations("I like action movies set in space", 5)`

<b>System Output:</b>

You provided us with the following query: "I like action movies set in space" <br>
This is how many recommendations you wanted: 5 <br>
Here are 5 movies we think you'll love. 

Movie 1: "Gattaca". Similarity score: 0.2324916639956013. <br>
Movie description: "In a future society in the era of indefinite eugenics, humans are set on a life course depending on their DNA. Young Vincent Freeman is born with a condition that would prevent him from space travel, yet is determined to infiltrate the GATTACA space program." 

Movie 2: "The Cheetah Girls: One World". Similarity score: 0.21330124631580724. <br>
Movie description: "Chanel, Dorinda, and Aqua, are off to India to star in a Bollywood movie. But when there they discover that they will have to compete against each other to get the role in the movie. Will the Cheetah's break up again?" 

Movie 3: "The Transporter Refueled". Similarity score: 0.21256302560184892. <br>
Movie description: "The fast-paced action movie is again set in the criminal underworld in France, where Frank Martin is known as The Transporter, because he is the best driver and mercenary money can buy. In this installment, he meets Anna and they attempt to take down a group of ruthless Russian human traffickers who also have kidnapped Frank’s father." 

Movie 4: "The Village". Similarity score: 0.17445331354748186. <br>
Movie description: "When a willful young man tries to venture beyond his sequestered Pennsylvania hamlet, his actions set off a chain of chilling incidents that will alter the community forever." 

Movie 5: "Deep Impact". Similarity score: 0.16773760137379393. <br>
Movie description: "A seven-mile-wide space rock is hurtling toward Earth, threatening to obliterate the planet. Now, it's up to the president of the United States to save the world. He appoints a tough-as-nails veteran astronaut to lead a joint American-Russian crew into space to destroy the comet before impact. Meanwhile, an enterprising reporter uses her smarts to uncover the scoop of the century." 

## Monthly Salary Expectation
My salary expectations are <span>&dollar;</span>30/hr, so this would be approximately (30/hr)(20hrs/week)(4.5weeks/month) = <span>&dollar;</span>2,700/month.