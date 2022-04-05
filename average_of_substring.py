def find_averages_of_subarrays(K, arr):
    result = []

    window_sum, window_start = 0.0, 0

    for window_end in range(len(arr)):
        window_sum += arr[window_end]

        if window_end >= K -1:
            result.append(window_sum/K)
            window_sum -= arr[window_start]
            window_start += 1

    return result



def main():
  result = find_averages_of_subarrays(5, [1, 3, 2, 6, -1, 4, 1, 8, 2])
  print("Averages of subarrays of size K: " + str(result))


main()

# [1, 3, 2, 6, -1, 4, 1, 8, 2]

# first substring

# [1, 3, 2, 6, -1]

# second sunstring 

# [3, 2, 6, -1, 4,]

# third Substring

# [2, 6, -1, 4, 1]

# forth substring

# [6, -1, 4, 1, 8,]


