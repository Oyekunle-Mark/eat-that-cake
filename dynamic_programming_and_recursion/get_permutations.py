def get_permutations(string):
    # To find the possible permutations of a string
    # find the permutations of every character in the
    # string without the last character, then insert the last
    # character in each index in the generated permutations

    # generating the possible combinations can be done recursively
    # with a base case being when input string is of length 1

    # set up a case of string being composed of one or being empty
    # if length of string is less than or equal to one
        # return input string as a set
    # initialize input_string_without_last_char to a slice of the
    # input string without the last character
    # initialize last_char to the last character in string
    # initialize permutations_of_input_string_without_last_character to the
    # recursive call of get_permutations passing in input_string_without_last_char
    # initialize possible permutations to an empty set
    # loop for every permutation_without_last in permutations_of_input_string_without_last_character
        # for every index in permutation_without_last
            # insert last_char and append to permutations
    # return permutations
    pass
