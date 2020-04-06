def has_palindrome_permutation(the_string):
    # initialize character_count to an empty dictionary
    character_count = {}

    # loop through every character in the_string
    for character in the_string:
        # if character is in character_count
        if character in character_count:
            # increment the count
            character_count[character] += 1
        # otherwise
        else:
            #  add it to character_count and set it as 1
            character_count[character] = 1

    # initialize even_count to zero
    even_count = 0

    # loop through every count in character_count
    for _, count in character_count.items():
        # if count is not even
        if count % 2 != 0:
            # if even_count equals one
            if even_count == 1:
                # return False
                return False
            # increment even_count by one
            even_count += 1

    # return True
    return True
