def find_repeat(numbers):
    # sort numbers in place
    numbers.sort()
    # initialize a variable previous_number to zero
    previous_number = 0
    # loop through every number in numbers
    for number in numbers:
        # if current number equals previous_number
        if number == previous_number:
            # return previous_number
            return previous_number
        # set previous_number to the current number
        previous_number = number
