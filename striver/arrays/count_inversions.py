# using merge sort way. time com O(n log n) aux com O(n)

N = 5
array = [5,4,3,2,1]

def merge_sort(arr):
    if len(arr) <= 1:
        return arr, 0

    mid = len(arr) // 2
    lower_half, left_cnt = merge_sort(arr[:mid])
    upper_half, right_cnt = merge_sort(arr[mid:])

    merged, merge_cnt = merge(lower_half, upper_half)

    return merged, left_cnt + right_cnt + merge_cnt


def merge(left, right):
    merged = []
    i = j = 0
    cnt = 0

    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            merged.append(left[i])
            i += 1
        else:
            # all remaining elements in left are inversions
            cnt += len(left) - i
            merged.append(right[j])
            j += 1

    merged.extend(left[i:])
    merged.extend(right[j:])
    return merged, cnt


sorted_array, count_invs = merge_sort(array)
print(sorted_array)
print(count_invs)
