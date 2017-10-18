    import pandas as pd

    movie = pd.read_csv('movies.csv')

    movie_pivot = movie.pivot_table(index='userId', columns='movieId', values='rating')

    movie_pivot.to_csv('movies_pivot.csv')
