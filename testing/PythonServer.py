## compute_input.py

import sys, json, numpy as np

#Read data from stdin
def read_in():
    lines = sys.stdin.readlines()
    #Since our input would only be having one line, parse our JSON data from that
    return json.loads(lines[0])

def main():
    #get our data as an array from read_in()
    #lines = read_in()
    lines = [1,2,3,4,5]
    #create a numpy array
    np_lines = np.array(lines)

    #use numpys sum method to find sum of all elements in the array
    lines_sum = np.sum(np_lines)

    print([0,1])
    # print(lines_sum)

    # print(lines_sum)

    #return the sum to the output stream
 
#start process
if __name__ == '__main__':
    main()