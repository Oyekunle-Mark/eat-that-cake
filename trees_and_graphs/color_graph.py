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

    # loop through every graph_node in graph
    for graph_node in graph:
        # check if the graph node has a loop
        # if graph_node in graph_node.neighbors
        if graph_node in graph_node.neighbors:
            # raise exception that legal coloring is impossible with a node with a loop
            raise Exception('Legal coloring impossible for node with loop: %s' %
                            graph_node.label)

        # get all the colors of neighboring nodes
        # initialize neighbors_colors to a set from the list comprehension
        # of all the neighbor in graph_node neighbors that has a color
        neighbors_colors = set(
            [neighbor.color for neighbor in graph_node.neighbors if neighbor.color])

        # loop through every color in colors
        for color in colors:
            # if color is not in neighbors_colors
            if color not in neighbors_colors:
                # set the graph_node color to color
                graph_node.color = color
                # break the loop
                break
