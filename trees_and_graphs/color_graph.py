"""
class GraphNode:

    def __init__(self, label):
        self.label = label
        self.neighbors = set()
        self.color = None


a = GraphNode('a')
b = GraphNode('b')
c = GraphNode('c')

a.neighbors.add(b)
b.neighbors.add(a)
b.neighbors.add(c)
c.neighbors.add(b)

graph = [a, b, c]
"""


def color_graph(graph, colors):
    # the graph coloring will be done by greedily walking though
    # the list of graph nodes. At each graph node,
    # we will get all the colors of the neighboring nodes in a set
    # and assign the first color from colors that is not in neighborring
    # color to the graph node.
    pass
