def is_first_come_first_served(take_out_orders, dine_in_orders, served_orders):
    # set take_out_index and dine_in_index to zero
    take_out_index, dine_in_index = 0, 0
    # loop for every order in served_orders
    for order in served_orders:
        # if order is take_out_index of take_out_orders
        if order == take_out_orders[take_out_index]:
            # increment take_out_index
            take_out_index += 1
        # otherwise, if order is dine_in_index of dine_in_orders
        elif order == dine_in_orders[dine_in_index]:
            # increment dine_in_index
            dine_in_index += 1
        # otherwise
        else:
            # return False
            return False
    # return True
    return True
