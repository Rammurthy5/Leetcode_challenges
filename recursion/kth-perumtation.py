# time complexity is O(n^2). space is O(n)
def findFactorial(n):
  return 1 if n==0 else n * findFactorial(n-1)

def perm_array(n):
  return [i for i in range(1, n+1)]

def findPartition(n, k, total_perms, p_array, res):
  if n == 0:
    return res
  partition = total_perms // n
  ind, k = divmod(k, partition)
  res.append(p_array[ind])
  p_array.pop(ind)
  return findPartition(n-1, k, findFactorial(n-1), p_array, res)

print(findPartition(3, 3-1, findFactorial(3), perm_array(3), []))

# Input:
# n = 3
# k = 3
# Output: "213"

# optimized version time is O(n)

def getPermutation(n, k):
    # Step 1: Precompute factorials
    factorial = [1] * (n + 1)
    for i in range(1, n + 1):
        factorial[i] = factorial[i - 1] * i

    # Step 2: Initialize numbers array
    numbers = [i for i in range(1, n + 1)]
    k -= 1  # convert k to 0-indexed
    res = []

    # Step 3: Build the permutation
    for i in range(n, 0, -1):
        idx = k // factorial[i - 1]
        res.append(numbers[idx])
        numbers.pop(idx)
        k %= factorial[i - 1]

    return res

# Example
print(getPermutation(3, 3))  # Output: [2, 1, 3]

