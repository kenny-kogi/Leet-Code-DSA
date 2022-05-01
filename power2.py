# The following function prints the powers of 2 from 1 through n (inclusive). For example, if n is 4, it would
# print 1, 2, and 4.
def powerOf2(n):
    if (n < 1):
        return 0
    elif (n == 1):
        print(1)
    else:
        prev = powerOf2(n / 2)
        curr = prev * 2
        print(curr)

powerOf2(4)