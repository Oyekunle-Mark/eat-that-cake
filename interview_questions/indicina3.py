"""
PROBLEM STATEMENT
=======================================================================


Write a function that converts number to text, Passing an int number should return array of text number.
The function should chunk the int number into two digits and return the text format of the chunks.

Example 1:
Given:

23498643 => 23, 49, 86, 43 => ['twenty-three', 'forty-nine', 'eighty-six', 'forty-three']

Example 2:
Given:

40263645 => 40, 26, 36, 45 => ['forty', 'twenty-six', 'thirty-six', 'forty-five']

Example 3:
Given:

9203234612391071 => 92, 03, 23, 46, 12, 39, 10, 71 => ['ninety-two', 'three', 'twenty-three', 'forty-six', 'twelve', 'thirty-nine', 'ten', 'seventy-one']


NOTE:
The number of digits in the input will always be even.
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
        '10': 'ten',
        '11': 'eleven',
        '12': 'twelve',
        '13': 'thirteen',
        '14': 'fourteen',
        '15': 'fifteen',
        '16': 'sixteen',
        '17': 'seventeen',
        '18': 'eighteen',
        '19': 'nineteen',
    }
    # create a mapping of tens to the leading text
    tens_mapping = {
        '2': 'twenty',
        '3': 'thirty',
        '4': 'forty',
        '5': 'fifty',
        '6': 'sixty',
        '7': 'seventy',
        '8': 'eighty',
        '9': 'ninety',
    }
    # instantiate ret to an empty list
    ret = []
    # iterate through inp_str starting at 0 and step through
    # jumping every one index to always find the start of the next
    # chunk
    for index in range(0, len(inp_str), 2):
        # set first_digit and second_digit to the first and second
        # digits in the current chunk
        first_digit = inp_str[index]
        second_digit = inp_str[index + 1]
        # if current chunk starts with a zero
        if first_digit == '0':
            # append the text value of the second digit
            ret.append(int_mapping[second_digit])
        # otherwise, if first_digit starts with a one
        elif first_digit == '1':
            # append the text value of the whole chunk
            ret.append(int_mapping[first_digit + second_digit])
        # finally, if first_digit is greater than one
        else:
            # check if second_digit is a zero
            if second_digit == '0':
                # append the text value of the ten value alone
                ret.append(tens_mapping[first_digit])
            # otherwise,
            else:
                # concatenate the ten value of the first with the int
                # mapping of the second and append to ret
                text = tens_mapping[first_digit] + \
                    '-' + int_mapping[second_digit]
                ret.append(text)
    # return ret
    return ret


print(parse_num(23498643))
print(parse_num(40263645))
print(parse_num(9203234612391071))
