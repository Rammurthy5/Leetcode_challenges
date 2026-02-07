# time com O(n) aux com O(1)

nums1 = [-5, -2, 4, 5, 0, 0, 0]
nums2 = [-3, 1, 8]

m = len(nums1)-len(nums2)
n = len(nums2)

i = m - 1
j = n - 1

while i >= 0 and j >= 0:
    if nums2[j] >= nums1[i]:
        nums1[i + j + 1] = nums2[j]
        j -= 1
    else:
        nums1[i + j + 1] = nums1[i]
        i -= 1

# copy remaining nums2 elements (if any)
while j >= 0:
    nums1[j] = nums2[j]
    j -= 1

print(nums1)
