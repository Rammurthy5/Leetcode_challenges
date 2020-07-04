"""
Given an array nums, and an int val, we just need to move instances to the last in-place, and return length of leftover.

"""

from typing import List


def removeElement(nums: List[int], val: int) -> int:
    L = len(nums)
    i = 0
    while i < L:

        if nums[i] == val:

            nums[i] = nums[L - 1]
            L-=1
        else:
            i+=1

    return nums[:L]


print(removeElement([1], 5))



# Approach 2 -- fastest
# i = 0
# for j in range(len(nums)):
#     if (nums[j] != val):
#         nums[i] = nums[j]
#         i += 1
#
# return i