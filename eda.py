import pandas as pd
import matplotlib.pyplot as plt

# Load Dataset
df = pd.read_csv("dataset/cleaned_netflix.csv")

# Dataset Shape
print("DATASET SHAPE")
print(df.shape)

# Descriptive Statistics
print("\nDESCRIPTIVE STATISTICS")
print(df.describe())

# Movies vs TV Shows
print("\nMOVIES VS TV SHOWS")
print(df['type'].value_counts())

# Movies vs TV Shows Chart
df['type'].value_counts().plot(kind='bar')
plt.title("Movies vs TV Shows")
plt.xlabel("Content Type")
plt.ylabel("Count")
plt.tight_layout()
plt.savefig("charts/movies_vs_tvshows.png")
plt.close()

# Top 10 Countries
top_countries = df['country'].value_counts().head(10)

print("\nTOP 10 COUNTRIES")
print(top_countries)

top_countries.plot(kind='bar')
plt.title("Top 10 Countries")
plt.xlabel("Country")
plt.ylabel("Count")
plt.tight_layout()
plt.savefig("charts/top_10_countries.png")
plt.close()

# Rating Distribution
ratings = df['rating'].value_counts().head(10)

print("\nRATING DISTRIBUTION")
print(ratings)

ratings.plot(kind='bar')
plt.title("Rating Distribution")
plt.xlabel("Rating")
plt.ylabel("Count")
plt.tight_layout()
plt.savefig("charts/rating_distribution.png")
plt.close()

# Release Year Distribution
df['release_year'].hist(bins=20)

plt.title("Release Year Distribution")
plt.xlabel("Release Year")
plt.ylabel("Number of Titles")
plt.tight_layout()
plt.savefig("charts/release_year_distribution.png")
plt.close()

print("\nALL CHARTS CREATED SUCCESSFULLY")