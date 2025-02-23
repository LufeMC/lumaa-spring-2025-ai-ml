The dataset is on Kaggle. Unfortunately, due to the file size I am unable to upload the data file here.
You do have to have an account with Kaggle to download, but it is free to create an account and download.
The link to download the dataset:
https://www.kaggle.com/datasets/cryptexcode/mpst-movie-plot-synopses-with-tags?resource=download

Extract the zip file to access the csv file named "mpst_full_data.csv" within.

The python version used is 3.9.12, and I used a virtual environment in Jupyter Notebook to run the code.
To set up the virtual environment for Jupyter Notebook follow these instructions and run the following code in your terminal:

Step 1: (firstEnv is a placeholder name for your virtual environment)

conda create --name firstEnv

Step 2:

conda install -c anaconda ipykernel

Step 3:

python -m ipykernel install --user --name=firstEnv

Now you should be able to create a notebook within Jupyter Notebook that runs within your new environment.

Then, install dependencies by running:
pip install -r requirements.txt

When running the display_recommendations() function, simply type your movie preferences and it will print the top 5 matches 
         (unless you specify a different amount of movies within the function call).
