# [2, 3, 4, 1, 5]
# ans = 7
# sub_array = [3, 4]

# def max_sum_subarray(K, arr):
#     result = []
#     window_sum, window_start = 0.0, 0

#     for window_end in range(len(arr)):
#         window_sum += arr[window_end]

#         if window_end >= K - 1:
#             result.append(window_sum)
#             window_sum -= arr[window_start]
#             window_start += 1

#     return result



def max_sub_array_of_size_k(k, arr):
  max_sum = 0
  window_sum = 0
  print(len(arr) - k + 1)
  for i in range(len(arr) - k + 1):
    print(i)
    window_sum = 0
    for j in range(i, i+k):
      window_sum += arr[j]
    max_sum = max(max_sum, window_sum)
  return max_sum


def main():
  #print("Maximum sum of a subarray of size K: " + str(max_sub_array_of_size_k(3, [2, 1, 5, 1, 3, 2])))
  print("Maximum sum of a subarray of size K: " + str(max_sub_array_of_size_k(2, [2, 3, 4, 1, 5])))


main()




