import random


def get_random(floor, ceiling):
    return random.randrange(floor, ceiling + 1)


def shuffle(the_list):
    # initialize ceiling to the length of the_list minus one
    ceiling = len(the_list) - 1
    # loop through every index in the_list
    for index in range(0, len(the_list)):
        # initialize random_index to the return value of
        # get_random passing in index and ceiling
        random_index = get_random(index, ceiling)
        # swap items at random_index and index
        the_list[index], the_list[random_index] = the_list[random_index], the_list[index]
