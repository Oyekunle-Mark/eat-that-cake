def reverse_array_portion(start_index, end_index, arr):
    """
    create a reverse_array_portion which reverses section of a list
    it should take the start_index, end_index and the list to be reversed
    """
    # loop while start_index is less than end_index
    while start_index < end_index:
        # swap item at start_index and end_index
        arr[start_index], arr[end_index] = arr[end_index], arr[start_index]
        # increment start_index
        start_index += 1
        # decrement end_index
        end_index -= 1


def reverse_words(message):
    # grab the start and end index of message
    start_index = 0
    end_index = len(message) - 1

    # reverse the entire list in place
    reverse_array_portion(start_index, end_index, message)

    # loop through for every character in message
    for current_index, character in enumerate(message):
        # if current character is an empty space
        if character == ' ':
            # reverse the characters from start_index to current_index minus one
            reverse_array_portion(start_index, current_index - 1, message)
            # set start_index to current_index plus one
            start_index = current_index + 1

    # remember to swap the characters of the last word
    # swap using start_index and end_index
    reverse_array_portion(start_index, end_index, message)


message = list('yummy is cake bundt chocolate')

reverse_words(message)
print(''.join(message))
