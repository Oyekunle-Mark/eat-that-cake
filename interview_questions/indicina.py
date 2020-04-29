"""
PROBLEM STATEMENT
=======================================================================


Given a string of round open and closing brackets, return whether the brackets are balanced (well-formed).
For example, given the string "([])[]({})", you should return true.
Given the string "([)(]" or "((()", you should return false.
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
    # loop through the input_str
        # if character is an opening bracket
            # increment count
        # otherwise, if character is a closing bracket
            # if count is zero
                # return False
            # decrement count
    # return True if count is zero
    # and False otherwise
    pass


print(balance_bracket('()'))
print(balance_bracket('(([]){})'))
print(balance_bracket('([)'))
print(balance_bracket('([)]'))
print(balance_bracket('[(({}[]))]'))
print(balance_bracket('[()()]()'))
print(balance_bracket('())('))
print(balance_bracket('(hello)'))
print(balance_bracket('())'))
