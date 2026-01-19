# find majority ele in an array 
# time complexity O(n) using Moore's voting algorithm

nums = [7, 0, 1, 7, 7, 2, 3,3]

cnt = 1
ele = nums[0]

for i in range(1, len(nums)-1):
    if nums[i]==ele:
        cnt+=1
    else:
        cnt-=1
    if cnt==0:
       ele = nums[i+1]

cnt1 = 0
for i in nums:
    if i==ele:
        cnt1+=1

if cnt1> len(nums)//2:
    print(ele)
else:
    print("-1")
