def contains(ordered_list, number):
    # since the list is sorted
    # use binary search and find the number(or not) in O(log n)

    # initialize lower to zero
    # initialize upper to length of ordered_list minus one
    # loop while lower <= upper
        # initialize midpoint to the average of lower and upper
        # if number is equivalent to value at midpoint
            # return True
        # if number is greater than value at midpoint
            # set lower to midpoint plus one
        # otherwise
            # set upper to midpoint minus one
    # return False
    pass
