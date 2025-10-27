# optimal version with O(1) constant lookup in the is_available method using sets() alongside improved space complexity O(1)

def solve(sudoku):
  # input sets
  row_sets = [set() for _ in range(9)]
  col_sets = [set() for _ in range(9)]
  box_sets = [set() for _ in range(9)]
  empties = []

  # find the hole
  for row in range(9):
    for col in range(9):
      if sudoku[row][col]== ".":
        empties.append((row,col))
      else:
        row_sets[row].add(sudoku[row][col])
        col_sets[col].add(sudoku[row][col])
        box_sets[(row // 3) * 3 + (col // 3)].add(sudoku[row][col])

    def backtrack(k=0):
      if k == len(empties):
          return True  # solved

      i, j = empties[k]
      b = (i // 3) * 3 + (j // 3)

      for n in map(str, range(1, 10)):
          if n not in row_sets[i] and n not in col_sets[j] and n not in box_sets[b]:
              # place number
              sudoku[i][j] = n
              row_sets[i].add(n)
              col_sets[j].add(n)
              box_sets[b].add(n)

              if backtrack(k + 1):
                  return True

              # backtrack
              sudoku[i][j] = "."
              row_sets[i].remove(n)
              col_sets[j].remove(n)
              box_sets[b].remove(n)

      return False
  backtrack(0)
  return sudoku

# Output: [
#   ["5","3","4","6","7","8","9","1","2"],["6","7","2","1","9","5","3","4","8"],["1","9","8","3","4","2","5","6","7"],
#   ["8","5","9","7","6","1","4","2","3"],["4","2","6","8","5","3","7","9","1"],["7","1","3","9","2","4","8","5","6"],
#   ["9","6","1","5","3","7","2","8","4"],["2","8","7","4","1","9","6","3","5"],["3","4","5","2","8","6","1","7","9"]
# ]
