"""
PROBLEM STATEMENT
=======================================================================


Write a function that converts number to text, Passing an int number should return array of text number.

Example 1: 
23498643 => [two, three, four, nine, eight, six, four, three]

Example 2:

40263645 => [four, zero, two, six, three, six, four, four, five]
"""


def parse_num(inp):
    # parse inp to a string
    inp_str = str(inp)
    # create a mapping of int to text representation
    int_mapping = {
        '0': 'zero',
        '1': 'one',
        '2': 'two',
        '3': 'three',
        '4': 'four',
        '5': 'five',
        '6': 'six',
        '7': 'seven',
        '8': 'eight',
        '9': 'nine',
    }

    # instantiate ret to an empty list
    ret = []

    # loop through inp_str
    for char in inp_str:
        # append the string mapping of the int character to re
        ret.append(int_mapping[char])

    # return ret
    return ret


print(parse_num(23498643))
print(parse_num(40263645))
