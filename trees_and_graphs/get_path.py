# use the deque class from the collections module
from collections import deque


def get_path(graph, start_node, end_node):
    # if the start_node or end_node is not in the graph
    if start_node not in graph or end_node not in graph:
        # raise an exception
        raise Exception("Start and End nodes must be in the same graph")

    # initialize queue to an instance of deque class
    queue = deque()
    # initialize visited_node to an empty set
    visited_nodes = set()
    # enqueue the start_node node as a list into the queue
    queue.appendleft([start_node])

    # loop while queue is not empty
    while len(queue):
        # dequeue the path from the queue
        path = queue.pop()
        # get the last_node from the path
        last_node = path[-1]

        # if the last_node is equivalent to the end_node
        if last_node == end_node:
            # return the path
            return path

        # if the last_node has not been visited_node
        if last_node not in visited_nodes:
            # add it to the visited_node
            visited_nodes.add(last_node)

            # for every node connected to last_node
            for node in graph[last_node]:
                # initialize new_path to a copy of path
                new_path = list(path)
                # append node to new_path
                new_path.append(node)
                # enqueue new_path into the queue
                queue.appendleft(new_path)


graph = {
    'Min': ['William', 'Jayden', 'Omar'],
    'William': ['Min', 'Noam'],
    'Jayden': ['Min', 'Amelia', 'Ren', 'Noam'],
    'Ren': ['Jayden', 'Omar'],
    'Amelia': ['Jayden', 'Adam', 'Miguel'],
    'Adam': ['Amelia', 'Miguel', 'Sofia', 'Lucas'],
    'Miguel': ['Amelia', 'Adam', 'Liam', 'Nathan'],
    'Noam': ['Nathan', 'Jayden', 'William'],
    'Omar': ['Ren', 'Min', 'Scott']
}

print(get_path(graph, 'Jayden', 'Adam'))
