# time complexity is O(n * 2^n). space is O(n * 2^n)

def is_palindrome(s, ind, curr_ind):
    actual = s[ind:curr_ind]
    return actual == actual[::-1]

def partition(ind, s, result, res):
    if ind == len(s):
        res.append(result[:])  # append a copy of current partition
        return
    
    for i in range(ind, len(s)):
        if not is_palindrome(s, ind, i + 1):
            continue  # just skip
        result.append(s[ind:i + 1])
        partition(i + 1, s, result, res)
        result.pop()  # backtrack

def all_partitions(s):
    res = []
    partition(0, s, [], res)
    return res

print(all_partitions("aabb"))
