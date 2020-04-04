def reverse(list_of_chars):
    # set the start_index to zero
    start_index = 0
    # set the end_index to length of list_of_chars minus one
    end_index = len(list_of_chars) - 1
    # loop while start_index is less than end_index

    while start_index < end_index:
        # swap values at start_index and end_index
        list_of_chars[start_index], list_of_chars[end_index] = list_of_chars[end_index], list_of_chars[start_index]
        # increment start_index
        start_index += 1
        # decrement end_index
        end_index -= 1
