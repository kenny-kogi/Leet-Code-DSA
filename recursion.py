# def sum_list(list_num):
#     if len(list_num) == 1:
#         return list_num[0]
#     else:
#         return list_num[0] + sum_list(list_num[1:])

# print(sum_list([1,2,3,4,5]))

# def factorial(num):
#     if num <= 1:
#         return 1
#     else:
#         return num * factorial(num - 1)

# print(factorial(5))


# def to_str(n, base):
#    convert_string = "0123456789ABCDEF"
#    if n < base:
#       return convert_string[n]
#    else:
#       return  to_str(n // base, base) + convert_string[n % base] 

# print(to_str(10, 2)) 


def reverse(s):
    if len(s) == 0:
        return s
    else:
        return reverse(s[1:]) + s[0]               

s = "Geeksforgeeks"
  
print ("The original string  is : ",end="")
print (s)
  
print ("The reversed string(using recursion) is : ",end="")
print (reverse(s))

