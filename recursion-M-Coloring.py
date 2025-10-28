# Time complexity is O (n * m^n). n is the size of array and m iterations for each node.
# space is O(N + E)  Adjacency list, color array, recursion stack

def paint(curr_ind, N, M, graph, colors):
  if curr_ind == N:
    return True
    
  def is_safe(color, curr_ind, graph, colors):
    # Check all adjacent vertices
    for neighbor in graph[curr_ind]:
        if colors[neighbor] == color:
            return False
    return True
    
  for colour in range(1, M+1):
    if is_safe(colour, curr_ind, graph, colors):
      colors[curr_ind]=colour
      if paint(curr_ind+1, N, M, graph, colors): return True
      colors[curr_ind]=0
  
  return False

def edgesDict(N, edges):
  dd = [set() for _ in range(N)]
  for i in edges:
    dd[i[0]].add(i[1])
    dd[i[1]].add(i[0])
  return dd

# Input : 
N = 4
M = 3
E = 5
Edges = [ (0, 1) , (1, 2) , (2, 3) , (3, 0) , (0, 2) ]


graph = edgesDict(N, Edges)
colors = [0] * N

print(paint(0, N, M, graph, colors))

# Output : true
