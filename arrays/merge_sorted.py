def merge_sorted(ls1, ls2):
    # set a variable pos1 to zero
    pos1 = 0
    # set a variable pos2 to zero
    pos2 = 0
    # set a variable len1 to length of ls1
    len1 = len(ls1)
    # set a variable len2 to length of ls2
    len2 = len(ls2)
    # create a variable sorted_list and initialize to empty list
    sorted_list = []
    # loop while pos1 is less than len1 and pos2 is less than len2
    while pos1 < len1 and pos2 < len2:
        # if item at index pos1 of ls1 is less than
        # item at index pos2 of ls2
        if ls1[pos1] < ls2[pos2]:
            # append item at index pos1 of ls1 to sorted_list
            sorted_list.append(ls1[pos1])
            # increment pos1
            pos1 += 1
        # otherwise, append item at index pos2 to sorted_list
        else:
            sorted_list.append(ls2[pos2])
            # increment pos2
            pos2 += 1

    # loop while pos1 is less than len1
    while pos1 < len1:
        # append item at index pos1 of ls1 to sorted_list
        sorted_list.append(ls1[pos1])
        # increment pos1
        pos1 += 1

    # loop while pos2 is less than len2
    while pos2 < len2:
        # append item at index pos2 of ls2to sorted_list
        sorted_list.append(ls2[pos2])
        # increment pos2
        pos2 += 1

    # return sorted_list
    return sorted_list


print(merge_sorted([3, 4, 6, 10, 11, 15], [1, 5, 8, 12, 14, 19]))
