"""
class LinkedListNode(object):

        def __init__(self, value, next=None):
            self.value = value
            self.next  = next

        def get_values(self):
            node = self
            values = []
            while node is not None:
                values.append(node.value)
                node = node.next
            return values
"""


def delete_node(node_to_delete):
    # To delete a node from a Singly Linked List
    # one way is to modify the previous node's next node property
    # when given just the node to be deleted and there is no way
    # of knowing the previous node, we can modify the node to be
    # deleted.

    # the two cases are that the node_to_delete can be the last
    # node in the LinkedList or have nodes after it
    # check if node_to_delete next is not None
    # that is node_to_delete is not the tail
    if node_to_delete.next is not None:
        # set node_to_delete's value to the value of the next
        node_to_delete.value = node_to_delete.next.value
        # set node_to_delete's next to the next's next
        node_to_delete.next = node_to_delete.next.next
    # otherwise,
    else:
        # point node_to_delete to None
        node_to_delete = None
