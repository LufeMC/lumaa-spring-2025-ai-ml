# Movie Recommendation System

## Dataset

- The dataset is sourced from Kaggle:  
  [Wikipedia Movie Plots](https://www.kaggle.com/datasets/jrobischon/wikipedia-movie-plots/data)
- A subset of 500 movies is generated from the full dataset using `data/generate_subset.py`.
- The subset is stored as `data/movie_plots_subset.csv` and is automatically used when running the recommendation system.

### Generating the Subset (if needed)
To create a smaller dataset from the full dataset:
```bash
python data/generate_subset.py
```

## Setup

### Python Environment

- **Python Version**: `3.10.15`
- **Set up virtual environment using pyenv:**
  ```bash
  pyenv virtualenv 3.10.15 lumaa
  pyenv activate lumaa
  ```
- **Alternatively, using venv:**
  ```bash
  python3 -m venv venv
  source venv/bin/activate  # Linux/Mac
  venv\Scripts\activate     # Windows
  ```
- **Install dependencies:**
  ```bash
  pip install -r requirements.txt
  ```

## Running

To run the recommendation system using Jupyter Notebook from the command line:
```bash
jupyter notebook
```
Then open `solution.ipynb` and execute the cells step by step.

## Results

### Example Queries in the unit test and Outputs:

🔹 **Basic Query**

➡ Query: `I like action movies set in space`

🔽 **Top Recommendations:**

      1. The Doomsday Machine (Recommendation Score: 36.37/100)
      2. Kaizoku Sentai Gokaiger vs. Space Sheriff Gavan: The Movie (Recommendation Score: 34.27/100)

--------------------------------------------------

🔹 **Short Query**

➡ Query: `Action movie`

🔽 **Top Recommendations:**

      1. Fight Club – Members Only (Recommendation Score: 56.86/100)
      2. Gallowwalkers (Recommendation Score: 51.30/100)
      3. Speedway Junky (Recommendation Score: 48.81/100)
      4. Anjathe (Recommendation Score: 47.72/100)
      5. Gopi Kishan (Recommendation Score: 47.11/100)

--------------------------------------------------

🔹 **Long Query**

➡ Query: `A detective solving a mystery in a dark and rainy city, filled with suspense, drama, and unexpected twists.`

🔽 **Top Recommendations:**

      1. The Bone Collector (Recommendation Score: 55.04/100)
      2. The Arnelo Affair (Recommendation Score: 52.46/100)
      3. Young and Innocent (Recommendation Score: 51.33/100)
      4. Striking Distance (Recommendation Score: 51.17/100)
      5. Romeo Is Bleeding (Recommendation Score: 51.02/100)

--------------------------------------------------

🔹 **Empty Query**

➡ Query: ``

🚫 **No recommendations available. Try a different query.**

--------------------------------------------------

🔹 **Irrelevant Query**

➡ Query: `asdfghjkl qwerty lorem ipsum blah blah`

🚫 **No recommendations available. Try a different query.**

--------------------------------------------------

✅ ~ ~ ~ All test cases completed! ~ ~ ~ ✅

The system recommends movies based on **BERT embeddings** and **cosine similarity**, ranking them from most to least relevant.

---

## Additional Information
- **Desired Salary**:
  - **Hourly**: $30 per hour
  - **Monthly**: $2,400 per month
  - **Availability**: ~20 hours per week
- **LinkedIn Profile**: 
  - [Keita Katsumi](https://www.linkedin.com/in/keita-katsumi-a4a639244/)

