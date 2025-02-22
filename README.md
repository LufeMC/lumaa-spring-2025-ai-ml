# Content-Based Movie Recommendation System

## Dataset

This project uses the **Wikipedia Movie Plots dataset** from Kaggle:  
[Wikipedia Movie Plots Dataset](https://www.kaggle.com/datasets/jrobischon/wikipedia-movie-plots?resource=download)

Since the original dataset is quite large, for simplicity, I have randomly selected **500 movies** to create a smaller dataset for this recommendation system.

---

## Setup

- No `requirements.txt` is needed.
- The project is implemented in a **Jupyter Notebook (`.ipynb`)**.
- You can run the notebook directly on **Google Colab** using the provided **Colab button** in the repository.
- The **first cell in the notebook** contains a piece of code that will **automatically import the dataset** from the repository when executed.
- The **second cell in the notebook** contains a piece of code that will **automatically import the dependencies** required.

---

## Running the Code

1. Open the Jupyter Notebook (`.ipynb`) in **Google Colab** using the provided button.
2. Run the **first cell** to import the dataset.
3. Execute all cells in sequence to run the recommendation system.
4. Provide a **movie-related query** (e.g., *"I love thrilling action movies set in space"*).
5. The system will return the **top 5 recommended movies** based on text similarity.

---

## Example Output

### **Query**:
```plaintext
I love thrilling action movies set in space, with a comedic twist.
```
### **Top 5 Recommended Movies**:

| Rank | Title                  | Similarity Score |
|------|------------------------|-----------------|
| 1    | What Love Is	         | 0.438784           |
| 2    | Get Over It	      | 0.417528           |
| 3    | Bedtime Stories	 | 0.411893          |
| 4    | Aloha           | 0.385455           |
| 5    | Superman: Unbound	        | 0.385011           |

## Demo
A video demonstration of the recommendation system is available in [demo.md](demo.md).

## Salary Expectation:
I am looking for $20–25 per hour, but my primary goal is to gain valuable learning experience. Salary is secondary, and I am open to accepting the minimum offered, as long as I have the opportunity to grow and contribute effectively.
