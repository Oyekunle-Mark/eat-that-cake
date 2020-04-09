def highest_product_of_3(list_of_ints):
    # initialize lowest_interger and highest_integer to the first integer
    # initialize the lowest_product_of_two and highest_product_of_two
    # to the product of the first two integers
    # set highest_product_of_three to the product of the first three integers
    # loop through every integer starting from the third integer
        # if integer multiplied by highest_product_of_two
        # is greater than highest_product_of_three
            # set highest_product_of_three to interger multiplied
            # by highest_product_of_two
        # otherwise, if integer multiplied by lowest_product_of_two
        # is greater than highest_product_of_three
            # set highest_product_of_three to interger multiplied
            # by lowest_product_of_two
        # initialize first_product_of_two to interger multiplied by lowest
        # if first_product_of_two is greater than highest_product_of_two
            # set highest_product_of_two to first_product_of_two
        # otherwise, if first_product_of_two is less than lowest_product_of_two
            # set lowest_product_of_two to first_product_of_two
        # initialize second_product_of_two to integer multiplied by highest
        # if second_product_of_two is greater than highest_product_of_two
            # set highest_product_of_two to second_product_of_two
        # otherwise, if second_product_of_two is less than lowest_product_of_two
            # set lowest_product_of_two to second_product_of_two
        # if interger is greater than highest
            # set highest to interger
        # otherwise, if interger is less than lowest
            # set lowest to interger
    # return highest_product_of_three
    pass
