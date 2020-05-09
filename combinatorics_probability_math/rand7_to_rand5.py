import random


def rand7():
    return random.randint(1, 7)


def rand5():
    # since every number in the five-sided die must have the same
    # probability of being chosen
    # we just keep on rolling the die until we get a number
    # that is five or less

    # initialize result to the return value of rand7
    result = rand7()
    # return result if it is less than or equal to 5
    # otherwise return the recursive call to rand5
    return result if result <= 5 else rand5()


print('Rolling 5-sided die...')
print(rand5())
