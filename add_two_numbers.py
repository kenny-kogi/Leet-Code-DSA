# -*- coding: utf-8 -*-

def longestPalindrome(s):
    res = ""
    resLength = 0
    
    for i in range(len(s)):
        """
        Odd length
        """
        l, r = i, i
        while l >= 0 and r < len(s) and s[l] == s[r]:
            if (r - l + 1) > resLength:
                res = s[l:r+1]
                resLength = r - l + 1
            l -= 1
            r += 1
        """
        even length
        """
        l, r = i, i + 1
        while l >= 0 and r < len(s) and s[l] == s[r]:
            if (r - l + 1) > resLength:
                res = s[l:r+1]
                resLength = r - l + 1
            l -= 1
            r += 1
    return res 
        
print(longestPalindrome("ababb"))

"""
ababb




"""