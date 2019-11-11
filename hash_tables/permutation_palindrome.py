def has_palindrome_permutation(the_string):
    # the trick to check if any combination of letters can
    # be a palindrom is to count the characters
    # palindromes have every character occuring an even number of times
    # only one character can occur an odd number of times

    # count the number of time each character occurs in the_string
    # set a variable is_odd to zero
    # loop through the count dictionary
        # if a character occurred an odd number of times
            # if is_odd is greater than or equal to 1
                # return False
            # otherwise, increment is_odd
    # return True
    pass
