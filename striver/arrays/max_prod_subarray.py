n = [-2, -3, -4]

# O(2n) time and O(1) space

def max_prod_subarray(arr):
    if not arr:
        return 0

    max_product = float('-inf')
    prod = 1

    # Left to right
    for num in arr:
        prod *= num
        max_product = max(max_product, prod)
        if prod == 0:
            prod = 1

    # Right to left
    prod = 1
    for num in reversed(arr):
        prod *= num
        max_product = max(max_product, prod)
        if prod == 0:
            prod = 1

    return max_product

print(max_prod_subarray(n))

# most optimal O(n) time and O(1) space
def max_prod_subarray2(arr):
    if not arr:
        return 0
    result = arr[0]   
    max_prod = arr[0]
    min_prod = arr[0]
    
    for i in range(1, len(arr)):
        if arr[i] < 0:
            min_prod, max_prod = max_prod, min_prod
        min_prod = min(arr[i], arr[i] * min_prod)
        max_prod = max(arr[i], arr[i] * max_prod)
        result = max(max_prod, result)
    return result

print(max_prod_subarray2(n))
