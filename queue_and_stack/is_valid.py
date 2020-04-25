def is_valid(code):
    # create a dict and map each opener to a closer
    # and name it openers_to_closers
    openers_to_closers = {
        '(': ')',
        '{': '}',
        '[': ']',
    }
    # create a set of the openers
    openers = set(openers_to_closers.keys())
    # create a set of the closers
    closers = set(openers_to_closers.values())
    # initialize s to an instance of the Stack class
    stack = []
    # loop through every character in code
    for char in code:
        # if character is an opener
        if char in openers:
            # push it onto the stack
            stack.append(char)
        # otherwise if character is a closer
        elif char in closers:
            if len(stack) == 0:
                return False
            # pop off the stack
            opener = stack.pop()
            # if pop item does not match the current closer
            if char != openers_to_closers[opener]:
                # return False
                return False
    # return True if the stack is empty
    return len(stack) == 0
