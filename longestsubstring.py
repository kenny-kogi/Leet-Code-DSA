# -*- coding: utf-8 -*-


def longest_substring(s):
    l = len(s)
    d = {}
    i = 0
    ans = 0
    for j in range(l):
        # print(j)
        if s[j] in d:
            i=max(d[s[j]],i)
        else:
            d[s[j]] = j + 1
            ans=max(ans,j-i+1)
    return ans
     
print(longest_substring("pwwkew"))   

#     d = {}
#     i = 0
#     l = len(s)
#     ans= 0
#     for j in range(l):
#         if s[j] in d:
#             i = max(d[s[j]], i)
#         else:
#             d[s[j]] = j + 1
#             ans = max(ans, j - i + 1)
#     return ans




    
    
    
