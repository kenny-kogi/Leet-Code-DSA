
def Search(list_items, item):
    pos = 0

    while pos < len(list_items):
        if list_items[pos] == item:
            return True
        else:
            pos += 1
        
    return False

test_list = [1, 2, 32, 8, 17, 19, 42, 13, 0]
print(Search(test_list, 3))
print(Search(test_list, 32))