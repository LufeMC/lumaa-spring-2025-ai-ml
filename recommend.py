from sklearn.metrics.pairwise import cosine_similarity
from vectorize import vectorize_texts
from load_data import load_dataset

def recommend_items(user_input, top_n=5):
    """
    Recommends the top N items based on text similarity.
    """
    df = load_dataset()

    # Convert descriptions to numerical vectors
    vectorizer, tfidf_matrix = vectorize_texts(df["description"])

    # Convert user input to a vector
    user_vector = vectorizer.transform([user_input])

    # Compute cosine similarity
    similarities = cosine_similarity(user_vector, tfidf_matrix).flatten()

    # Get top N most similar items
    top_indices = similarities.argsort()[::-1][:top_n]

    # Return recommended items
    return df.iloc[top_indices][["title", "description"]]

if __name__ == "__main__":
    import sys
    user_query = sys.argv[1] if len(sys.argv) > 1 else "I love thrilling action movies set in space"
    recommendations = recommend_items(user_query)
    print("\nRecommended Movies:")
    print(recommendations)

