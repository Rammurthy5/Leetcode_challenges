ar = [1,2,-4,-5]

res_ar = []
half = len(ar)//2
for i in range(half):
    res_ar.extend([ar[i], ar[i+half]])

print(res_ar)

# time complexity O(n/2) => O(n)
# aux complexity O(n)
