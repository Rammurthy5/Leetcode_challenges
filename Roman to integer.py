class Solution:
    def romanToInt(self, s: str) -> int:
        d = {
            "I": 1,
            "V": 5, 
            "X":10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
        }
        total = 0
    
        i = len(s)-1
        prev = 0
        while i>=0:
        
        # Optimized approach 
            if d[s[i]]<prev:
                total-=d[s[i]]
            else:
                total+=d[s[i]]
                prev = d[s[i]]
            i-=1
        
        # Alternate approach takes 15% more time 
#             if i>0 and ((s[i] in ['C', 'L'] and s[i-1]=='X') 
#             or (s[i] in ['V', 'X'] and s[i-1]=='I')
#             or (s[i] in ['D', 'M'] and s[i-1]=='C')):
#                 total-=d[s[i-1]]
#                 i-=1
            
#             total+=d[s[i]]
#             i-=1
        return total
