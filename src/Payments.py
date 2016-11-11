from Graph import Graph


class Payments(object):
    """ Generic class serving as a wrapper around the Graph class and encapsulates the functions dealing with
    payments"""

    def __init__(self, path_batch, path_stream, path_output1, path_output2, path_output3):
        """ Constructor; also loads up the graph; also opens all file handles"""
        print bcolors.WARNING + "***Loading the batch payment file into a graph***" + bcolors.ENDC
        self.graph = Graph()
        self.f_batch = open(path_batch)  # File handle for the batch file
        self.f_stream = open(path_stream)  # File handle for the stream file
        self.f_output1 = open(path_output1,'w')  # File handle for output1
        self.f_output2 = open(path_output2,'w')  # File handle for output2
        self.f_output3 = open(path_output3,'w')  # File handle for output3
        self.load_graph()  # Load the graph from the batch_payment file
        self.f_stream.readline()  # Skip the first line
        print bcolors.OKGREEN + "***Done initializing the payment graph***" + bcolors.ENDC


    def load_graph(self):
        """ Method to load up the graph from the batch file"""
        lines_batch = self.f_batch.readlines()  # Read the whole batch file at once to avoid unnecessary disk access

        for line in lines_batch[1:]:  # Sweep the batch file and construct the graph network
            elements = line.split(', ')
            node_ids = map(int, elements[1:3])
            for node_id in node_ids:
                if not self.graph.is_node_in_graph(node_id):
                    self.graph.add_node(node_id)
            self.graph.add_edge(node_ids[0], node_ids[1])

    def process_stream_one_line(self):
        """ Processes one line of the stream
        Returns:
            Bool: If successful, returns true, otherwise false
        """
        verified_status = {'feature1': 'Unverified', 'feature2': 'Unverified', 'feature3': 'Unverified'}
        node_ids = self.read_stream_one_line()
        if node_ids is None:
            return False
        if not self.graph.is_node_in_graph(node_id=node_ids[0]) or \
                not self.graph.is_node_in_graph(node_id=node_ids[1]):
            self.write_results_one_line(verified_status=verified_status)
            return verified_status
        distance = self.graph.shortest_path_distance(node_id1=node_ids[0], node_id2=node_ids[1])
        if distance <= 4:  # form the output for write
            verified_status['feature3'] = 'Verified'
        if distance <= 2:
            verified_status['feature2'] = 'Verified'
        if distance <= 1:
            verified_status['feature1'] = 'Verified'
        self.write_results_one_line(verified_status=verified_status)
        return True

    def read_stream_one_line(self):
        """ Reads one line from the batch_payment file
        Returns:
            node_ids (list): List of two nod_ids integers corresponding to the two sides of the transaction.
                also returns None if end-of-file
        """
        line = self.f_stream.readline()
        if line == "":
            return None
        elements = line.split(', ')
        node_ids = map(int, elements[1:3])
        return node_ids

    def write_results_one_line(self, verified_status):
        """ Writes the appropriate verified/unverified conclusions to the 3 output files
        Arguments:
            verified_status (dict): A dictionary of all the outcomes to write to the output files in {'feature1': res}
                format
        """
        self.f_output1.write(verified_status['feature1'] + '\n')
        self.f_output2.write(verified_status['feature2'] + '\n')
        self.f_output3.write(verified_status['feature3'] + '\n')

    def process_stream_all_lines(self):
        """ Processes all lines of the stream. Wrapper around similar function that does one line only"""
        count = 0
        line_process_success = True
        while line_process_success:
            count += 1
            line_process_success = self.process_stream_one_line()
            if count % 10 == 0:
                print bcolors.OKBLUE + "> Processed", count, 'lines of the stream_payment file so far' + bcolors.ENDC

        self.f_batch.close()
        self.f_stream.close()
        self.f_output1.close()
        self.f_output2.close()
        self.f_output3.close()

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'