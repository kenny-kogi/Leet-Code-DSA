from pstats import SortKey


def bubble_sort(a_list):
    for i in range(len(a_list) - 1, 0, -1):
        for j in range(i):
            print(j)
            if a_list[j] > a_list[j + 1]:
                a_list[j], a_list[j +1] = a_list[j + 1], a_list[j]

a_list = [54, 26, 93, 17, 77, 31, 44, 55, 20]
bubble_sort(a_list)
print(a_list)

# [19, 1, 9, 7, 3, 10, 13, 15, 8, 12]
# First Sort
# [1, 9, 7, 3, 10, 13, 15, 8, 12, 19]
# Second Sort
# [1, 7, 3, 9, 10, 13, 8, 12, 15, 19]
# Third Sort
# [1, 3, 7, 9, 10, 8, 12, 13, 15, 19]
# Fourth Sort
# [1, 3, 7, 9, 8, 10, 12, 13, 15, 19]
# Fifth Sort
# [1, 3, 7, 8, 9, 10, 12. 13, 15, 19]


