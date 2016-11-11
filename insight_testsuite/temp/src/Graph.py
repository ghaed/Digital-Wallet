import Queue


class Graph(object):
    """ Graph class to store the payment network.
    The nodes are the people and the edges are the payment transactions.
    A semi-generic graph class to store the payment transactions
    The nodes of the graph represent the people and the arcs represent occurred payments.
    For the purposes of this anti-fraud project, the Graph class implements the algorithms to perform
    Breadth-First-Search(BFS) on the graph. BFS finds the k-th rank neighbours in the graph using a queue data structure
    The BFS method is shortest_path_distance() which only returns the shortest path distance between two nodes.
    The idea is that this method will be called whenever a new pair appears in the input stream.
    Alternatively, we could have stored all the calculated distances so far in the Graph object to avoid re-calculating
    them in the future. This, however, would require O(n^2) space to store as the input stream comes in and exercises
    all the paths in the graph. As a result, I made a decision, to keep it simple and do a minimal terminating BFS every
    time a new input arrives.
    """
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

    def shortest_path_distance(self, node_id1, node_id2):
        """ Calculates the distance between two nodes. Uses a breadth-first-search algorithm with queue data structure
        Args:
            node_id1 (int): First node
            node_id2 (int): Second node

        Returns:
            int: distance between node_id1 and node_id2. If there is no path, returns -1
        """
        self.clear_bfs()
        q = Queue.Queue()   # Stores the FIFO list of items to search in a breadth-first search
        self.nodes[node_id1].is_explored = True     # Mark the origin as explored
        self.nodes[node_id1].layer = 0  # Label the starting node as layer 0 with minimum distance of 0 to itself
        q.put(node_id1)
        while not q.empty():    # Sweep through the queue via breadth-first-search
            node_id = q.get()
            for edge in self.nodes[node_id].edges:
                if not self.nodes[edge].is_explored:
                    self.nodes[edge].is_explored = True
                    self.nodes[edge].layer = self.nodes[node_id].layer + 1
                    q.put(edge)
                    if edge == node_id2:    # If breadth-first-search reaches node_id2, stop the search and return
                        return self.nodes[node_id2].layer
        return -1

    def clear_bfs(self):
        """ Clears the layers and the is_explored flags so that breadth-first-search can do a fresh start """
        for node_id in self.nodes:
            self.nodes[node_id].is_explored = False
            self.nodes[node_id].layer = -1


class Node(object):
    """ Node object that mainly stores the edges connecting to the itself. Also contains distance informations"""
    def __init__(self):
        """ Constructor """
        self._edges = []     # List of ID's of nodes that have direct edges to current node
        self._is_explored = False
        self._layer = -1     # The distance from source node to current node

    def add_edge(self, node_id):
        """ Adds an edge between current node and  another node"""
        self.edges.append(node_id)

    def to_string(self):
        """ Returns the list of edges in string format"""
        return str(self.edges) + ', layer=' + str(self._layer) + '\n'

    @property
    def edges(self):
        return self._edges

    @property
    def is_explored(self):
        return self._is_explored

    @is_explored.setter
    def is_explored(self, value):
        self._is_explored = value

    @property
    def layer(self):
        return self._layer

    @layer.setter
    def layer(self, value):
        self._layer = value