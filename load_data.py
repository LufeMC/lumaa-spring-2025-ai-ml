import pandas as pd

def load_dataset(filepath="movies.csv"):
    """
    Loads the dataset from a CSV file and returns a DataFrame.
    """
    df = pd.read_csv(filepath)
    return df

if __name__ == "__main__":
    df = load_dataset()
    print(df.head())  # Check if the data is loaded correctly

