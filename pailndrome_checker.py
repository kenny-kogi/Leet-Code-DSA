def reverse(s):
    if len(s) == 0:
        return s
    else:
        return reverse(s[1:]) + s[0]
     

def pailndrome(s):
    if s == reverse(s):
        return True
    else: 
        return False


print(pailndrome("madam"))