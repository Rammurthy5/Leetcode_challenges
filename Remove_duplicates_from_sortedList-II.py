# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        sentinel = ListNode(0, head)
        
        pred = sentinel
        
        curr_node = head
        while curr_node:
            if curr_node.next and curr_node.val == curr_node.next.val:
                while curr_node.next and curr_node.val == curr_node.next.val:
                    curr_node = curr_node.next
                pred.next = curr_node.next
            else:
                pred = pred.next
            
            curr_node = curr_node.next
        
        return sentinel.next
                
   # runtime 40ms faster than 71%
