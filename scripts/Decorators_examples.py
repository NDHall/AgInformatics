import sys, os, math, random, functools
import numpy as np
import matplotlib
import matplotlib.pyplot as pp
import matplotlib.animation as anim

#from IPython.display import display, HTML

def printargs(func):
    def decorated(*args,**kwargs):
        print("Function{} called with args = {} and kwargs -{}".format(func.__name__,args,kwargs))
        return func(*args,**kwargs)
    return decorated

@printargs
def fibonacci(n,tag=None):
    """

    :param n: integer
    :return: number in the Fibonacci sequence
    """

    if n<2:
        return n
    return fibonacci(n-1 ,tag='1') + fibonacci(n-2,tag=2)
    #return (n - 1,tag='1' ) + (n -2)
print(fibonacci(5))


print("start LL")

@printargs
def lessLonely(func):
    def decorated(*args):
        print('{} is less lonely than {}'.format(*args,func(*args)))
        return func(*args)
    return decorated

print('start addone()')

@functools.lru_cache(maxsize=None)
@lessLonely
@printargs
def addone(n):
    """
    adds 1 to number
    """
    return n +1

print("start\n\n\n")
print("first:",addone(3))
print("second:",addone(3))
print("third:" ,addone(3))

@printargs
@functools.lru_cache(maxsize=None)
def fib(n):
    if n < 2:
        return n
    return fib(n-2) +fib(n-1)

print(fib(4))
print(fib(7))