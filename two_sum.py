# -*- coding: utf-8 -*-
"""
greatest common divisor (20, 12)

x/y
20/12 = 1 rem 8
12/8 = 1 rem 4
8/4 = 1 rem 0

"""

def euclid(x, y):
    if y == 0:
        x, y = x, y
    while (y != 0):
        x, y = y, x % y
    return x
    
print(euclid(20, 12))