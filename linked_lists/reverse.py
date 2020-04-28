"""
class LinkedListNode(object):

    def __init__(self, value):
        self.value = value
        self.next  = None
"""


def reverse(head_of_list):
    # To reverse the linked list,
    # modify each node as we go and point the next
    # to the node before. Do that until there is no more
    # nodes and return the last processed node

    # initialize current to head_of_list
    current = head_of_list
    # initialize prev and next to None
    prev = None
    next = None
    # loop while there is a current node
    while current:
        # set next to current's next node
        next = current.next
        # set current's next node to prev
        current.next = prev
        # set prev to current
        prev = current
        # set current to next
        current = next
    # since current will be None here
    # return prev
    return prev
