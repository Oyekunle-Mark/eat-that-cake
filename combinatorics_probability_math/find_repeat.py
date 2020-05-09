def find_repeat(numbers_list):
    # to save up space, this can be done in O(1) space
    # since 1..n is a triangular series
    # we can add up every number in the series using the formula
    # add up all the numbers. The difference between the two
    # will be the repeated number

    # find the value of n which will be the length minus
    # one because of the repeat number
    n = len(numbers_list) - 1
    # find the triangular_sum using the formula
    triangular_sum = (n * n + n) / 2
    # find the total_sum of all numbers in numbers_list
    total_sum = sum(numbers_list)

    # return the difference of total_sum and triangular_sum
    return total_sum - triangular_sum
