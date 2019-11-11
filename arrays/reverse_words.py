def reverse_by_characters(word, left_index=None, right_index=None):
    # check if left and right is None
    if left_index is None and right_index is None:
        # set the left_index to 0
        left_index = 0
        # set the right_index to the length of word minus 1
        right_index = len(word) - 1

    # loop while left_index is less than right_index
    while left_index < right_index:
        # swap character at index left_index with character
        # at index right index
        word[left_index], word[right_index] = word[right_index], word[left_index]
        # increment left_index
        left_index += 1
        # decrement right_index
        right_index -= 1


def find_words_positions(words):
    # set the left_index to 0
    left_index = 0
    # set the right_index to 0
    right_index = -1
    # initialize positions to empty list
    positions = []

    # loop through words
    for char in words:
        # if current character is not an empty string, increment right index
        if char != ' ':
            right_index += 1
        # otherwise
        else:
            # append a tuple with left_index and right_index to positions
            positions.append((left_index, right_index))
            # increment right_index
            right_index += 1
            # set left_index to right_index + 1
            left_index = right_index + 1

    # append left_index and right_index to positions because list has ended
    positions.append((left_index, right_index))

    # return positions
    return positions


def reverse_by_words(words):
    # call reverse_by_characters and pass in words
    reverse_by_characters(words)

    # initialize a variable pos to the return value of find_words_positions and pass in words
    word_positions = find_words_positions(words)

    # loop through pos
    for start, end in word_positions:
        # call reverse_by_characters passing in the values in the tuples
        reverse_by_characters(words, start, end)


message = ['c', 'a', 'k', 'e', ' ',
           'p', 'o', 'u', 'n', 'd', ' ',
           's', 't', 'e', 'a', 'l']
reverse_by_words(message)
print(''.join(message))

message = list("vault")
reverse_by_words(message)
print(''.join(message))

message = list('thief cake')
reverse_by_words(message)
print(''.join(message))

message = list('rat the ate cat the')
reverse_by_words(message)
print(''.join(message))

message = list('yummy is cake bundt chocolate')
reverse_by_words(message)
print(''.join(message))
