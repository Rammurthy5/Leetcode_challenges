class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        keys = {0}
        visited = set()
        while keys:
            roomno = keys.pop()
            visited.add(roomno)
            for i in rooms[roomno]:
                if i!=roomno and i not in visited:
                    keys.add(i)
                 
        if len(visited)!=len(rooms):
            return False
        return True
            
# time O(noOfRooms * No.Keys) # space O(2n)
