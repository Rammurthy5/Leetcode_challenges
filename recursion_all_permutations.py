# time complexity is O(n! * n) n! for the permutation factorial, n for the work in each permutation
# space complexity is O(n! * n) because we are storing it on hash map. 
from collections import defaultdict


def print_all_permutations(arr, t_arr, hasher):
    if len(t_arr) == len(arr):
        return [t_arr.copy()]

    result = []

    for i in range(len(arr)):
        if not hasher[i]:
            t_arr.append(arr[i])
            hasher[i]=True
            result += print_all_permutations(arr, t_arr, hasher)
            t_arr.pop()
            hasher[i]=False

    return result


# time complexity is same as above but space complexity is optimised by using swap method in-place on original array.
def print_all_permutations_approach2(ind, arr):
    if ind == len(arr):
        return [arr.copy()]

    result = []

    for i in range(ind, len(arr)):
            arr[ind], arr[i] = arr[i], arr[ind]
            result += print_all_permutations_approach2(ind+1, arr)
            arr[ind], arr[i] = arr[i], arr[ind]
    return result


print(print_all_permutations([2,3,5], [], defaultdict(bool)))
print(print_all_permutations(0, [2,3,5]))
