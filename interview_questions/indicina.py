"""
PROBLEM STATEMENT
=======================================================================


Given a string of round open and closing brackets, return whether the brackets are balanced (well-formed).

Example 1: Given the string "([])[]({})", you should return true.
Example 2: Given the string "([)(]" or "((()", you should return false.

Test Cases:

()             => true
(([]){})    => true
([)            => true
([)]        => true
[(({}[]))]    => true
[()()]()     => true
())(        => false
(hello)        => true
())            => false
"""


def balance_bracket(input_str: str) -> bool:
    # instantiate bracket count to zero
    bracket_count = 0
    # loop through the input_str
    for char in input_str:
        # if character is an opening bracket
        if char == '(':
            # increment count
            bracket_count += 1
        # otherwise, if character is a closing bracket
        elif char == ')':
            # if count is zero
            if bracket_count == 0:
                # return False
                return False
            # decrement count
            bracket_count -= 1
    # return True if count is zero
    # and False otherwise
    return bracket_count == 0


print(balance_bracket('()'))
print(balance_bracket('(([]){})'))
print(balance_bracket('([)'))
print(balance_bracket('([)]'))
print(balance_bracket('[(({}[]))]'))
print(balance_bracket('[()()]()'))
print(balance_bracket('())('))
print(balance_bracket('(hello)'))
print(balance_bracket('())'))
