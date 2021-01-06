class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        i = set(range(1,arr[-1])).difference(set(arr))
        if i:
            if len(i)>k-1:
                return sorted(list(i))[k-1]
            else:
                return arr[-1]+k-len(i)
        else:
            return arr[-1]+k
            
# beats 99.7% of run time code.
# 14.6 MB 
