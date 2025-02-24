# AI/Machine Learning Intern Challenge: Simple Content-Based Recommendation

**Deadline**: Sunday, Feb 23th 11:59 pm PST

---

# 🎬 Content-Based Movie Recommendation System  

## 📌 Overview  
This project implements a **content-based recommendation system** that suggests movies based on a user's short text description of their preferences. The system uses **TF-IDF vectorization** and **cosine similarity** to compare the user's query with movie overviews and return the most relevant recommendations.  

## 📊 Dataset  
- The dataset consists of movies with their **overviews (descriptions)**.  
- **Source**: A small **public dataset** (100–500 movies) that includes movie titles and plot summaries.  
- The dataset is included in this repository as **`[movies_metadata.csv](Data link='https://drive.google.com/file/d/1IAifkLYGrkllrK9c7WHDl9gaAo-3eY6x/view?usp=drive_link')`** . connect to drive in colab and copy the file path and replace it with your own in the code file.

## ⚙️ Approach  
1. **Preprocessing:** Clean and normalize the text (lowercasing, removing special characters, stopwords, and lemmatization).  
2. **TF-IDF Vectorization:** Convert movie overviews and user query into TF-IDF vectors.  
3. **Cosine Similarity:** Measure the similarity between the user query and all movie descriptions.  
4. **Recommendation:** Return the **top 3–5 most similar** movies.  

## 🛠️ Setup Instructions  

### **1️⃣ Install Dependencies**  
Since this project is implemented in a **Jupyter Notebook (`.ipynb`)**, install the required libraries directly using the following command in a new cell:  
```python
!pip install pandas numpy scikit-learn nltk
```

### **2️⃣ Run the Notebook**  
- Open **Jupyter Notebook**.  
- Load and run all cells sequentially.  
- Enter a movie preference query when prompted.  

### **3️⃣ Example Query & Output**  
#### **User Input:**  
```plaintext
"I love thrilling action movies set in space, with a comedic twist."
```

#### **Expected Output:**  
```
Top 5 Recommended Movies:
1. Guardians of the Galaxy (Similarity: 0.82)
2. Star Wars: A New Hope (Similarity: 0.76)
3. Thor: Ragnarok (Similarity: 0.72)
4. The Fifth Element (Similarity: 0.68)
5. Serenity (Similarity: 0.65)
```

[📽️ Short Video Demo](https://www.awesomescreenshot.com/video/36753966?key=212b0d94b1fec99f2cc056b6c0e1e74b) 

## 💰 Salary Expectation per Month  
20-30$/hr for the internship  

## 📝 Deliverables  
✅ **Forked GitHub Repository** with the full implementation.  
✅ **Jupyter Notebook (`.ipynb`)** for implementation.  
✅ **README.md** (this file).  
✅ **Short Video Demo** demonstrating how the system runs.  
✅ **Implementation of the recommendation system** using TF-IDF + cosine similarity.  
