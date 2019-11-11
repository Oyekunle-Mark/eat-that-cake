def reverse_by_characters(word, left=None, right=None):
    # check if left and right is None
        # set the left_index to 0
        # set the right_index to the length of word
    # loop while left_index is less than right_index
        # swap character at index left_index with character
        # at index right index
        # increment left_index
        # decrement right_index
    pass


def find_words_positions(words):
    # set the left_index to 0
    # set the right_index to 0
    # initialize positions to empty list
    # loop through words
        # if current character is not an empty string, increment right index
        # otherwise
            # append a tuple with left_index and right_index to positions
            # increment right_index
            # set left_index to right_index + 1
    # return positions
    pass


def reverse_by_words(words):
    # call reverse_by_characters and pass in words
    # initialize a variable pos to the return value of find_words_positions and pass in words
    # loop through pos
        # call reverse_by_characters passing in the values in the tuples
    pass
