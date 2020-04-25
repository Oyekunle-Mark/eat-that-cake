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


class MaxStack(object):

    def __init__(self):
        # set items to an instance property as an empty list
        self.items = []
        # set maxes to an instance property of a stack instance

    def push(self, item):
        # append to self.items
        self.items.append(item)
        # compare item with the largest item in maxes
            # if it's larger, replace it

    def pop(self):
        # check if self.items is empty
        if not self.items:
            # return None
            return None
        # get the popped item from self.items
        item = self.items.pop()
        # check if item is the largest item from maxes
            # if it is pop the largest item from maxes too
        # return item

    def get_max(self):
        # return the return value of the peek method on maxes
        pass
