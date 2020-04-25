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


def get_closing_paren(sentence, opening_paren_index):
    # check if the starting parenthesis is a closing one
        # raise an exception
    # instantiate the stack class
    # initialize sen_length to the length of the sentence
    # loop from opening_paren_index to the end index of sentence
        # if character at current index is an opening parenthesis
            # push it to the stack
        # otherwise, if it is a closing parenthesis
            # pop from the stack
        # if the stack is empty
            # return current index
    pass
