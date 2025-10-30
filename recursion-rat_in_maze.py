# time complexity - O(4 ^ n ^ 2); space complexity - O(n^2)


# Input: 
maze = [
  [1, 0, 0, 0],
  [1, 1, 0, 1],
  [1, 1, 0, 0],
  [0, 1, 1, 1]
]
  
def findPathUtil(r, c, maze, visited, res, result):
  n = len(maze)

  # If reached destination
  if r == n - 1 and c == n - 1:
      result.append(res)
      return
    
  # mark visited
  visited[r][c] = True
  
  # all 4 directions: Down, Left, Right, Up
  directions = [('D', r + 1, c), ('L', r, c - 1), ('R', r, c + 1), ('U', r - 1, c)]
  for move, nr, nc in directions:
      if is_fine(nr, nc, maze, visited):
          findPathUtil(nr, nc, maze, visited, res + move, result)

  # backtrack
  visited[r][c] = False

def is_fine(r, c, maze, visited):
  n = len(maze)
  return (0 <= r < n and 0 <= c < n and maze[r][c] == 1 and not visited[r][c])

def findPath(maze):
    n = len(maze)
    visited = [[False] * n for _ in range(n)]
    result = []
    if maze[0][0] == 0:
        return []  # no path if start is blocked
    findPathUtil(0, 0, maze, visited, "", result)
    return sorted(result)
  
# Output: DDRDRR DRDDRR
print(findPath(maze))
