#######################################################################
# MAD:
#   
#######################################################################
import math
import logging
import random

import matplotlib
matplotlib.use('TkAgg')

import matplotlib.pyplot as plt


#######################################################################
def signal1( x ):

    t1 = 2.0 * x / 5.0
    t2 = x / 40.0 - 1.0
    fx = math.cos(t1) + t2 * t2 * t2
    return fx

#######################################################################
def signal2( x ):

    t1 = x / 10.0
    t2 = x / 50.0
    fx = math.sin(t1) + t2 * t2
    return fx

#######################################################################
def signal3( x ):

    return 10.0 * x

    
#######################################################################
def generate_signal( signal, num_steps, delta_time ):

    x = []
    y = []

    t = 0.0

    for i in range(num_steps):

        s = signal(t)
        
        x.append(t)
        y.append(s)

        t += delta_time
        
    return (x, y)

#######################################################################
def stat_signal( x, y ):

    N = len(x)
    if len(y) != N:
        logging.error("The series x, y have different lengths")
        exit(1)

    avg = 0.0

    for i in range(N):
        avg += y[i]

    avg /= N

    var2 = 0.0

    for i in range(N):
        tmp = y[i] - avg
        var2 += tmp * tmp
        
    var2 /= N

    return (avg, var2)

#######################################################################
def add_noise( x, y, noise ):

    N = len(x)
    if len(y) != N:
        logging.error("The series x, y have different lengths")
        exit(1)

    for i in range(N):
        
        r = random.gauss(0.0, noise)
        y[i] += r
        


#######################################################################
def main():

    logging.basicConfig( level=logging.DEBUG )
    
    ##############################################
    # Parse command line arguments

    import argparse

    parser = argparse.ArgumentParser(description="Command to generate test time signals")

    parser.add_argument("--hz", "-s", help="signal sampling in Hz", type=float, default=30.0)
    parser.add_argument("--time", "-t", help="signal time length in seconds", type=float, default=1.0)
    parser.add_argument("--decibel", "-db", help="noise added in decibels", type=float)
    parser.add_argument("--out", "-o", help="output file name")
    parser.add_argument("--signal", help="signal function to use [1,2]", type=int, default=1)
    parser.add_argument("--display", help="display signal", action='store_true')
    
    args = parser.parse_args()

    # If not out file specified write to console
    outpath = None
    if args.out:
        outpath = args.out

    # If no noise level specified add no noise
    noise = None
    if args.decibel:

        noise = math.pow( 10.0, -args.decibel/10.0 )
        
    # Hz/timestep
    delta_time = 1.0 / args.hz
    time       = args.time
    num_steps  = int(time/delta_time)

    # Choose signal function
    signal = None

    if args.signal == 1:
        signal = signal1
        
    elif args.signal == 2:
        signal = signal2

    elif args.signal == 3:
        signal = signal3

    else:

        logging.error( "signal function selected is not supported" )
        exit(1)
        

    ##############################################
    # Generate time signal
    (x, y) = generate_signal( signal, num_steps, delta_time )
    (avg, var2) = stat_signal(x,y)


    ##############################################
    # Add noise to signal if needed
    if noise:

        add_noise( x, y, avg * noise )


    ##############################################
    # Display time signal
    if args.display:

        plt.figure(1)
        plt.plot( x, y )
        plt.xlabel('x (seconds)')
        plt.ylabel('y(x)')
        plt.show()
        
    
    ##############################################
    # Output signal
    if not outpath:

        for i in range(num_steps):
            
            print "{:.6f} {:.6f}".format( x[i], y[i] )
            
    else:

        out = open( outpath, "wt")
        
        for i in range(num_steps):
            
            out.write( "{:.6f} {:.6f} \n".format( x[i], y[i] ) )
        
        out.close()

    

#######################################################################
if __name__ == '__main__':

    main()
    
