"""
Given a sorted array remove duplicates

"""

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        k = 0
        # I = 1
        if len(nums) == 0:
            return 0
        for i in range(1, len(nums)):
            if nums[i] != nums[k]:
                nums[k + 1] = nums[i]
                k += 1
            # I =i
        return k + 1



