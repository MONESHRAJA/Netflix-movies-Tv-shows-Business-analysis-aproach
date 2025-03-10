import numpy as np
import matplotlib as plt
import seaborn as sbn
import pandas as pd
import pandas as pd

# Load dataset
file_path = "C:/Users/Monesh Raja/Downloads/netflix movies and tv series DATA (28th feb 2025).csv"

pj1 = pd.read_csv("C:/Users/Monesh Raja/Downloads/netflix movies and tv series DATA (28th feb 2025).csv")

# Drop rows where essential columns have missing values
pj1.dropna(subset=['title', 'genres', 'releaseYear', 'imdbAverageRating', 'imdbNumVotes'], inplace=True)

# Convert releaseYear to integer
pj1['releaseYear'] = pj1['releaseYear'].astype(int)

# Fill missing genres with "Unknown"
pj1['genres'].fillna("Unknown", inplace=True)

# Remove duplicates based on the title
pj1.drop_duplicates(subset=['title'], keep='first', inplace=True)

# Drop availableCountries column (too many missing values)
pj1.drop(columns=['availableCountries'], inplace=True)

# Reset index
pj1.reset_index(drop=True, inplace=True)

# Save cleaned data to a new file in the same directory
cleaned_file_path = "C:/Users/Monesh Raja/Downloads/cleaned_netflix_data.csv"
pj1.to_csv(cleaned_file_path, index=False)

print(f"Data Preprocessing Completed! Cleaned file saved at: {cleaned_file_path}")








