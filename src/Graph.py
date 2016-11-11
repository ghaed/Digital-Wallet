"""
A semi-generic graph class to store the payment transactions
The nodes of the graph represent the people and the arcs represent occurred payments.
For the purposes of this anti-fraud project, the Graph class implements the algorithms to perform Breadth-First-Search
(BFS) on the graph. BFS finds the k-th rank neighbours in the graph using a queue data structure
"""


class Graph(object):
    """ Graph class to store the payment network.
    The nodes are the people and the edges are the payment transactions"""
    def __init__(self):
        """ Constructor """
        self.nodes = {}     # Nodes are stored in a hash table for quick access in {id: node_obj} format

    def add_node(self, node_id):
        """ Adds a node to the current graph"""
        self.nodes[node_id] = Node()

    def add_edge(self, id1, id2):
        """ Adds an edge between id1 and id2 to the current graph"""
        self.nodes[id1].add_edge(id2)
        self.nodes[id2].add_edge(id1)

    def to_string(self):
        """ Returns a readable string containing the graph"""
        graph_str = ""
        for node_id in self.nodes:
            graph_str += str(node_id) + ':' + self.nodes[node_id].to_string()
        return graph_str

    def is_node_in_graph(self, node_id):
        """ Returns true if node is indeed in graph
        Args:
            node_id (int): The node to check if it is in the graph

        Returns:
            bool: The return value. True for existence, False if does not exist.
        """
        return node_id in self.nodes

    def distance(self, node_id1, node_id2):
        """ Calculates the distance between two nodes. Uses a breadth-first-search algorithm with queue data structure
        Args:
            node_id1 (int): First node
            node_id2 (int): Second node

        Returns:
            int: distance between node_id1 and node_id2
        """


class Node(object):
    """ Node object that mainly stores the edges connecting to the itself"""
    def __init__(self):
        """ Constructor """
        self.edges = []     # List of ID's of nodes that have direct edges to current node

    def add_edge(self, node_id):
        """ Adds an edge between current node and  another node"""
        self.edges.append(node_id)

    def to_string(self):
        """ Returns the list of edges in string format"""
        return str(self.edges) + '\n'