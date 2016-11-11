'''Detects suspicious transactions'''
from Graph import Graph

trans_folder = '../insight_testsuite/tests/test-2-paymo-trans/'   # The root folder for transaction files
f_batch = open(trans_folder+'paymo_input/batch_payment.txt')    # File handle for the batch file
f_stream = open(trans_folder+'paymo_input/stream_payment.txt')  # File handle for the stream file

lines_batch = f_batch.readlines()   # Read the whole batch file at once to avoid unnecessary disk access
g = Graph()

for line in lines_batch[1:]:    # Sweep the batch file and construct the graph network
    elements = line.split(', ')
    node_ids = map(int, elements[1:3])
    for node_id in node_ids:
        if not g.is_node_in_graph(node_id):
            g.add_node(node_id)
    g.add_edge(node_ids[0], node_ids[1])


print g.to_string()
print g.shortest_path_distance(node_id1=1, node_id2=6)
print g.to_string()
