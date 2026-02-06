# time com O(n) due to single iteration
# aux com O(n) for hashmap

N = 6
array = [9, -3, 3, -1, 6, -5]
max_subarr = 0
curr_sum = 0
hashed = dict()

def longest_subarray_sum(curr_sum, max_subarr, hashed, N, ar):
    for i in range(N):
        curr_sum+=ar[i]
        if curr_sum==0:
            max_subarr = max(max_subarr, i+1)
        else:
            if curr_sum in hashed:
                max_subarr = max(max_subarr, i+1-hashed[curr_sum])
            else:
                hashed[curr_sum]=i+1
    return max_subarr
max_subarr = longest_subarray_sum(curr_sum, max_subarr, hashed, N, array)

print(max_subarr)
