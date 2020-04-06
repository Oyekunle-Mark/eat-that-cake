def is_first_come_first_served(take_out_orders, dine_in_orders, served_orders):
    # set take_out_index and dine_in_index to zero
    take_out_index, dine_in_index = 0, 0
    # initialize take_out_limit and dine_in_limit to the
    # last allowable index in both lists
    take_out_limit = len(take_out_orders) - 1
    dine_in_limit = len(dine_in_orders) - 1
    # loop for every order in served_orders
    for order in served_orders:
        # if take_out_orders is not an empty list
        # and order is take_out_index of take_out_orders
        if take_out_orders and order == take_out_orders[take_out_index]:
            # if take_out_index is less than take_out_limit
            if take_out_index < take_out_limit:
                # increment take_out_index
                take_out_index += 1
        # otherwise, if dine_in_orders is not an empty list
        # and order is dine_in_index of dine_in_orders
        elif dine_in_orders and order == dine_in_orders[dine_in_index]:
            # if dine_in_index is less than dine_in_limit
            if dine_in_index < dine_in_limit:
                # increment dine_in_index
                dine_in_index += 1
        # otherwise
        else:
            # return False
            return False
    # return True
    return True


print(is_first_come_first_served([1, 4, 5], [2, 3, 6], [1, 2, 3, 4, 5, 6]))
print(is_first_come_first_served([1, 5], [2, 3, 6], [1, 2, 6, 3, 5]))
print(is_first_come_first_served([], [2, 3, 6], [2, 3, 6]))
