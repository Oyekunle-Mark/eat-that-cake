def inflight_entertainment(movie_lengths, flight_length):
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


print(inflight_entertainment([2, 4], 1))  # False
print(inflight_entertainment([2, 4], 6))  # True
print(inflight_entertainment([3, 8], 6))  # False
print(inflight_entertainment([3, 8, 3], 6))  # True
print(inflight_entertainment([1, 2, 3, 4, 5, 6], 7))  # True
print(inflight_entertainment([4, 3, 2], 5))  # True
print(inflight_entertainment([6], 6))  # False
print(inflight_entertainment([], 2))  # False
