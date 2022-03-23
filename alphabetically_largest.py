"""
We are given a string S consisting of N letters. We want to find the alphabetically largest letter that occur in both lowercase and upercase in S, or decide there is no such letter

"""

def largestCharacter(str):
    upper_case = [False] * 26
    lower_case = [False] * 26
     
    arr = list(str)
    for c in arr:
        if (c.islower()):
            lower_case[ord(c) - ord('a')] = True
        if (c.isupper()):
            upper_case[ord(c) - ord('A')] = True
             
    # Iterate from right side of array
    # to get the largest index character
    for i in range(25,-1,-1):
         
        # Check for the character if both its
        # uppercase and lowercase exist or not
        if (upper_case[i] and lower_case[i]):
            return chr(i + ord('A')) + ""
    # Return -1 if no such character whose
    # uppercase and lowercase present in
    # string str
    return "NO"
 

 
str = "Codility"
print(largestCharacter(str))
     