from collections import Counter, OrderedDict 

# 1st solution twice faster than 2nd 
# time 1st : O(n); 2nd: O(2n)

class Solution:
    
    def reorganizeString(self, S: str) -> str:
        char_counter = Counter(S).most_common()
                
        if char_counter[0][1]>(len(S)+1)//2:
            return ""
        res = [""]*len(S)
        i = 0   
        for letter, cnt in char_counter:
            for j in range(cnt):
                res[i]= letter
                i+=2
                if i>=len(S):
                    i = 1
        return "".join(res)

    # import heapq

        # char_counter = Counter(S)
        # heap = []
#         for k, v in char_counter.items():
#             heapq.heappush(heap, (-v, k)) O(n)
            
#         prev_v, prev_k = 0, ""
        
#         while heap:
#             popped = heapq.heappop(heap)
#             res+=popped[1]
#             if prev_v<0:
#                 heapq.heappush(heap, (prev_v, prev_k))
#             prev_v, prev_k = popped[0]+1, popped[1]
        
#         if len(res)!=len(S):
#             return ""
        
#         return res
            
        
