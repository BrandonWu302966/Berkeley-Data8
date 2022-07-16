#basic numpy array operations and functions

import numpy as np
import math
import random



def basic():
    a = np.array([1,2,3])
    print (a)

def num_dimensions():
    a = np.array([1,2,3])
    print(a.ndim)

def multidimensional():
    b = np.array([[1,2,3],[4,5,6]])
    print(b)

def dimensions():
    b = np.array([[1,2,3],[4,5,6]])
    print(b.shape)

def arraytype():
    c = np.array([2.2,5,1.1])
    print(c.dtype)

def zeroes():
    d = np.zeros((2,3))
    print(d)

def ones():
    e = np.ones((2,3))
    print(e)

def randarray():
    r = np.random.rand(2,3)
    print(r)

def steps():
    f = np.arange(10,50,2)
    print(f)

def float_steps():
    g = np.linspace(0,2,5)
    print(g)

def array_operations():
    a = np.array([10,20,30,40])
    b = np.array([1,2,3,4])
    c = a-b
    d = a*b
    e = a/2
    print(c)
    print(d)
    print(e)

def boolean_array():
    a = np.array([10,20,30,40])
    b = np.array([1,2,3,4])
    c = a-b
    print(c<12)

def multiply():
    a = np.array([[1,1],[0,1]])
    b = np.array([[2,0],[3,4]])
    print(a*b)

def dot_product():
    a = np.array([[1,1],[0,1]])
    b = np.array([[2,0],[3,4]])
    print(a@b)

def diff_types():
    array1 = np.array([[1,2,3],[4,5,6]])
    array2 = np.array([[7.1,8.2,9.1],[10.4,11.2,12.3]])
    array3 = array1 + array2
    print(array3)
    print(array3.dtype)

def array_functions():
    array3 = np.array([[1,2,3],[4,5,6]])
    print(array3.sum())
    print(array3.max())
    print(array3.min())
    print(array3.mean())

def step_array_with_dimensions():
    a = np.arange(1,16,1)
    a = a.reshape(3,5)
    print(a)




