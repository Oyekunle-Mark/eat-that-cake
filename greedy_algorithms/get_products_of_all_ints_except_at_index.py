def get_products_of_all_ints_except_at_index(int_list):
    # initialize product_at_all_ints_except_index to list
    # of Nones of size int_list
    product_at_all_ints_except_index = [None] * len(int_list)
    # set product_so_far to one
    product_so_far = 1
    # loop through every int in int_list
    for index in range(0, len(int_list)):
        # set value at current index of product_at_all_ints_except_index
        # to the product_so_far
        product_at_all_ints_except_index[index] = product_so_far
        # set product_so_far to the product of product_so_far and
        # integer at current index of int_list
        product_so_far *= int_list[index]
    # set product_so_far to one
    product_so_far = 1
    # loop through int_list backwards
    for index in range(len(int_list) - 1, -1, -1):
        # set value at current index of product_at_all_ints_except_index to the
        # product of product_so_far and value at current index of product_at_all_ints_except_index
        product_at_all_ints_except_index[index] *= product_so_far
        # set product_so_far to the product of product_so_far and
        # integer at current index of int_list
        product_so_far *= int_list[index]
    # return product_at_all_ints_except_index
    return product_at_all_ints_except_index
