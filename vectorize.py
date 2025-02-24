from sklearn.feature_extraction.text import TfidfVectorizer

def vectorize_texts(texts):
    """
    Converts a list of text descriptions into TF-IDF vectors.
    """
    vectorizer = TfidfVectorizer(stop_words="english")
    tfidf_matrix = vectorizer.fit_transform(texts)
    return vectorizer, tfidf_matrix

