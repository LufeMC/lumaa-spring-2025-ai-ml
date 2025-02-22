import pandas as pd

# Load the full dataset
file_path = "data/wiki_movie_plots_deduped.csv"
df = pd.read_csv(file_path)

# Randomly sample 500 rows (without replacement for unique picks)
df_sampled = df.sample(n=500, random_state=42)

# Save the sampled dataset to a new CSV file
subset_path = "data/movie_plots_subset.csv"
df_sampled.to_csv(subset_path, index=False)

print(f"Successfully created a smaller dataset: {subset_path}")
print(f"Shape: {df_sampled.shape}")
print(df_sampled.head())  # Display first few rows