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
    if sentence[opening_paren_index] != '(':
        # raise an exception
        raise IndexError("Starting position must be an opening parenthesis")
    # instantiate the stack class
    s = Stack()
    # initialize sen_length to the length of the sentence
    sen_length = len(sentence)
    # loop from opening_paren_index to the end index of sentence
    for index in range(opening_paren_index, sen_length):
        # if character at current index is an opening parenthesis
        if sentence[index] == '(':
            # push it to the stack
            s.push('(')
        # otherwise, if it is a closing parenthesis
        elif sentence[index] == ')':
            # pop from the stack
            s.pop()
        # if the stack is empty
        if s.peek() is None:
            # return current index
            return index
