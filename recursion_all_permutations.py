# time complexity is O(n! * n) n! for the permutation factorial, n for the work in each permutation
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


print(print_all_permutations([2,3,5], [], defaultdict(bool)))
