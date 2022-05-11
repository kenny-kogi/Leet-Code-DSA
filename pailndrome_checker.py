# def reverse(s):
#     if len(s) == 0:
#         return s
#     else:
#         return reverse(s[1:]) + s[0]
     

def pailndrome(s):
    if len(s) == 1:
        return True
    else:
        a_list = list(s)
        if s == ("").join(a_list[::-1]):
            return True
        else: 
            return False


print(pailndrome("madam"))