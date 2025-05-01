import pandas as pd

# Column names for the dataset
column_names = ["user_id", "movie_id", "rating", "timestamp"]

# Load the data from GroupLens
# This is has user, movie, rating, and timestamp
ratings = pd.read_csv(
    "http://files.grouplens.org/datasets/movielens/ml-100k/u.data",
    sep="\t",
    names=column_names
)

print(ratings.head())

ratings.to_csv("movielens_ratings.csv", sep="\t", index=False)
