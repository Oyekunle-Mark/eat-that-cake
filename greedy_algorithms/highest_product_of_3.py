def highest_product_of_3(list_of_ints):
    # initialize lowest_interger and highest_integer to the first integer
    lowest_integer, highest_integer = list_of_ints[0], list_of_ints[0]
    # initialize the lowest_product_of_two and highest_product_of_two
    # to the product of the first two integers
    lowest_product_of_two, highest_product_of_two = list_of_ints[0] * \
        list_of_ints[1], list_of_ints[0] * list_of_ints[1]
    # set highest_product_of_three to the product of the first three integers
    highest_product_of_three = list_of_ints[0] * \
        list_of_ints[1] * list_of_ints[2]
    # loop through every integer starting from the third integer
    for index in range(2, len(list_of_ints)):
        # let variable interger hold current value at index of list_of_ints
        interger = list_of_ints[index]
        # if integer multiplied by highest_product_of_two
        # is greater than highest_product_of_three
        if interger * highest_product_of_two > highest_product_of_three:
            # set highest_product_of_three to interger multiplied
            # by highest_product_of_two
            highest_product_of_three = interger * highest_product_of_two
        # otherwise, if integer multiplied by lowest_product_of_two
        # is greater than highest_product_of_three
        elif interger * lowest_product_of_two > highest_product_of_three:
            # set highest_product_of_three to interger multiplied
            # by lowest_product_of_two
            highest_product_of_three = interger * lowest_product_of_two
        # initialize first_product_of_two to interger multiplied by lowest_integer
        first_product_of_two = interger * lowest_integer
        # if first_product_of_two is greater than highest_product_of_two
        if first_product_of_two > highest_product_of_two:
            # set highest_product_of_two to first_product_of_two
            highest_product_of_two = first_product_of_two
        # otherwise, if first_product_of_two is less than lowest_product_of_two
        elif first_product_of_two < lowest_product_of_two:
            # set lowest_product_of_two to first_product_of_two
            lowest_product_of_two = first_product_of_two
        # initialize second_product_of_two to integer multiplied by highest_integer
        second_product_of_two = interger * highest_integer
        # if second_product_of_two is greater than highest_product_of_two
        if second_product_of_two > highest_product_of_two:
            # set highest_product_of_two to second_product_of_two
            highest_product_of_three = second_product_of_two
        # otherwise, if second_product_of_two is less than lowest_product_of_two
        elif second_product_of_two < lowest_product_of_two:
            # set lowest_product_of_two to second_product_of_two
            lowest_product_of_two = second_product_of_two
        # if interger is greater than highest_integer
        if interger > highest_integer:
            # set highest_integer to interger
            highest_integer = interger
        # otherwise, if interger is less than lowest_integer
        elif interger < lowest_integer:
            # set lowest_integer to interger
            lowest_integer = interger
    # return highest_product_of_three
    return highest_product_of_three
