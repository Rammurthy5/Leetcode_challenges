# time O(2n)
# DFS and Hash table approach

"""
# Definition for Employee.
class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates
"""

class Solution:
    def getImportance(self, employees: List['Employee'], id: int) -> int:
        empDict = {}
        
        for i in employees:
            empDict[i.id] = [i.importance, i.subordinates]
        
        total_importance = empDict[id][0]
        subordinates = empDict[id][1]
        while subordinates:
            s = subordinates.pop()
            subordinates.extend(empDict[s][1])
            total_importance+=empDict[s][0]
        return total_importance
                
