def word_cloud_data(the_string):
    # initialize split_string to the return value of split_word
    split_string = split_word(the_string)
    # initialize word_count to empty dictionary
    word_count = {}
    # loop through for every word in split_string
    for word in split_string:
        # if word to lower case is in word_count
        if word.lower() in word_count:
            # increment the count
            word_count[word.lower()] += 1
        # otherwise
        else:
            # add the word to lower case to the word_count
            # and set the value to one
            word_count[word.lower()] = 1
    # return word_count
    return word_count


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
