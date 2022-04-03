def binary_search(list_item, item):
    first = 0
    last = len(list_item) - 1

    while first <= last:
        midpoint = (first + last) // 2

        if list_item[midpoint] == item:
            return True
        elif (item < list_item[midpoint]):
            last = midpoint - 1
        else:
            first = midpoint + 1
    
    return False

listOfItems = [1, 2 , 3, 4, 5, 6, 7, 8]

print(binary_search(listOfItems, 3))
print(binary_search(listOfItems, 10))


# Using Recursive

def binary_search_rec(list_items, item):
    if len(list_items) == 0:
        return False
    else:
        midpoint = len(list_items) // 2

        if list_items[midpoint] == item:
            return True
        elif (item < list_items[midpoint]):
            return binary_search_rec(list_items[:midpoint], item)
        else:
            return binary_search_rec(list_items[midpoint + 1:], item)

listOfItems = [1, 2 , 3, 4, 5, 6, 7, 8]
print(binary_search_rec(listOfItems, 7))
print(binary_search_rec(listOfItems, 10))


# def midpoint(list_item):
#     first = 0
#     last = len(list_item) - 1
#     return (first + last) // 2


# print(midpoint([3, 5, 6, 8, 11, 12, 14, 15, 17, 18]))