# time complexity O(n)
# aux complexity O(1)

nums = [100, 4, 200, 1, 3, 2]

st = set(nums)
cnt = 1
longest = 1

# we sort the array by moving to set,  iterate the set and do a while for consecutive numbers present in the array. 
# increment counter and compare the max of longest
for i in st:
    x = i
    if x-1 in st:
        continue
    while x+1 in nums:
        cnt+=1
        x=x+1

    longest = max(longest, cnt)
    cnt=1

print(longest)
