# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""




"""
greatest common divisor (20, 12)

x/y
20/12 = 1 rem 8
12/8 = 1 rem 4
8/4 = 1 rem 0

"""

def longest_substring(s):
    l = len(s)
    d = {}
    i = 0
    ans = 0
    for j in range(l):
        if s[j] in d:
            i=max(d[s[j]],i)
        d[s[j]] = j + 1
        ans=max(ans,j-i+1)
    return ans
     
print(longest_substring("pwwkew"))   
    
    
    
