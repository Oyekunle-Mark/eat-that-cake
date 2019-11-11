def has_palindrome_permutation(the_string):
    # the trick to check if any combination of letters can
    # be a palindrom is to count the characters
    # palindromes have every character occuring an even number of times
    # only one character can occur an odd number of times

    # count the number of time each character occurs in the_string
    char_count = {}

    # loop through and count characters
    for char in the_string:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 0
    # set a variable is_odd to zero
    is_odd = 0
    # loop through the count dictionary
    for key, value in char_count.items():
        # if a character occurred an odd number of times
        if value % 2 != 0:
            # if is_odd is greater than or equal to 1
            if is_odd >= 1:
                # return False
                return False
            # otherwise, increment is_odd
            else:
                is_odd += 1
    # return True
    return True
