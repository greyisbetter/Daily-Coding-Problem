# -*- coding: utf-8 -*-
"""
Created on Thu Jul  8 09:18:55 2021

@author: Kushan
"""

"""
def cons(a, b):
    return lambda f: f(a, b)

def car(f):
    z = lambda x, y: x
    return f(z)

def cdr(f):
    z = lambda x, y: y
    return f(z)


assert car(cons(3, 4)) == 3
assert cdr(cons(3, 4)) == 4
"""

def cons(a,b):
    def pair(f):
        return f(a, b)
    return pair

def car(pair):
    return pair[0]

def cdr(pair):
    return pair[1]

assert car(cons(3, 4)) == 3
assert cdr(cons(3, 4)) == 4