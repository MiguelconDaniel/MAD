#######################################################################
# MAD:
#       Miguel & Daniel Sepulveda    2017
#   
#######################################################################
import math
import logging
import random
import numpy

#######################################################################
def kernel_epanechnikov(u):

    us = math.fabs(u)

    k = 0.0
    if us <= 1.0:
        k = 0.75 * ( 1.0 - us * us )

    return k

#######################################################################
def linear_regression( m, x, y):

    if m <= 1:

        logging.error("Not enough points provided for linear regression m={}".format(m) )
        exit(1)

    if len(x) < m:

        logging.error("Not enough points provided for linear regression m={} len(x)={}".format(m, len(x)) )
        exit(1)

    if len(y) < m:

        logging.error("Not enough points provided for linear regression m={} len(y)={}".format(m, len(y)) )
        exit(1)

        
    Sxi   = 0.0
    Sxi2  = 0.0
    Sxiyi = 0.0
    Syi   = 0.0

    for i in range(m):

        Sxi   += x[i]
        Syi   += y[i]
        Sxi2  += x[i] * x[i]
        Sxiyi += x[i] * y[i]

    # transpose(A) * A
    ATA = numpy.matrix( [[ m, Sxi] , [Sxi, Sxi2]] )

    # Y array
    Y = numpy.array( [Syi, Sxiyi] )

    # Find inverse
    ATAi = numpy.linalg.inv(ATA)

    # Regression coefficients
    Beta = numpy.dot(ATAi, Y)
    
    return (Beta[0,0], Beta[0,1])
        


#######################################################################
def quadratic_regression( m, x, y):

    if m <= 1:

        logging.error("Not enough points provided for linear regression m={}".format(m) )
        exit(1)

    if len(x) < m:

        logging.error("Not enough points provided for linear regression m={} len(x)={}".format(m, len(x)) )
        exit(1)

    if len(y) < m:

        logging.error("Not enough points provided for linear regression m={} len(y)={}".format(m, len(y)) )
        exit(1)

    Sxi    = 0.0
    Syi    = 0.0
    Sxi2   = 0.0
    Sxi3   = 0.0
    Sxi4   = 0.0
    Syixi  = 0.0
    Syixi2 = 0.0

    for i in range(m):

        Sxi += x[i]
        Syi += y[i]

        xi2 = x[i] * x[i]
        xi3 = xi2 * x[i]
        xi4 = xi3 * x[i]

        Sxi2 += xi2
        Sxi3 += xi3
        Sxi4 += xi4

        Syixi  += y[i] * x[i]
        Syixi2 += y[i] * xi2


    # transpose(A) * A
    ATA = numpy.matrix( [[ m, Sxi, Sxi2] , [Sxi, Sxi2, Sxi3], [Sxi2, Sxi3, Sxi4]] )

    # Y array
    Y = numpy.array( [Syi, Syixi, Syixi2] )

    # Find inverse
    ATAi = numpy.linalg.inv(ATA)

    # Regression coefficients
    Beta = numpy.dot(ATAi, Y)
    
    return (Beta[0,0], Beta[0,1], Beta[0,3])
        
        
