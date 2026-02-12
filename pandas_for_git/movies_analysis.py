import pandas as pd

# ============================================================
# 0. Display configuration
# ============================================================
pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)


# ============================================================
# 1. Load dataset & basic inspection
# ============================================================
movie_rat = pd.read_csv(
    "D:\\IMDBTop100.csv",
    index_col="Unnamed: 0"
)

movie_rat.index.name = "Rank"

print("HEAD:")
print(movie_rat.head())
print("\nINFO:")
print(movie_rat.info())
print("\nSHAPE:", movie_rat.shape)
print("\nDESCRIBE:")
print(movie_rat.describe())
print("\nCOLUMNS:")
print(movie_rat.columns)
print("\nANY NULLS?")
print(movie_rat.isna().any().any())

# ============================================================
# 2. Rating extremes & averages
# ============================================================
high_rating_movie = movie_rat[['Title', 'Rating']].sort_values(
    'Rating', ascending=False
)
print("\nTop Rated Movies:")
print(high_rating_movie.head(10))

lowest_rating_movie = movie_rat[['Title', 'Rating']].sort_values(
    'Rating', ascending=True
)
print("\nLowest Rated Movies:")
print(lowest_rating_movie.head(10))

avg_rating = movie_rat['Rating'].mean()
print(f"\nAverage Rating: {avg_rating:.2f}")

# ============================================================
# 3. Genre-wise rating statistics (Genre1)
# ============================================================
avg_rating_by_genre = (
    movie_rat
    .groupby('Genre1')
    .agg(avg_rating=('Rating', 'mean'))
    .sort_values('avg_rating', ascending=False)
)
print("\nAverage Rating by Genre:")
print(avg_rating_by_genre)

max_rating_by_genre = movie_rat.groupby('Genre1')['Rating'].max()
min_rating_by_genre = movie_rat.groupby('Genre1')['Rating'].min()

print("\nMax Rating by Genre:")
print(max_rating_by_genre)
print("\nMin Rating by Genre:")
print(min_rating_by_genre)

# ============================================================
# 4. Votes cleaning & popularity
# ============================================================
movie_rat['VotesIMDB'] = (
    movie_rat['VotesIMDB']
    .astype(str)
    .str.replace(',', '', regex=False)
    .astype(float)
)

max_votes_movie = movie_rat[['Title', 'VotesIMDB']].sort_values(
    'VotesIMDB', ascending=False
)
print("\nMost Voted Movies:")
print(max_votes_movie.head(10))

# ============================================================
# 5. Rating vs votes (quality vs popularity)
# ============================================================
high_rating_vs_high_votes = (
    movie_rat
    .groupby('Genre1')
    .agg(
        total_votes=('VotesIMDB', 'sum'),
        avg_rating=('Rating', 'mean')
    )
    .sort_values('total_votes', ascending=False)
)

print("\nGenre: Total Votes vs Avg Rating")
print(high_rating_vs_high_votes)

# ============================================================
# 6. MetaCritic vs IMDb rating segmentation
# ============================================================
rating_metacritic = movie_rat.groupby('Genre1').agg(
    avg_rating=('Rating', 'mean'),
    avg_metacritic=('MetaCritic', 'mean')
)

high_rating = rating_metacritic['avg_rating'].quantile(0.75)
low_rating = rating_metacritic['avg_rating'].quantile(0.25)
high_mc = rating_metacritic['avg_metacritic'].quantile(0.75)
low_mc = rating_metacritic['avg_metacritic'].quantile(0.25)

elite_genres = rating_metacritic[
    (rating_metacritic['avg_rating'] >= high_rating) &
    (rating_metacritic['avg_metacritic'] >= high_mc)
]

print("\nElite Genres (High IMDb + High MetaCritic):")
print(elite_genres)

# ============================================================
# 7. Multi-genre handling
# ============================================================
movie_rat['multi_genre'] = (
    movie_rat[['Genre1', 'Genre2', 'Genre3']]
    .notna()
    .sum(axis=1) > 1
)

print("\nNumber of Multi-Genre Movies:")
print(movie_rat[movie_rat['multi_genre']].shape[0])

# ============================================================
# 8. Melt to long format (advanced Pandas)
# ============================================================
genre_long = movie_rat.melt(
    id_vars=['Rating'],
    value_vars=['Genre1', 'Genre2', 'Genre3'],
    var_name='GenrePosition',
    value_name='Genre'
)

genre_position_rating = (
    genre_long
    .dropna(subset=['Genre'])
    .groupby(['Genre', 'GenrePosition'])['Rating']
    .mean()
    .unstack()
    .sort_values(by='Genre1', ascending=False)
)

print("\nAverage Rating by Genre Position:")
print(genre_position_rating)

# ============================================================
# 9. Demographic vote cleaning
# ============================================================
vote_cols = ['VotesM','VotesF','VotesU18','Votes1829','Votes3044','Votes45A','VotesUS','VotesnUS']

for col in vote_cols:
    movie_rat[col] = (
        movie_rat[col]
        .astype(str)
        .str.replace(',', '', regex=False)
        .astype(float)
    )

print("\nDemographic vote columns cleaned.")

# ============================================================
# 10. Popularity & quantile-based segmentation
# ============================================================
q90 = movie_rat['VotesIMDB'].quantile(0.90)
q75 = movie_rat['VotesIMDB'].quantile(0.75)
q50 = movie_rat['VotesIMDB'].quantile(0.50)
q25 = movie_rat['VotesIMDB'].quantile(0.25)

movie_rat['elite_popular'] = (movie_rat['VotesIMDB'] >= q90).astype(int)
movie_rat['high_popular'] = ((movie_rat['VotesIMDB'] >= q75) & (movie_rat['VotesIMDB'] < q90)).astype(int)
movie_rat['above_median_popular'] = ((movie_rat['VotesIMDB'] >= q50) & (movie_rat['VotesIMDB'] < q75)).astype(int)
movie_rat['low_popular'] = (movie_rat['VotesIMDB'] <= q25).astype(int)

print("\nPopularity Segmentation Sample:")
print(movie_rat[['Title','VotesIMDB','elite_popular','high_popular','above_median_popular','low_popular']].head())

