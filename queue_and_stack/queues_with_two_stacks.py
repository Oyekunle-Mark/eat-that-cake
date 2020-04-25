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
    def __init__(self):
        # set instance properties in_stack and out_stack
        # to stack instances
        self.in_stack = Stack()
        self.out_stack = Stack()

    def enqueue(self, item):
        # to enqueue, push onto the in_stack
        self.in_stack.push(item)

    def dequeue(self):
        # to dequeue, move all the items from the in_stack to the out_stack
        # then pop off the out_stack

        # first check if the out_stack is empty
        if self.out_stack.peek() is None:
            # move all the items over from the in_stack
            # loop while the in_stack is not empty
            while self.in_stack.peek() is not None:
                # get the popped item from the in_stack
                popped_item = self.in_stack.pop()
                # push that item onto the out_stack
                self.out_stack.append(popped_item)
            # if the out_stack is still empty
            if self.out_stack.peek() is None:
                # raise an exception
                raise IndexError("Can't dequeue from empty queue!")
        # return the popped item from the out_stack
        return self.out_stack.pop()
