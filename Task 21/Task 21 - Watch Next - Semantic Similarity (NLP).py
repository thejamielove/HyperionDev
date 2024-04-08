import spacy
nlp = spacy.load('en_core_web_md')

# Function to recommend movies based on similarity
def watch_next(planet_hulk):
    model_movie = nlp(planet_hulk)

    # Read the movie list from text file
    with open('movies.txt', 'r') as file:
        movies = file.readlines()

    # Calculate the similarity between 'planet_hulk' and each movie in the text file list
    similarities = [] # store similarity results in list
    for movie in movies:
        similarity = nlp(movie).similarity(model_movie)
        similarities.append((movie.strip(), similarity))

    # Sort the movies based on similarity in descending order
    similarities.sort(key = lambda movie_similarity : movie_similarity[1], reverse = True)

    # Get top 3 recommended movies
    recommended_movies = [movie[0] for movie in similarities[0:3]]

    return recommended_movies

planet_hulk = ''' Will he save
their world or destroy it? When the Hulk becomes too dangerous for the
Earth, the Illuminati trick Hulk into a shuttle and launch him into space to a
planet where the Hulk can live in peace. Unfortunately, Hulk lands on the
planet Sakaar where he is sold into slavery and trained as a gladiator.'''

# running function based on 'planet_hulk' description
recommended_movies = watch_next(planet_hulk)

# Print the top 3 recommended movies on separate lines
print("\nRecommended top 3 movies to watch based on Planet Hulk:\n")
print("\n \n".join(recommended_movies))