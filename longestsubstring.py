# -*- coding: utf-8 -*-


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






    
    
    
