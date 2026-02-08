# time com O(n) aux com O(n) 

nums = [3, 5, 4, 1, 1]
nums_set = set(range(1, len(nums) + 1))

def find_missing_repeating_nums(nums):
    for i in range(len(nums)):
        if nums[i] in nums_set:
            nums_set.remove(nums[i])
        else:
            repeating_num = nums[i]
    missing_num = nums_set.pop()
    print([repeating_num, missing_num])

find_missing_repeating_nums(nums)

# time complexity O(n) and aux com O(1)

def find_missing_repeating_nums(nums):
    n = len(nums)
    xor_all = 0

    for i in range(n):
        xor_all ^= nums[i]
        xor_all ^= (i + 1)

    rightmost_set_bit = xor_all & -xor_all

    x = y = 0
    for num in nums:
        if num & rightmost_set_bit:
            x ^= num
        else:
            y ^= num

    for i in range(1, n + 1):
        if i & rightmost_set_bit:
            x ^= i
        else:
            y ^= i

    # determine which is repeating
    if nums.count(x) == 2:
        return [x, y]
    else:
        return [y, x]
