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
# math based approach. xsq - ysq = (x+y)(x-y). find x and y. 

def find_missing_repeating_nums(nums):
    n = len(nums)
    local_nums = range(1, n + 1)
    sum_of_nums = sum(nums)
    sum_of_local_nums = sum(local_nums)
    sum_of_squares_of_nums = sum(x ** 2 for x in nums)
    sum_of_squares_of_local_nums = sum(x ** 2 for x in local_nums)
    x_minus_y = sum_of_nums - sum_of_local_nums
    xsquared_minus_ysquared = sum_of_squares_of_nums - sum_of_squares_of_local_nums
    x_plus_y = xsquared_minus_ysquared // x_minus_y
    x = (x_minus_y + x_plus_y) // 2
    y = x_plus_y - x
    print(y, x)
find_missing_repeating_nums(nums)
