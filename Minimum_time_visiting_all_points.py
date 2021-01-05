class Solution:
    def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:
        result = 0
        for i in range(len(points)-1):
            x,y = points[i]
            x1,y1 = points[i+1]
            result+=max(abs(x-x1), abs(y-y1))                
        return result
        
 # time complexity O(n). 56ms better than 80.5%
 # memory 14MB Better than 54%
