# AI/Machine Learning Intern Challenge: Simple Content-Based Recommendation

## Dataset

The dataset is from the Github repo of Brendan Martin. It is called IMDB-Movie-Data.csv and can be found through his Github page within articles then Python Pandas Tutorial A Complete Introduction for Beginners. The dataset can be loaded in through pandas.read_csv as shown in my notebook. A link to the dataset is also here: https://github.com/LearnDataSci/articles/blob/master/Python%20Pandas%20Tutorial%20A%20Complete%20Introduction%20for%20Beginners/IMDB-Movie-Data.csv

## Setup

This notebook was ran using Python 3.11.7

To use a virtual environment on a Mac, follow these instructions:

On your Mac, open Terminal and navigate to your project directory. Then, run the command python3 -m venv myenv to create a new virtual environment named "myenv". Once the environment is created, activate it by running source myenv/bin/activate. Your terminal prompt will update to show that you're working within the virtual environment, and any packages you install will be confined to this environment rather than your global Python installation. When you're finished working in the environment, simply type deactivate to exit.

To install dependencies, use the requirements.txt file. To install these dependencies, you can use the command `pip install -r requirements.txt`.

## Running
To run the code, click the "Run All" button at the top of the notebook. This will run all of the cells. If you'd like to change the user preference query, simply change the text in the user_preference variable (found in the code block below the heading "Recommend Top Movies").

## Results

The output for the system comes in the form of a printed dictionary value, showing title and then description. For example,
{'Title': 'Percy Jackson & the Olympians: The Lightning Thief', 'Description': "A teenager discovers he's the descendant of a Greek god and sets out on an adventure to settle an on-going battle between the gods."}.