import nltk
import pandas as pd
import re
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer

nltk.download('stopwords')
nltk.download('punkt')
nltk.download('wordnet')

#Adds preprocess function that preprocesses text data
def preprocess_text(text):
    text = text.lower() #Makes Lowercase
    text = re.sub(r'[^\w\s]', '', text) #Replaces punctuation/special characters
    tokens = nltk.word_tokenize(text)
    lemmatizer = WordNetLemmatizer()
    cleaned_text = [lemmatizer.lemmatize(word) for word in tokens if word not in stopwords.words('english')] #Removes stop words/Changes words to base form

    cleaned_text = ' '.join(cleaned_text)

    return cleaned_text

#Loads Data so can be accessed in other scripts
def load_data():
    data = pd.read_csv('../movie_dataset.csv', index_col=0) #Loads dataset in
    data = data[['title','overview','genres', 'keywords']] #Creates new Dataframe from dataset
    data = data.dropna() #Removes Null Values
    data = data.iloc[0:400] #Selects first 400 rows to train on

    #Processes Data
    data['overview'] = data['overview'].apply(preprocess_text)
    data['keywords'] = data['keywords'].apply(preprocess_text)
    data['genres'] = data['genres'].apply(preprocess_text)

    return data


"""

What does preprocessed_text() do?

The function is meant to process text data by:
    
    1. Lower casing text
    2. Removing punctuation/special characters
    3. Lemmatizing text (setting words to base form | ex. stopping -> stop)
    4. Removing stopwords (removing meaningless words | ex. a, an, the, in



What does load_data() do?

This function formats the data and applies preprocessing to the data.
Another main function is to provide access to the preprocessed data across Python scripts.

"""