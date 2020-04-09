def highest_product_of_3(list_of_ints):
    # initialize lowest to the minimum of the first two integers
    lowest = min(list_of_ints[0], list_of_ints[1])
    # initialize highest to the maximum of the first two integers
    highest = max(list_of_ints[0], list_of_ints[1])
    # initialize lowest_product_of_two and highest_product_of_two
    # to the product of the first two integers
    lowest_product_of_two, highest_product_of_two = list_of_ints[0] * \
        list_of_ints[1], list_of_ints[0] * list_of_ints[1]
    # initialize highest_product_of_three to the product of the first three integers
    highest_product_of_three = list_of_ints[0] * \
        list_of_ints[1] * list_of_ints[2]
    # loop through every integer in list_of_ints
    # starting from the third
    for index in range(2, len(list_of_ints)):
        # set integer to the value at index of list_of_ints
        integer = list_of_ints[index]
        # set highest_product_of_three to the maximum of highest_product_of_three
        # integer multiplied by highest_product_of_two and
        # integer multiplied by lowest_product_of_two
        highest_product_of_three = max(
            highest_product_of_three, integer * highest_product_of_two, integer * lowest_product_of_two)

        # set highest_product_of_two to the maximum of of highest_product_of_two
        # and interger multiplied by lowest and integer multiplied by highest
        highest_product_of_two = max(
            highest_product_of_two, integer * highest, integer * lowest)

        # set lowest_product_of_two to the minimum of lowest_product_of_two
        # and integer multiplied by lowest and integer multiplied by highest
        lowest_product_of_two = min(
            lowest_product_of_two, integer * highest, integer * lowest)

        # set lowest to the minimum of lowest and interger
        lowest = min(lowest, integer)
        # set highest to the maximum of highest and interger
        highest = max(highest, integer)
    # return highest_product_of_three
    return highest_product_of_three
