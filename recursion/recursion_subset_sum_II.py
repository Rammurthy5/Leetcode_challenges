# time complexity is O(2^n * k) k is the avg size of subset
def print_all_unique_subsets(ind, arr, t_arr):
  result = []

  result.append([t_arr.copy()]) # include the current subset

  for i in range(ind, len(arr)):
    if i>ind and arr[i] == arr[i-1]:
      continue
    t_arr.append(arr[i])
    result += print_all_unique_subsets(i+1, arr, t_arr) # recurse
    t_arr.pop() # backtracking
  return result
