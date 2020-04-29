"""
Write a function that converts number to text, Passing an int number should return array of text number eg
23498643 => [two, three, four, nine, eight, six, four, three]
40263645 => [four, zero, two, six, three, six, four, four, five]
"""


def parse_num(inp):
    # parse inp to a string
    inp_str = str(inp)
    # # create a mapping of int to text representation
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

    ten_mapping = ['ten', 'eleven', 'twelve', 'thirteen', 'fourteen',
                   'fifteen', 'sixteen', 'seventeen', 'eighteen', 'nineteen', ]

    mapping_mult = {
        '2': 'twenty',
        '3': 'thirty',
        '4': 'forty',
        '5': 'fifty',
        '6': 'sixty',
        '7': 'seventy',
        '8': 'eighty',
        '9': 'ninety',
    }
    # create a list to be returned
    ret = []

    # iterate through inp_str
    for index in range(0, len(inp_str), 2):
        # check the mapping of the current character in the int_mapping
        # append to the ret
        res = ''
        if inp_str[index] == '0':
            ret.append(int_mapping[inp_str[index+1]])
        elif inp_str[index] == '1':
            ret.append(ten_mapping[int(inp_str[index+1])])
        else:
            first = mapping_mult[inp_str[index]]
            second = int_mapping[inp_str[index+1]]

            if second == 'zero':
                res = first
            else:
                res = first + '-' + second

            ret.append(res)
    # return ret
    return ret


print(parse_num(23498643))
print(parse_num(40263645))
