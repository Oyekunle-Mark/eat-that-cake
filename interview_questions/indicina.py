"""
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
    # start by instantiating a stack class
    stack = []
    # have a mapBracket dictionary to match opening and closing brackets
    mapBracket = {
        '(': ')',
        # '{': '}',
        # '[': ']'
    }
    # opening = set(['(', '{', '['])
    # closing = set([')', ']', '}'])
    # iterate thorough the input_str
    for char in input_str:
        # if the current character is an opening brackets
        if char == '(':
            # push into the stack
            stack.append(char)
        # otherwise, if its a closing bracket
        elif char == ')':
            # check if stack is empty
            if len(stack) == 0:
                # return False
                return False
            # # pop from the stack and compare to the current bracket I have
            popped_item = stack.pop()
            # # if it does not match
            if char != mapBracket[popped_item]:
                # return False
                return False
    # check if the stack is empty
    # return True if it is
    # return false otherwise
    return len(stack) == 0

print(balance_bracket('()'))
print(balance_bracket('(([]){})'))
print(balance_bracket('([)'))
print(balance_bracket('([)]'))
print(balance_bracket('[(({}[]))]'))
print(balance_bracket('[()()]()'))
print(balance_bracket('())('))
print(balance_bracket('(hello)'))
print(balance_bracket('())'))
