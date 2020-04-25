def get_closing_paren(sentence, opening_paren_index):
    # check if the starting parenthesis is a closing one
    if sentence[opening_paren_index] != '(':
        # raise an exception
        raise IndexError("Starting position must be an opening parenthesis")

    # instantiate paren_count to zero
    paren_count = 0
    # initialize sen_length to the length of the sentence
    sen_length = len(sentence)

    # loop from opening_paren_index to the end index of sentence
    for index in range(opening_paren_index, sen_length):
        # if character at current index is an opening parenthesis
        if sentence[index] == '(':
            # increment paren_count
            paren_count += 1
        # otherwise, if it is a closing parenthesis
        elif sentence[index] == ')':
            # decrement paren_count
            paren_count -= 1

        # if paren_count equals zero
        if paren_count == 0:
            # return index
            return index

    # if the loop terminates without finding matching position
    # raise an exception
    raise IndexError("Starting position must be an opening parenthesis")
