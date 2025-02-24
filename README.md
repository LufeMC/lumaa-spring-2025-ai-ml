# BBC News Recommendation System

This project implements a content-based recommendation system using the BBC News dataset. The system suggests news articles to users based on their descriptions, categories, and similarity scores.

## Introduction
Recommender systems are vital in filtering vast amounts of information to provide users with personalized content. This project implements a content-based approach to recommend news articles from the BBC News dataset by analyzing their descriptions and matching them to user-provided input.

## Dataset

The dataset used is the BBC News dataset, download from [Kaggle](https://www.kaggle.com/datasets/hgultekin/bbcnewsarchive). Save it as `bbc-news-data.csv` in the root directory. For this demonstration, I randomly sampled 500 articles to improve efficiency.

The dataset consists of BBC News articles categorized into topics such as:

* business
* entertainment
* politics
* sport
* tech
  
Each entry includes:

* title: The News headline.
* content: The content of the News.
* category: The News' topic classification.


## Setup

* Python 3.8+
* Jupyter Notebook

## Methodology


The recommendation process involves:

1. Data Loading: Reading and preprocessing the dataset.
2. TF-IDF Vectorization: Converting article descriptions into numerical representations.
3. Cosine Similarity Calculation: Measuring the similarity between user input and article descriptions.
4. Recommendation Generation: Ranking and displaying the top 5 similar articles.



## Example Usage and Output (within the Notebook)



- User Query: "current political events in the UK"
  
- Output:
  ```
  Top 5 Recommended News:

    -> online games play with politics
    Category: tech
    Similarity Score: 0.225
    Preview:  after bubbling under for some time, online games broke through onto the political arena in 2004.  the us presidential election provided a showcase for many, aimed at talking directly to a generation ...

    -> holmes starts 2005 with gb events
    Category: sport
    Similarity Score: 0.159
    Preview:  kelly holmes will start 2005 with a series of races in britain.  holmes will make her first track appearance on home soil since winning double olympic gold in january's norwich union international in...

    -> 'debate needed' on donations cap
    Category: politics
    Similarity Score: 0.108
    Preview:  a cap on donations to political parties should not be introduced yet, the elections watchdog has said.  fears that big donors can buy political favours have sparked calls for a limit. in a new report...

    -> uk firms 'embracing e-commerce'
    Category: politics
    Similarity Score: 0.097
    Preview:  uk firms are embracing internet trading opportunities as never before, e-commerce minister mike o'brien says.  a government-commissioned study ranked the uk third in its world index of use of informa...

    -> navratilova hits out at critics
    Category: sport
    Similarity Score: 0.094
    Preview:  martina navratilova has defended her decision to prolong her tennis career at the age of 48.  navratilova, who made a comeback after retiring in 1994, will play doubles and mixed doubles events in 20...
  ```


## Video Demo 

[BBC_news_demo](https://drive.google.com/file/d/1rVnphDbbZECCqJ2Hx3eoN_pSgqc0oz6I/view?usp=sharing)


## Salary expectation per month

My salary expectation is $2500-3000 / month.

