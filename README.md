# **🎬 AI-Powered Movie Recommendation System**

## **🌟 Introduction**
This project implements a content-based movie recommendation system that suggests movies based on user input describing their preferences. The system utilizes TF-IDF vectorization and cosine similarity to find the best matches based on movie descriptions. It applies filtering to ensure high-quality recommendations and prioritizes genre relevance.

---

## **📊 Dataset**
The dataset is a randomly sampled subset (300 movies) from a public IMDB movie database, ensuring diversity and randomness for machine learning training. It includes:
✔ Titles  
✔ Overviews (plot summaries)  
✔ Genres  
✔ Popularity scores  
✔ Ratings  

- **Source**: [IMDB Movies Dataset](https://www.kaggle.com/code/padmanabhanporaiyar/imdb-movies-all-types-of-recommender-system/input?select=movies_metadata.csv)  
- The sampled dataset (`movies_metadata_sampled_for_test.csv`) must be placed in the project directory for proper execution.  

---

## **🛠️ How It Works**
🔹 **Data Preprocessing**: Cleans and normalizes movie descriptions and genre data.  
🔹 **TF-IDF Vectorization**: Converts text-based data into numerical representations.  
🔹 **Cosine Similarity Calculation**: Measures the similarity between the user’s query and movie descriptions.  
🔹 **Recommendation Filtering**: Returns the **top 5 relevant movies**, excluding those with similarity scores below 0.05.  
🔹 **Genre Matching**: Prioritizes recommendations that match the genre extracted from the user's input.  

---

## **⚙️ Setup Instructions**
### **1️⃣ Python Version**
- The system requires **Python 3.8+**. Using a **virtual environment** is recommended.  

### **2️⃣ Install Dependencies**
Run the following command to install the required libraries:
```bash
pip install -r requirements.txt
```

---

## **🚀 Running the Recommendation System**
You can run the system using **Python script or Jupyter Notebook**:

### **1️⃣ Running as a Python Script**
Execute the following command in the terminal:
```bash
python recommend.py
```
Enter a **movie preference description** when prompted.  

### **2️⃣ Running in Jupyter Notebook**
- Open the `.ipynb` file in **Jupyter Notebook**.  
- Run all cells in order.  
- Provide a movie preference description when prompted.  

---

## **🎯 Example Query & Results**
For a user query like:
```text
"I love romantic movies with humor."
```
The system returns the **top 5 movie recommendations**:

```
Top recommended movies:
                              title  vote_average genres_cleaned  similarity
                          Dreamboat           7.0         Comedy    0.15
                        Bon appétit           5.3        Romance    0.14
      Walking the Streets of Moscow           7.0 Romance Comedy    0.13
Tig Notaro: Boyish Girl Interrupted           6.3         Comedy    0.10
                The Transfiguration           6.1   Horror Drama    0.09
```
Movies with **similarity < 0.05** are automatically filtered out.

---

## **🛠️ Improvements & Fixes**
### **Identified Issues & Fixes**
1. **Genre Matching Was Not Strict Enough**
   - Before: Recommendations contained either romance or comedy, not both.
   - Fix: The system now ensures both genres are included in the recommended movies.

2. **Word Standardization Issue (Romantic vs. Romance)**
   - Before: The system failed to recognize "romantic" as "romance."
   - Fix: Implemented lemmatization to standardize genre-related words.

3. **Weak Similarity Threshold Allowed Irrelevant Matches**
   - Before: Low similarity scores resulted in unrelated recommendations.
   - Fix: Increased the minimum similarity threshold to 0.05, improving recommendation quality.

---

## **📝 Deliverables**
✅ Forked GitHub Repository with complete implementation.  
✅ Jupyter Notebook (`.ipynb`) for execution.  
✅ `README.md` (this file) with setup and instructions.  
✅ Short Demo Video demonstrating system execution.([https://drive.google.com/drive/my-drive?dmr=1&ec=wgc-drive-globalnav-goto](https://drive.google.com/file/d/1cLc02_5_F5bT5_IPoKna_LKv_2SgLcCv/view?usp=sharing))
✅ Implementation using TF-IDF + Cosine Similarity for recommendation generation.  

This recommendation system is **simple, efficient, and provides accurate movie suggestions** based on **user text input preferences**. 🎬✨
