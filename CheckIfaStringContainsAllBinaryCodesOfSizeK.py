class Solution:
    def hasAllCodes(self, s: str, k: int) -> bool:
        #naive but slow 
#         start = 2**(k-1)
#         if k==1 and ('0' not in s or '1' not in s):
#             return False
            
#         for i in range(start, 2**k):
#             if k==2 and '00' not in s:
#                 return False
#             if bin(i)[2:] not in s:
#                 return False
            
#         return True
       # faster approach 
        n = len(s)
        substrings = set([])
        for i in range(n - k + 1):
            substrings.add(s[i:i + k])
        return len(substrings) == (2 ** k)
       
