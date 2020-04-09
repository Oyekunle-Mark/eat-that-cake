def highest_product_of_3(list_of_ints):
    # initialize first, second and third highest integers to zero
    first_highest_int, second_highest_int, third_highest_int = 0, 0, 0
    # loop through every number in list_of_ints
    for number in list_of_ints:
        # if number is greater than first_highest_int
        if number > first_highest_int:
            # set first_highest_int to number
            first_highest_int = number
        # otherwise, if number is greater than second_highest_int
        elif number > second_highest_int:
            # set second_highest_int to number
            second_highest_int = number
        # otherwise, if number is greater than third_highest_int
        elif number > third_highest_int:
            # set third_highest_int to number
            third_highest_int = number
    # return the product of first_highest_int, second_highest_int and third_highest_int
    return first_highest_int * second_highest_int * third_highest_int
