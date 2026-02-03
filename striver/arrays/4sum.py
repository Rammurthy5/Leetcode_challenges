# time com O(n * n * n); aux O(1)

nums = [1,0,-1,0,-2,2]
target = 0

ans_set = set()
nums.sort()

for f in range(len(nums)-3):
    for s in range(f+1, len(nums)-2):
        left = s+1
        right = len(nums)-1
        while left < right:
            curr_sum = nums[f] +nums[s]+nums[left]+nums[right]
            print(f, s, left, right)
            print(curr_sum)
            if curr_sum == target:
                ans_set.add((nums[f], nums[s], nums[left], nums[right]))
                left +=1
                right = right - 1
            elif curr_sum > target:
                right = right -1
            elif curr_sum < target:
                left += 1
                
print(ans_set)
