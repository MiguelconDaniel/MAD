#######################################################################
# MAD:
#   
#######################################################################
import math
import logging
import random
import os

import matplotlib
matplotlib.use('TkAgg')

import matplotlib.pyplot as plt


#######################################################################
def load_data( path ):

    x = []
    y = []
    
    if not os.path.exists(path):
        logging.error("Unable to find the file {}".format(path))
        exit(1)

    f = open(path, "rt")
    line = f.readline().strip()

    while(line):

        (xi, yi) = line.split()
        x.append( float(xi) )
        y.append( float(yi) )
        
        line = f.readline().strip()
    
    return (x,y)

#######################################################################
def display1( x, y ):

    plt.plot( x, y )
    plt.xlabel("t (s)")
    plt.ylabel("y(t)")
    plt.show()

    

#######################################################################
def display2( x1, y1, x2, y2 ):

    plt.plot( x1, y1 )
    plt.plot( x2, y2, linestyle="--" )
    plt.xlabel("t (s)")
    plt.ylabel("y(t)")
    plt.show()



#######################################################################
def main():

    logging.basicConfig( level=logging.DEBUG )
    
    ##############################################
    # Parse command line arguments

    import argparse

    parser = argparse.ArgumentParser(description="Command to generate test time signals")
    parser.add_argument("--input", "-i", help="input files", type=str, nargs="*")
    
    args = parser.parse_args()

    if args.input:

        if len(args.input) == 1:

            file1 = args.input[0]
            (x,y) = load_data(file1)

            display1( x, y )
            
        elif len(args.input) == 2:

            file1 = args.input[0]
            (x1,y1) = load_data(file1)

            file2 = args.input[1]
            (x2,y2) = load_data(file2)

            display2( x1, y1, x2, y2 )
            
    

#######################################################################
if __name__ == '__main__':

    main()
    
