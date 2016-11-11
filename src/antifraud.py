#!/usr/bin/python

import sys
from Payments import Payments

def main():
    path_batch = sys.argv[1]
    path_stream = sys.argv[2]
    path_output1 = sys.argv[3]
    path_output2 = sys.argv[4]
    path_output3 = sys.argv[5]

    payments = Payments(path_batch, path_stream, path_output1, path_output2, path_output3)
    payments.process_stream_all_lines()     # Processes all lines in the stream file and writes the results to the
                                            # three output files
if __name__ == "__main__":
    main()