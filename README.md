# AI/Machine Learning Intern Challenge: Simple Content-Based Recommendation

## Dataset

The dataset is called "Popular Video Games 1980 - 2023", and it was found on Kaggle: https://www.kaggle.com/datasets/arnabchaki/popular-video-games-1980-2023. The dataset is already included in the repo as `games.csv`, so no additional steps are needed to load the dataset. 

## Setup

The setup required is included in the notebook. You only need to run the cell with the commented code that reads `!pip install numpy pandas nltk`. Be sure to uncomment the code first, then uncomment when the installation is finished.

## Running

Open the notebook `video_game_recommender.ipynb` and run the cells in order. Once you have reached the code block where it asks for a user query, feel free to re-run it to try out multiple queries. 

## Results

The query output is a list of five names of games. For example, if the query is `I like games with action, adventure, and strategy.`, the output is `['Death Stranding 2', 'Bloodborne PSX', '13 Sentinels: Aegis Rim', 'Super Smash Bros. for Wii U', 'Shovel Knight']`. 