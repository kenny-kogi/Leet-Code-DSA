MAX_CHARS = 256

def unique_characters(str):
    n = len(str)

    if n > MAX_CHARS:
        return False
    
    chars = [False] * MAX_CHARS
    print(chars)

    for i in range(n):
        index = ord(str[i])
        if chars[index] == True:
            return False
        chars[index] = True

    return True

print(unique_characters("HELO"))
