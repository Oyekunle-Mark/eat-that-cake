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

    def push(self, item):
        # append to self.items
        self.items.append(item)

    def pop(self):
        # check if self.items is empty
        if not self.items:
            # return None
            return None
        # return the popped item from self.items
        return self.items.pop()

    def get_max(self):
        pass
