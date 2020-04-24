# modify the function signature to take a default parameter
# current_index which is set to zero
def change_possibilities(amount, denominations, current_index=0):
    # To solve this problem, think of it as a sum of subproblems
    # of the possibility of making change for each of the denominations

    # check if amount is zero
    if amount == 0:
        # return one
        return 1
    # check if amount is less than zero
    if amount < 0:
        # return zero
        return 0
    # check if current_index has overshot the denominations
    # if current_index is equivalent to length of denominations
    if current_index == len(denominations):
        # return zero
        return 0
    # initialize current_coin to the coin at current_index
    # of denominations
    current_coin = denominations[current_index]
    # initialize sum_of_change_possibility to zero
    sum_of_change_possibility = 0
    # loop while amount is greater than or equal to zero
    while amount >= 0:
        # add the return value of recursive call to change_possibilities
        # passing in the amount, denominations and current_index plus one
        sum_of_change_possibility += change_possibilities(
            amount, denominations, current_index + 1)
        # decrement amount by substracting current_coin
        amount -= current_coin
    # return sum_of_change_possibility
    return sum_of_change_possibility


print(change_possibilities(4, (1, 2, 3)))
print(change_possibilities(100, (1, 5, 10, 25, 50)))