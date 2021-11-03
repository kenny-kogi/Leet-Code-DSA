# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""


def zigzag(s, numRows):
    if numRows == 1: return s
    
    res =""
    for r in range(numRows):

        increment = 2 * (numRows - 1)
        for i in range(r, len(s), increment):
            res += s[i]
            if (r > 0 and r < numRows -1 and i + increment - 2 * r < len(s)):
                res += s[i + increment - 2 * r]
    
    return res
    
zigzag("PAYPALISHIRING", 3)