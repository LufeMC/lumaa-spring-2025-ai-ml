# News Category Dataset Analysis

## Overview

This project analyzes and processes the **News Category Dataset** from Kaggle. The dataset consists of news articles categorized into different topics. The notebook includes data preprocessing, vectorization, and a recommendation system.

## Video Demo
[![Watch the demo video](https://img.youtube.com/vi/IM1ZOGOwegQ/0.jpg)](https://www.youtube.com/watch?v=IM1ZOGOwegQ)



## Dataset

- **Source:** [News Category Dataset](https://www.kaggle.com/rmisra/news-category-dataset)
- **Format:** JSON
- **Contains:** News headlines, short descriptions, category labels, and more

## Features

- Downloads the dataset using `kagglehub`
- Converts JSON data into a Pandas DataFrame
- Vectorizes textual data for processing
- Implements a news recommender function

## Installation

1. Clone the repository:
   ```sh
   git clone https://github.com/yourusername/your-repo.git
   cd your-repo
   ```
2. Install dependencies:
   ```sh
   pip install -r requirements.txt
   ```
3. Ensure you have Kaggle API access set up to download the dataset.

## Dependencies

- Python 3.x
- Pandas
- NumPy
- Kaggle API


## Usage

Run the Jupyter Notebook:

```sh
jupyter notebook solution.ipynb
```

## Results

Below is an example output of the news recommender system:

### Query:
**"Health benefits of green tea"**

### Recommended Articles:

#### 1. Tea Health Benefits: 8 Ways It Could Benefit Our Bodies
- **Description:** A cup of tea anyone? It could do wonders for your health. A lot of research has focused on green tea in particular, Health.com
- **Similarity Score:** 0.7115
- **[Read More](https://www.huffingtonpost.com/entry/tea-health-benefits-cancer-heart-disease_us_5b9c2e55e4b03a1dcc7ce60b)

#### 2. Green Tea Benefits: How The Drink Improves Your Health
- **Description:** While experts agree that more research is still needed, this only adds to the body of work linking green tea to healthy, happy.
- **Similarity Score:** 0.6392
- **[Read More](https://www.huffingtonpost.com/entry/green-tea-benefits-health_us_5b9c6ec9e4b03a1dcc7e965a)

#### 3. Green Tea Could Help Functioning In Old Age: Study
- **Description:** Green tea has long been eyed for possible health benefits, including its potential to decrease the risk of certain cancers.
- **Similarity Score:** 0.6156
- **[Read More](https://www.huffingtonpost.com/entry/green-tea-functioning-old-age_us_5b9b4994e4b03a1dcc765816)

#### 4. 6 Amazing Benefits of Tea
- **Description:** For those that have not yet embraced a tea-drinking habit, it's never too late to start brewing a batch! Explore the various types, flavors, and brands to find your tea-mate.
- **Similarity Score:** 0.4471
- **[Read More](https://www.huffingtonpost.com/entry/tea-health-benefits_us_5b9d4d2be4b03a1dcc866e19)

#### 5. Will And Kate Anniversary: Tetley Tea Gives Away A Year's Supply Of Tea
- **Description:** To get 12 full-size boxes of different varieties of the tea including Classic Blend, Pure Green, Iced Tea blend and of course.
- **Similarity Score:** 0.4450
- **[Read More](https://www.huffingtonpost.com/entry/will-and-kate-anniversary_us_5b9ba2a3e4b03a1dcc79328e)




## Desired compensation
4500 USD/month

## Contact
Email ID - ggandhikumar@ucsd.edu

