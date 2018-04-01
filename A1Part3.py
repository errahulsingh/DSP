
"""
Complete the function hopSamples(x,M) in the file A1Part3.py so that given a
numpy array x, the function returns every Mth element in x, starting from the
first element.

The input arguments to this function are a numpy array x and a positive
integer M such that M is less than the number of elements in x. The output of
this function should be a numpy array.

If you run your code with x = np.arange(10) and M = 2, the function should
return the following output: array([0, 2, 4, 6, 8]).
def hopSamples(x,M):
"""
    """
    Inputs:
    x: input numpy array
    M: hop size (positive integer)

    Output:
    A numpy array containing every Mth element in x, starting
    from the first element in x.
    """
    ## Your code here

---

# A1Part3.py
"""! PYTHON 3 !"""


import numpy as np
from scipy.io.wavfile import read
import sys
import utilFunctions as UF


def hopSamples(x,M):
    inputFile='../../sounds/oboe-A4.wav'
    print("Input File: ", inputFile)
    (fs, x) = UF.wavread(inputFile)
    y = x[0:10]
    np_a = np.arange(y)
    print( "np_a:", np_a)

print(hopSamples())


