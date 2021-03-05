# time complexity for both appraoch O(N+M) space O(N)
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        # hash approach
#         nodes = set()
#         while headB is not None:
#             nodes.add(headB)
#             headB = headB.next
            
#         while headA is not None:
#             if headA in nodes:
#                 return headA
#             headA = headA.next
            
#         return None
    
        # two pointers
        pA = headA
        pB = headB
        while pA!=pB:
            pA = headB if pA is None else pA.next
            pB = headA if pB is None else pB.next
            
        return pA
            
