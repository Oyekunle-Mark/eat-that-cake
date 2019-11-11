def is_first_come_first_served(take_out_orders, dine_in_orders, served_orders):
    # initialize take_out_index to zero
    take_out_index = 0
    # initialize dine_in_index to zero
    dine_in_index = 0
    # initialize take_out_len to the len of take_out_orders - 1
    take_out_len = len(take_out_orders) - 1
    # initialize dine_in_len to the len of dine_in_orders - 1
    dine_in_len = len(dine_in_orders) - 1

    # loop through server_orders
    for order in served_orders:
        # if take_out_index is less than take_out_len and order is at index
        # take_out_index of take_out_orders
        if take_out_index <= take_out_len and order == take_out_orders[take_out_index]:
            # increment take_out_index
            take_out_index += 1
        # also, if dine_in_index is less than dine_in_len and order is at index
        # dine_in_index of dine_in_orders
        elif dine_in_index <= dine_in_len and order == dine_in_orders[dine_in_index]:
            # increment dine_in_index
            dine_in_index += 1
        # otherwise,
        else:
            # return False
            return False

    # check if take_out_index does not equal take_out_len + 1
    # or dine_in_index does not equal dine_in_len + 1
    if take_out_index != take_out_len + 1 or dine_in_index != dine_in_len + 1:
        # return False
        return False

    # return True
    return True


print(is_first_come_first_served(
    [1, 4, 5], [2, 3, 6], [1, 2, 3, 4, 5, 6]))  # True
print(is_first_come_first_served([1, 5], [2, 3, 6], [1, 2, 6, 3, 5]))  # False
print(is_first_come_first_served([], [2, 3, 6], [2, 3, 6]))  # True
print(is_first_come_first_served([1, 5], [2, 3, 6], [1, 6, 3, 5]))  # False
print(is_first_come_first_served(
    [1, 5], [2, 3, 6], [1, 2, 3, 5, 6, 8]))  # False
print(is_first_come_first_served([1, 9], [7, 8], [1, 7, 8]))  # False
print(is_first_come_first_served([55, 9], [7, 8], [1, 7, 8, 9]))  # False
