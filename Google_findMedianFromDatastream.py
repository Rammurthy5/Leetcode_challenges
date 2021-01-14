# Insertion sort approach which takes O(n) + O(log n ) = O(n) time 
class MedianFinder:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.arr = []
        

    def addNum(self, num: int) -> None:
        
        for i, j in enumerate(self.arr):
            if num<j:
                self.arr.insert(i, num)
                return 
        self.arr.append(num)

    def findMedian(self) -> float:
        q, r = divmod(len(self.arr), 2)
        if r==0:
            return (self.arr[q]+self.arr[q-1])/2
        return self.arr[q]
            


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()

# Two heaps runtime O(log n)
from heapq import * 
class MedianFinder:
    def __init__(self):
        self.heaps = [], []

    def addNum(self, num):
        small, large = self.heaps
        heappush(small, -heappushpop(large, num))
        if len(large) < len(small):
            heappush(large, -heappop(small))

    def findMedian(self):
        small, large = self.heaps
        if len(large) > len(small):
            return float(large[0])
        return (large[0] - small[0]) / 2.0
