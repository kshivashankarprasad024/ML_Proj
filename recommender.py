import csv

# Function to load movies from a CSV file
def load_movies():
    movies = []
    with open('HollywoodMovies.csv', 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            movies.append({
                "Film": row['Movie'],
                "Genre": row['Genre'],
                "Year": int(row['Year'])
            })
    return movies

# Load movies dataset
movies = load_movies()

# Get a list of all unique genres
def get_genres():
    return list(set(movie['Genre'] for movie in movies))

# Recommend movies based on genre with a fallback to ensure at least 10 recommendations
def recommend_movies_by_genre(genre, min_recommendations=10):
    genre = genre.lower()
    
    # Filter movies that match the selected genre
    genre_movies = [movie for movie in movies if movie['Genre'].lower() == genre]
    
    # If fewer than min_recommendations, include additional movies from other genres
    if len(genre_movies) < min_recommendations:
        other_movies = [movie for movie in movies if movie['Genre'].lower() != genre]
        genre_movies.extend(other_movies[:min_recommendations - len(genre_movies)])
    
    return genre_movies[:min_recommendations]

# Test the function
if __name__ == "__main__":
    print("Available Genres:")
    genres = get_genres()
    for i, genre in enumerate(genres, 1):
        print(f"{i}. {genre}")

    # Let the user choose a genre
    choice = int(input("Select a genre by number: ")) - 1
    if 0 <= choice < len(genres):
        selected_genre = genres[choice]
        print(f"\nRecommendations for genre: {selected_genre}")
        recommendations = recommend_movies_by_genre(selected_genre)
        if recommendations:
            print(f"\nHere are your recommendations (at least 10 movies):")
            for movie in recommendations:
                print(f" - {movie['Film']} ({movie['Year']}) [{movie['Genre']}]")
        else:
            print("No movies found for this genre.")
    else:
        print("Invalid choice. Please run the program again.")
