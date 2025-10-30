# time complexity O(2^n)
def print_all_subset_sum(ind, arr, t_arr, summ):
  if ind ==len(arr): # stop when the index is out of bounds
    return [summ]
  t_arr.append(arr[ind])
  include = print_all_subset_sum(ind+1, arr, t_arr, summ+arr[ind]) # include the current element and recurse the next ind
  t_arr.pop()
  exclude = print_all_subset_sum(ind+1, arr, t_arr, summ) # excluse the current ele and recurse the next ind
  return include + exclude

print(print_all_subset_sum(0, [3,1,2],[],0))
