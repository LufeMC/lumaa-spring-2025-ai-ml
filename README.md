
# Simple Content-Based Recommendation System

This repository contains a basic content-based recommendation system. Given a short text description of a user’s preferences, the system suggests the most similar items (movies) from a small dataset.

---

## 1. Dataset

I use the **Movies Details** dataset from [Kaggle](https://www.kaggle.com/datasets/sachinkumar62/movies-details). It contains various movie information such as title, overview, and other metadata that help in constructing text-based similarity.

- **File**: `movies.csv`
- **Source**: [Kaggle - Movies Details](https://www.kaggle.com/datasets/sachinkumar62/movies-details)
---

## 2. Approach

1. **Text Vectorization**: I apply TF-IDF (Term Frequency–Inverse Document Frequency) to transform movie overviews into vectors.
2. **Cosine Similarity**: I compare the user’s input text vector against each movie’s vector to measure similarity.
3. **Top-N Recommendations**: I sort results by similarity and output the most relevant movies (e.g., top 5).

**Why Content-Based?**  
- It allows recommendations based purely on text data (e.g., overview, keywords), without requiring user–item interactions or ratings.

---

## 3. Repository Structure

- **recommendation.ipynb**  
  Jupyter Notebook with the entire workflow:
  - Data loading and cleaning
  - TF-IDF vectorization
  - Cosine similarity calculation
  - Recommendation function to output the top matches

- **movies.csv**  
  Dataset file containing movie information (title, overview, etc.).

- **README.md**  
  This file (instructions and documentation).

---

## 4. Setup and Dependencies

1. **Python version**: 3.8+ (tested on Python 3.9).
2. **Libraries**:
   - `pandas`
   - `math`
   - `re`

You can install these dependencies by running:
```
pip install -r requirements.txt
```

---

## 5. Running the Code

1. Clone or download this repository.
2. Place `movies.csv` in the same folder (or update paths in `recommendation.ipynb` if needed).
3. Open `recommendation.ipynb` in Jupyter (e.g., `jupyter notebook recommendation.ipynb`).
4. Run the cells in order:
   - **Data Loading**: Reads the CSV.
   - **Preprocessing & Vectorization**: Transforms text into TF-IDF vectors.
   - **Similarity Computation**: Sets up cosine similarity.
   - **Recommendation**: Provide an input description (e.g. `"I love action movies set in space"`) and get the top recommended movies.


---

## 6. Example Usage

**User Input**:
```
"I like action movies set in space"
```

**System Output**
```
User Input: 'I like action movies set in space'

Recommended Movies:
Captain Fantastic (Similarity: 0.2219)
space pirate captain harlock and his fearless crew face off against the space invaders who seek to conquer the planet earth.

A Clockwork Orange (Similarity: 0.1385)
4 would be astronauts spend 400 days in a land locked space simulator to test the psychological effects of deep space travel but, when something goes terribly wrong and they are forced to leave the simulation, they discover that everything on earth has changed. is this real or is the simulation on a higher level than they could have ever imagined?

Mulan (Similarity: 0.1306)
a faithful wife takes action when it becomes clear to her that her devious husband has betrayed her.

The Night of the Hunter (Similarity: 0.1254)
a chronicle of the original mercury astronauts in the formation of america's space program: alan shepherd, the first american in space; gus grissom, the benighted astronaut for whom nothing works out as planned; john glenn, the straight-arrow 'boy scout' of the bunch who was the first american to orbit the earth; and the remaining pilots: deke slayton, scott carpenter and wally schirra.

Citizen Kane (Similarity: 0.1074)
joe, a young american soldier, is hit by a mortar shell on the last day of world war i. he lies in a hospital bed with a fate worse than death as a quadruple amputee who has lost his arms, legs, eyes, ears, mouth and nose. unbeknown to his doctors, he remains conscious and able to think, thereby reliving his life through strange dreams and memories.

```
(The exact titles and similarity scores will depend on how you process the data.)

---

## 7. Salary Expectation

I’m available for 25 hours of work each week at $25/hour, translating to $2500 per month.


---

## 8. Demo

Here is my demo video: 
---


**Thank you** for reviewing my submission! 