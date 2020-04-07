def word_cloud_data(the_string):
    return split_word(the_string)


def split_word(string):
    # initialize split_words to an empty list
    split_words = []
    # initialize current_word to en empty string
    current_word = ''
    # loop through string
    for character in string:
        # if character is an alphabet or an apostrophe
        if character.isalpha() or character == "'":
            # append character to current_word
            current_word += character
        # if character is a hyphen and current_word is not empty
        elif character == '-' and current_word != '':
            # append character to current_word
            current_word += character
        # otherwise, if current_word is empty
        elif current_word == '':
            # continue to the next character
            continue
        # otherwise
        else:
            # append current_word to split_words
            split_words.append(current_word)
            # reset current_word
            current_word = ''
    # append the last word
    # if current_word
    if current_word:
        # append to split_words
        split_words.append(current_word)
    # return split_words
    return split_words


print(word_cloud_data('Chocolate cake for dinner and pound cake for dessert'))
print(word_cloud_data('Strawberry short cake? Yum!'))
print(word_cloud_data('Dessert - mille-feuille cake'))
print(word_cloud_data('Mmm...mmm...decisions...decisions'))
print(word_cloud_data("Allie's Bakery: Sasha's Cakes"))
