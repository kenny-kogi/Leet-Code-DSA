# -*- coding: utf-8 -*-
"""
Spyder Editor
This is a temporary script file.
"""

def intToRoman(num):
    lookup = {
        "I":1,
        "IV":4,
        "V":5,
        "IX":9,
        "X":10,
        "XL":40,
        "L":50,
        "XC":90,
        "C":100,
        "CD":400,
        "D":500,
        "CM":900,
        "M":1000,
        }
    output = []
    for k, v in reversed(lookup.items()):
        while num > 0:
            if v <= num:
                output.append(k)
                num -= v
            else:
                break
    return "".join(output)

print(intToRoman(3))


def IntToRoman2(num):
    n_dict = {'M': 1000, 'CM': 900, 'D': 500, 'CD': 400, 'C': 100, 'XC': 90, 'L': 50, 'XL': 40,
              'X': 10, 'IX': 9, 'V': 5, 'IV': 4, 'I': 1}
    roman = ""
    for key, val in n_dict.items():
		# print("num", num, "val", val, "res", roman)
        if (num // val):
            count = num // val
            roman += (key * count)
            num = num % val
    return roman
print(IntToRoman2(3))