# AI/ML Intern Challenge: Content-Based Recommendation System

## Overview
This project implements a simple content-based recommendation system that suggests movies based on a user's textual input. It utilizes TF-IDF vectorization and cosine similarity to find the most relevant matches from a dataset.

---

## Dataset
- The dataset used is **IMDB Dataset.csv**, which contains a list of movies along with their descriptions.
- The dataset was provided as part of this challenge.
- **Dataset link**: [Movie Plot Dataset on Kaggle](https://www.kaggle.com/datasets/ruchi798/movies-on-netflix-prime-video-hulu-and-disney)
- **Steps to load the dataset**:
  - Ensure the file `wiki_movie_plots_deduped.csv` is present in the project directory.
  - The script automatically reads the CSV file using pandas.

---

## Setup
### Prerequisites
- Python **3.8+**
- Virtual environment (optional but recommended)

### Installation Steps
1. Clone the repository:
   ```sh
   git clone <repo-url>
   cd <repo-folder>
   ```
2. Create and activate a virtual environment (optional but recommended):
   ```sh
   python -m venv venv
   source venv/bin/activate  # macOS/Linux
   venv\Scripts\activate  # Windows
   ```
3. Install dependencies:
   ```sh
   pip3 install -r requirements.txt
   ```

---

## Running the Recommendation System
You can run the recommendation system in two ways:

### **Jupyter Notebook** (Recommended for easy visualization)
- Open Jupyter Notebook:
  ```sh
  jupyter notebook
  ```
- Open `recommendation.ipynb` and run all cells.

- The system will output the top 3-5 recommended movies based on the input description.

---

## Results Example
### **Input Query:**
```sh
"Romance movies with comedy"
```

### **Output (Top 3 Recommendations):**
```
Recommended movies: ['Min & Max', 'I Was a Teenage Zombie', 'The Boy Friend', 'A Saloon Wet with Beautiful Women', 'Yellow Sands']
```

---

## Demo Video

- Link to the video - https://drive.google.com/file/d/1pjcnwxMFlVtTBFUUnuPk_9Spva4Uw5jY/view