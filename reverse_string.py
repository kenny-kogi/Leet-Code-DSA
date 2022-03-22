# my_list = ['p','r','o','b','e']

# # last item

# print(my_list[::])


def reverse_string(string):
    return "".join(list(string)[::-1])

print(reverse_string("probe"))