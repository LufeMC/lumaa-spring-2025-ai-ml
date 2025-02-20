# TV Show Recommendation System

## Dataset

The dataset used for this project is `titles.csv`. It contains information about various media titles, including TV shows and movies, along with their descriptions. you can find the dataset [here](https://drive.google.com/file/d/1qPcKC9_wvVmX7robdkVcmxKjm1oq8_i5/view?usp=sharing)

Filtering the data to have only 500 values affects the accuracy of the recommendation program so it is best to use the full dataset.

### Loading the Dataset

To load the dataset, the script reads `titles.csv` and filters and removes the NaN values in descriptions column. 

## Setup

### Python Version

This project is developed using **Python 3.8+**.

### Running in Google Colab

To run this code in Google Colab:
1. Upload the `titles.csv` file to Colab.
2. Install necessary dependencies using:
   ```python
   !pip install pandas
   !pip install numpy
   ```
3. Execute the notebook cells to run the recommendation system.

## Running the Code

To execute the recommendation system in Colab:

```python
!python recommend.py
```

It will prompt you to enter a description. Based on the input, it will return the top three matching TV shows or Movies.

If you want to continue type "yes".

## Results

For an input like:

```bash
Enter a description: Space Theme.
```

The output will be:

```
->(MOVIE)  Fukrey Boyzzz: Space Mein Fukrapanti : 0.3
->(MOVIE)  A StoryBots Space Adventure : 0.27
->(MOVIE)  The Wonderful: Stories from the Space Station : 0.26
```

## Salary Expectation

The expected salary for this role is **$20-$25 per hour**.


