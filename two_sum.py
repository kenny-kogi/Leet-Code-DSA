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

def two_sum(nums, target):
    solution = [[i_a, i_b] for i_a, a in enumerate(nums) for i_b, b in enumerate(nums)  if a +b == target and i_a != i_b]
    print(solution[0])


two_sum([2,7,11,15], 9)
