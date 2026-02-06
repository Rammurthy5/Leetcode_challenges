# time complexity O(n)
# aux O(n)

intervals=[[1,3],[2,6],[8,10],[15,18]]

intervals.sort()
merged = []
starti, endi = intervals[0]
i = 1
while i < len(intervals):
    s,e = intervals[i]
    if s in range(starti, endi+1):
        endi = max(endi, e)
    else:
        merged.append([starti, endi])
        starti = s
        endi = e
    i+=1

merged.append([starti, endi])
print(merged)
