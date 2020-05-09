def contains(ordered_list, number):
    # since the list is sorted
    # use binary search and find the number(or not) in O(log n)
    # time and O(1) space

    # initialize lower to zero
    lower = 0
    # initialize upper to length of ordered_list minus one
    upper = len(ordered_list) - 1

    # loop while lower <= upper
    while lower <= upper:
        # initialize midpoint to the average of lower and upper
        midpoint = (lower + upper) // 2

        # if number is equivalent to value at midpoint
        if number == ordered_list[midpoint]:
            # return True
            return True

        # if number is greater than value at midpoint
        if number > ordered_list[midpoint]:
            # set lower to midpoint plus one
            lower = midpoint + 1
        # otherwise
        else:
            # set upper to midpoint minus one
            upper = midpoint - 1

    # return False
    return False
