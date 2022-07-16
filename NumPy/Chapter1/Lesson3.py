#indexing slicing and iterating

import numpy as np
import math

a = np.array([[1,2],[3,4],[5,6]])

def index():
    print(a[0,0])
    print (a[1,1])

def array_of_indexes():
    b = np.array([[a[0,0],a[1,1],a[2,1]]])
    print (b)

def boolean_indexing():
    print (a > 5)

def conditional_indexing():
    print (a[a>5])

def slicing():
    a = np.array([1,2,3,4,5])
    print(a[:3])
    print(a[2:4])
