# create a reverse_array_portion which reverses section of a list
# it should take the start_index, end_index and the list to be reversed
def reverse_array_portion(start_index, end_index, arr):
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
    # reverse the entire list in place
    # loop through for every character in message
        # if current character is an empty space
            # reverse the characters from start_index to current_index
            # set start_index to current_index
    # remember to swap the characters of the last word
    # swap using start_index and end_index
    pass
