# using Boyer-Moore's algorithm
# time com O(n) and Aux com O(1)

nums =  [1, 2, 1, 1, 3, 2, 2]

cnt1 = cnt2 = 0
ele1 = ele2 = None

target = len(nums)//3


for num in nums:
    if num == ele1:
        cnt1 += 1
    elif num == ele2:
        cnt2 += 1
    elif cnt1 == 0:
        ele1 = num
        cnt1 = 1
    elif cnt2 == 0:
        ele2 = num
        cnt2 = 1
    else:
        cnt1 -= 1
        cnt2 -= 1

result = []
if nums.count(ele1) > target:
    result.append(ele1)
if ele2 != ele1 and nums.count(ele2) > target:
    result.append(ele2)

print(result)
