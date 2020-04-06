def can_two_movies_fill_flight(movie_lengths, flight_length):
    # initialize movie_lengths_dict to empty dictionary
    movie_lengths_dict = {}

    # loop through movie in movie_lengths
    for movie in movie_lengths:
        # if flight_length minus movie is in movie_lengths_dict
        if flight_length - movie in movie_lengths_dict:
            # return True
            return True

        # add movie to the movie_lengths_dict and set its value to True
        movie_lengths_dict[movie] = True

    # return False
    return False
