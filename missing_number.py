# average solution takes O(n) time, and O(1) space. O(2n)
# gauss formula takes O(n) time though gauss formula takes O(1) but our sum(nums) takes n, and O(1) space. this is better because this is O(n)+1

class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        # average solution
        #return sum([i for i in range(len(nums)+1)]) - sum(nums)

        # Best solution - Gauss formula ∑ to find sum of natural numbers n(n+1)/2

        expected = len(nums)*(len(nums)+1)//2
        actual= sum(nums)
        return int(expected - actual)
      
 
