# modify the function signature to take a default parameter
# current_index which is set to one
def change_possibilities(amount, denominations):
    # To solve this problem, think of it as a sum of subproblems
    # of the possibility of making change for each of the denominations

    # check if amount is zero
        # return one
    # check if amount is less than zero
        # return zero
    # check if current_index has overshot the denominations
    # if current_index is equivalent to length of denominations
        # return zero
    # initialize current_coin to the coin at current_index
    # of denominations
    # initialize sum_of_change_possibility to zero
    # loop while amount is greater than or equal to zero
        # add the return value of recursive call to change_possibilities
        # passing in the amount, denominations and current_index plus one
        # decrement amount by substracting current_coin
    # return sum_of_change_possibility
    pass
