# DFS is faster than BFS. 

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: TreeNode) -> List[float]:
        # bfs 
        row = [root] if root else []
        rst =[]
        while row:
            rst.append(sum([node.val for node in row]) / len(row))
            next = [node.left for node in row if node.left]
            next+= [node.right for node in row if node.right]
            row = next
            
        return rst
    
        #dfs
#         self.lst = []
#         def dfs(node, depth):
#             if node:
#                 if len(self.lst) == depth:
#                     self.lst.append([])
#                 self.lst[depth].append(float(node.val))
#                 dfs(node.left, depth + 1)
#                 dfs(node.right, depth + 1)
            
#         dfs(root, 0)
#         return [sum(l) / len(l) for l in self.lst]
