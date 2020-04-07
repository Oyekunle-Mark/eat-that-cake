def word_cloud_data(the_string):
    return split_word(the_string)


def split_word(string):
    # initialize split_words to an empty list
    # initialize current_word to en empty string
    # loop through string
        # if character is an alphabet or an apostrophe
            # append character to current_word
        # if character is is a hyphen and current_word is not empty
            # append character to current_word
        # otherwise, if current_word is empty
            # continue to the next character
        # otherwise
            # append current_word to split_words
    # return split_words
    pass


print(word_cloud_data('Chocolate cake for dinner and pound cake for dessert'))
print(word_cloud_data('Strawberry short cake? Yum!'))
print(word_cloud_data('Dessert - mille-feuille cake'))
print(word_cloud_data('Mmm...mmm...decisions...decisions'))
print(word_cloud_data("Allie's Bakery: Sasha's Cakes"))
