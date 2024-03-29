from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# let's assume we have the following data
movies = ["The Dark Knight", "Dunkirk", "Interstellar", "Inception"]
movie_descriptions = [
    "Action, Crime, Drama",
    "Action, Drama, History",
    "Adventure, Drama, Sci-Fi",
    "Action, Adventure, Sci-Fi"
] 

# count vectorizer
vectorizer = CountVectorizer().fit_transform(movie_descriptions)
vectors = vectorizer.toarray()

# cosine similarity
csim = cosine_similarity(vectors)

# get the title of the movie that the user has watched
user_movie = "The Dark Knight"

# get the index of this movie from the movies list
movie_index = movies.index(user_movie)

# get a list of cosine similarity scores for this movie with all other movies
scores = list(enumerate(csim[movie_index]))

# sort the list of scores in descending order
sorted_scores = sorted(scores, key=lambda x:x[1], reverse=True)

# get the top 3 most similar movies
recommended_movies = sorted_scores[1:4]

# print out the recommended movies
for movie in recommended_movies:
    print(movies[movie[0]])

