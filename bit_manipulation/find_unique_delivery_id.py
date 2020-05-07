def find_unique_delivery_id(delivery_ids):
    # a simple way of doing this in linear time
    # and constant space is to cancel out the repeated delivery_id
    # to cancel out two numbers you can use bitwise xor

    # initialize unique_id to zero
    unique_id = 0

    # loop through every delivery_id in delivery_ids
    for delivery_id in delivery_ids:
        # xor delivery_id and unique_id
        unique_id ^= delivery_id

    # whatever number is left at the end of loop is the unique_id
    # xor has cancelled out all repeated delivery_id
    # return unique_id
    return unique_id
