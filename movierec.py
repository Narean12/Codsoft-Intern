movies = {
    "Movie 1": ["Action", "Adventure", "Sci-Fi"],
    "Movie 2": ["Drama", "Romance"],
    "Movie 3": ["Action", "Comedy"],
    "Movie 4": ["Horror", "Thriller"],
    "Movie 5": ["Comedy", "Romance"],
}
user_preferences = {
    "Action": 5,
    "Adventure": 4,
    "Sci-Fi": 3,
    "Drama": 2,
    "Romance": 4,
    "Comedy": 3,
    "Horror": 1,
    "Thriller": 2,
}
def recommend_movies(user_preferences, movies):
    recommended_movies = {}
    
    for movie, genres in movies.items():
        score = 0
        for genre in genres:
            if genre in user_preferences:
                score += user_preferences[genre]
        recommended_movies[movie] = score
    sorted_recommendations = sorted(recommended_movies.items(), key=lambda x: x[1], reverse=True)
    return [movie[0] for movie in sorted_recommendations]
user_recommendations = recommend_movies(user_preferences, movies)
print("Recommended Movies for the User:")
for i, movie in enumerate(user_recommendations):
    print(f"{i + 1}. {movie}")
