#!/usr/bin/python

import sys

def main():
    # print command line arguments
    path_batch = sys.argv[1]
    path_stream = sys.argv[1]
    path_stream = sys.argv[1]
    for arg in sys.argv[1:]:
        print arg

if __name__ == "__main__":
    main()



'''Detects suspicious transactions'''
from Graph import Graph
from Payments import Payments

path_trans = '../insight_testsuite/tests/test-2-paymo-trans/'   # The root folder for transaction files
payments = Payments(path_trans=path_trans)

print payments.graph.to_string()
print payments.graph.shortest_path_distance(node_id1=1, node_id2=6)
print payments.graph.to_string()
payments.process_stream_all_lines()
