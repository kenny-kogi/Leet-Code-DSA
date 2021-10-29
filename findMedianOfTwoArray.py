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


def findMedianOfTwoArrays(nums1, nums2):
    new_nums = sorted(nums1 + nums2)
    length = len(new_nums)
    
    if length == 0:
        return 0
    elif (length != 0):
        return float(new_nums[length//2 - 1] + new_nums[length//2])/2
    else:
        return new_nums[length / 2] 


print(findMedianOfTwoArrays([1,2], [3,4]))