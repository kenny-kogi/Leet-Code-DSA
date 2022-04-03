# -*- coding: utf-8 -*-

def myAtoi(self, s: str) -> int:
    s1 = s.split()
    a= 0
    try:
        for i in range(len(s1[0])):
            if s1[0][i].isdigit():
                a = int(s1[0][:i+1])
    except:
        pass
    if a <= -2**31:
        a = -2**31
    elif a>= 2**31:
        a = 2**31-1
    return a