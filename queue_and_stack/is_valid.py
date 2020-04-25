class Stack(object):

    def __init__(self):
        """Initialize an empty stack"""
        self.items = []

    def push(self, item):
        """Push a new item onto the stack"""
        self.items.append(item)

    def pop(self):
        """Remove and return the last item"""
        # If the stack is empty, return None
        # (it would also be reasonable to throw an exception)
        if not self.items:
            return None

        return self.items.pop()

    def peek(self):
        """Return the last item without removing it"""
        if not self.items:
            return None
        return self.items[-1]


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
    s = Stack()
    # loop through every character in code
    for char in code:
        # if character is an opener
        if char in openers:
            # push it onto the stack
            s.push(char)
        # otherwise if character is a closer
        elif char in closers:
            if s.peek() is None:
                return False
            # pop off the stack
            opener = s.pop()
            # if pop item does not match the current closer
            if char != openers_to_closers[opener]:
                # return False
                return False
    # return True if the stack is empty
    return s.peek() is None
