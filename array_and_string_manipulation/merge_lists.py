def merge_lists(my_list, alices_list):
    # initialize index_one and index_two to zero
    index_one, index_two = 0, 0
    # initialize merged_list to an empty list
    merged_list = []

    # loop while index_one is less than length of my_list
    # and index_two is less than length of alices_list
    while index_one < len(my_list) and index_two < len(alices_list):
        # if value at index_one of my_list is less than
        # value at index_two of alices_list
        if my_list[index_one] < alices_list[index_two]:
            # append value at index_one of my_list into merged_list
            merged_list.append(my_list[index_one])
            # increment index_one
            index_one += 1
        # otherwise
        else:
            # append value at index_two of alices_list into merged_list
            merged_list.append(alices_list[index_two])
            # increment index_two
            index_two += 1

    # if index_one is less than length of my_list
    if index_one < len(my_list):
        # append value at index_one of my_list into merged_list
        merged_list.append(my_list[index_one])
        # increment index_one
        index_one += 1

    # if index_two is less than length of alices_list
    if index_two < len(alices_list):
        # append value at index_two of alices_list into merged_list
        merged_list.append(alices_list[index_two])
        # increment index_two
        index_two += 1

    # return merged_list
    return merged_list


my_list = [3, 4, 6, 10, 11, 15]
alices_list = [1, 5, 8, 12, 14, 19]

# Prints [1, 3, 4, 5, 6, 8, 10, 11, 12, 14, 15, 19]
print(merge_lists(my_list, alices_list))
