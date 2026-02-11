# time com O(n log n). aux com O(n). 
# using merge sort but a slight change by introducing additional for loop with nested while. 

N = 5
array = [1,3,2,3,1]

def merge_sort(arr):
    if len(arr) <= 1:
        return arr, 0

    mid = len(arr) // 2
    lower_half, left_cnt = merge_sort(arr[:mid])
    upper_half, right_cnt = merge_sort(arr[mid:])

    merged, merge_cnt = merge(lower_half, upper_half)

    return merged, left_cnt + right_cnt + merge_cnt


def merge(left, right):
    cnt = 0
    j = 0

    # Count reverse pairs
    for i in range(len(left)):
        while j < len(right) and left[i] > 2 * right[j]:
            j += 1
        cnt += j

    # Normal merge process
    merged = []
    i = j = 0

    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            j += 1

    merged.extend(left[i:])
    merged.extend(right[j:])

    return merged, cnt

sorted_array, count_reverse_pairs = merge_sort(array)
print(sorted_array)
print(count_reverse_pairs)
