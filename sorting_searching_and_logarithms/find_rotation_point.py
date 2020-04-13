def find_rotation_point(words):
    # initialize first_word to the first_item in words
    first_word = words[0]
    # initialize floor_index to zero
    floor_index = 0
    # initialize ceiling_index to zero
    ceiling_index = len(words) - 1
    # loop while floor_index is less than ceiling_index
    while floor_index < ceiling_index:
        # set midpoint to the average of floor_index and ceiling_index
        midpoint = (floor_index + ceiling_index) // 2
        # if midpoint is greater than first_word
        if words[midpoint] >= first_word:
            # set floor_index to midpoint
            floor_index = midpoint
        # otherwise
        else:
            # set ceiling_index to midpoint
            ceiling_index = midpoint

        # If floor and ceiling have converged
        if floor_index + 1 == ceiling_index:
            # Between floor and ceiling is where we flipped to the beginning
            # so ceiling is alphabetically first
            return ceiling_index
