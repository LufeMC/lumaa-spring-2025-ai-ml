Hi I'm Saba Abdulaziz, 1st year MSCS student at CMU. <br />
**Dataset:** Wikipedia Movie Plots from Kaggle, will be directly downloaded in the notebook. <br />
**Running:** directly in the notebook. <br />
**Results:** text = "I love thrilling action movies set in space, with a comedic twist.", recommendation: 1. A Modern Musketeer
2. Love, Loot and Crash
3. Caught in the Rain

**Basic algorithm:** <br />
convert the dataset to embeddings through open_ai api, then compare the user input embedding with this dataset and return the k highest scores as a few shots to the model. <br />
