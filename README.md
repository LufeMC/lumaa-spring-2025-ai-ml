# 🎬 AI/Machine Learning Intern Challenge: Simple Content-Based Recommendation

This project implements a **content-based recommendation system** that suggests movies based on a user-provided text description. It uses **sentence embeddings (SBERT) and cosine similarity** to find the most relevant movies from a dataset of 10,000 popular films.


## **🚀 How It Works**
1. **User Input**: The user provides a short text description of their movie preferences and the number of recommendations **N** they want.
2. **Text Preprocessing**: The dataset's movie overviews and user input are preprocessed (punctuation removal, tokenization, stopword removal, lemmatization).
3. **Sentence Embeddings**: The processed text is converted into **SBERT embeddings** using **SentenceTransformers**.
4. **Similarity Computation**: The **cosine similarity** between the user’s query and each movie in the dataset is computed.
5. **Hybrid Ranking**: The system ranks movies based on a combination of **text similarity and popularity (vote average)**.
6. **Top Recommendations**: The system returns the **top N** most relevant movies.


## 📂 Dataset
The dataset used is **TMDb Top 10,000 Popular Movies**, sourced from Kaggle:  
🔗 [TMDb Dataset](https://www.kaggle.com/datasets/sankha1998/tmdb-top-10000-popular-movies-dataset).


## 🛠 Setup & Installation

### 1. Clone the Repository
To get started, clone the repository to your local machine using:

```bash
git clone https://github.com/urmidedhiacmu/lumaa-spring-2025-ai-ml
cd lumaa-spring-2025-ai-ml
```

### 2. Create a virtual environment
It is recommended to use a virtual environment to keep dependencies isolated.
- For macOS/Linux:

   ```
   python3 -m venv <env_name>
   source rec_env/bin/activate
   ```
- For Windows (PowerShell):

   ```
   python -m venv <env_name>
   rec_env\Scripts\activate
   ```

### 3. Install Dependencies
- Ensure you have **Python 3.10** installed. Install all required dependencies using:

   ```bash
   pip install -r requirements.txt
   ```


### 4. Set up the Kernel
- Set up your kernel for Jupyter using:

   ```bash
   python -m ipykernel install --user --name <env_name> --display-name "<Python (env_name)>"
   ```

### 5. Run the Recommendation System  
- You can use the **Jupyter Notebook** to run the recommendation system using:

   ```bash
   jupyter notebook
   ```
- Open the file `Recommendation_System.ipynb` 
- Select your Python kernel from the top right
- Follow the steps given in the notebook :)

## 📊 Example Input and Output
### Input:
![Demo Image](Input.png "Input")

### Output:
![Demo Image](Output.png "Output")

## 🎥 Demo  
A short screen recording demonstrating the recommendation system can be found here:  
[📹 Demo Video](https://drive.google.com/file/d/1XVGG6QJxW7CaY2ImjF2fz5dmVDkw6Mwp/view?usp=sharing)

## 💼 Salary Expectation
Expected Monthly Salary: **$10k-$12k**

## 📝 Author Information
- Name: Urmi Dedhia
- Email: udedhia@andrew.cmu.edu
- LinkedIn: linkedin.com/in/urmidedhia