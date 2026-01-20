nums = [2, 3, 5, -2, 7, -4]  

max_sum = float('-inf')
summ = nums[0]

for i in range(1, len(nums)):
    if (nums[i]+summ) >-1:
       summ += nums[i]
       max_sum = max(max_sum, summ) 
    else:
       summ = 0

max_sum = max(summ, max_sum)
print(max_sum)

# time comp O(n)
# aux com O(1)
# uses kadane's 
