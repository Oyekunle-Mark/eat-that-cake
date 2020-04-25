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
    # create a set of the openers
    # create a set of the closers
    # initialize s to an instance of the Stack class
    # loop through every character in code
        # if character is an opener
            # push it onto the stack
        # otherwise if character is a closer
            # pop off the stack
            # if pop item does not match the current closer
                # return False
    # return True if the stack is empty
    pass
