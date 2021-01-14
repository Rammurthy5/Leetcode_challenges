# Stack approach
"""
O(maxK to power of countK *n) 
where maxK is the maximum value of k
countK is the count of nested k values and n is the maximum length of encoded string. 
Example, for s = 20[a10[bc]], maxK is 20, countK is 2 as there are 2 nested k values (20 and 10) .
Also, there are 2 encoded strings a and bc with maximum length of encoded string ,n as 2
"""

class Solution:
    def stackPop(self, result: list) -> list:
        
        curr_str = str()
        while result[-1]!='[':
            curr_str+=result.pop()
        else:
        
            result.pop()
            k = str()
            while result:
                if result[-1].isdigit():
                    k+= result.pop()
                else:
                    break
            curr_str = int(k[::-1])* curr_str
            
        result.extend(list(curr_str[::-1]))
        
        return result

                        
    def decodeString(self, s: str) -> str:
        result = []
        
        c = 0
        while c<len(s):
            if s[c]==']':
                result = self.stackPop(result)
                
            else:
                result.append(s[c])
            c+=1
        return ''.join(result)
                        
