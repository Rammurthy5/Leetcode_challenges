#using dutch national algorithm
# time complexity O(n)
# aux complexity O(1)

low = 0
mid = 0
high = len(a)-1

while mid<high:
    if a[mid]==0:
        a[mid],a[low]=a[low],a[mid]
        low+=1
        mid+=1
    elif a[mid]==1:
        mid+=1
    elif a[mid]==2:
        a[mid],a[high]=a[high],a[mid]
        high-=1
print(a)
