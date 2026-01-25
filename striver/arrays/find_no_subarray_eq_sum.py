# find the count of number of subarrays sum upto "k"
# time com O(n) using sliding window technique. Aux O(1)

N = 4
array = [3, 1, 2, 4]
k = 6
counter = 0

def base_iter(arr, counter):
    for i in range(len(array)):
        counter+=int(find_sub_arr(array[i:]))
    print(counter)

def find_sub_arr(arr, k=k):
    tot = arr[0]
    for i in arr[1:]:
        if tot==k:
           return 1
        if tot > k:
           return 0
        tot+=i
    if tot==k:
        return 1
    return 0
base_iter(array, counter)  # O(n*n) brute force approach


# optimal O(n) using sliding window
left = 0
tot = 0
for right in range(len(array)):
     tot+=array[right]
     while tot > k  and left <=right:
         tot-=array[left]
         left+=1
     if tot==k:
         counter+=1

print(counter)
