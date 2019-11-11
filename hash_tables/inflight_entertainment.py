def inflight_entertainment(flight_length, movie_lengths):
    # initialize a variable movies to an empty dictionary
    movies = {}
    # loop through movie_lengths
    for movie in movie_lengths:
        # check to see if flight_length minus the current movie is in the movies
        if flight_length - movie in movies:
            # if it is, return True
            return True
        # otherwise, add the current movie to movies as a key value pair
        else:
            movies[movie] = movie

    # return False if no match is found
    return False
