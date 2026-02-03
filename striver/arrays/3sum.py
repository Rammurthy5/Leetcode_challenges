# time com O(n * n) 
# aux O(1) we dont use extra space except to store answer set

nums = [-1,0,1,2,-1,-4]
target = 0

ans_set = set()
nums.sort()

for f in range(len(nums)):
    for s in range(f, len(nums)):
        left = s+1
        right = len(nums)-1
        while left < right:
            curr_sum = nums[f]+nums[left]+nums[right]
            print(f, left, right)
            print(curr_sum)
            if curr_sum == target:
                ans_set.add((nums[f], nums[left], nums[right]))
                left +=1
                right = right -1
            elif curr_sum > target:
                right = right -1
            elif curr_sum < target:
                left += 1
                
print(ans_set)
