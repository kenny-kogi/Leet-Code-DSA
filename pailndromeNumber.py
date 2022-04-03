# -*- coding: utf-8 -*-

def max_area(height): 
        l = 0
        r = len(height)-1
        res = 0
        while l < r:
            if height[l] < height[r]:
                res = max(res, height[l]*(r-l))
                l += 1
            else:
                res = max(res, height[r]*(r - l))
                r -= 1                       
        return res




print(max_area([1,8,6,2,5,4,8,3,7]))