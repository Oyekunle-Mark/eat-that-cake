def reverse_in_place(char_ls):
    # get the length of the char_ls - 1 and set to a variable right_index
    right_index = len(char_ls) - 1
    # set the index to zero
    left_index = 0

    # while left_index is less than right_index
    while left_index < right_index:
        # swap the character at left_index with the character at right_index
        char_ls[left_index], char_ls[right_index] = char_ls[right_index], char_ls[left_index]

        # increment index
        left_index += 1
        # decrement length
        right_index -= 1


string = ["h", "e", "l", "l", "o"]
reverse_in_place(string)
print(string)
