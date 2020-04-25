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


class QueueTwoStacks(object):
    # initialize a constructor
        # set instance properties in_stack and out_stack
        # to stack instances

    def enqueue(self, item):
        # to enqueue, push onto the in_stack
        pass

    def dequeue(self):
        # to dequeue, move all the items from the in_stack to the out_stack
        # then pop off the out_stack

        # first check if the out_stack is empty
            # move all the items over from the in_stack
            # loop while the in_stack is not empty
                # get the popped item from the in_stack
                # push that item onto the out_stack
            # if the out_stack is still empty
                # raise an exception
        # return the popped item from the out_stack
        pass
