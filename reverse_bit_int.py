# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""


def reverse_bit_integer(x):
    """
    :type x: int
    :rtype: int
    """
    res = 0
    if x >= 0:
        res = int(str(x)[::-1])
    else:
        res = int(str(x)[:0:-1])*-1
  
    if 2**31-1>res>-2**31:
        return res
    else:
        return 0
    

print(reverse_bit_integer(-123))    