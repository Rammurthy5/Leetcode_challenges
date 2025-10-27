# optimised sudoku solver solution with slight improvement in time complexity by doing is_available in single loop. 

# time complexity is O(k^E) but faster than version 1 in practice
# space is O(1)

def is_available(n, row, col, sudoku):
  for i in range(9):
    if sudoku[row][i]==n:
      return False
    if sudoku[i][col]==n:
      return False

    if sudoku[3 * (row//3) + i // 3][3 * (col // 3) + i % 3] == n):
      return False
  return True

def solve(sudoku):
  # find the hole
  for row in range(9):
    for col in range(9):
      if sudoku[row][col]== ".":
        # start with 1 but change if that number exists in row, col, or 3x3
        for n in range(1,10):
          if is_available(n, row, col, sudoku):
            sudoku[row][col]=str(n)
            if solve(sudoku):
              return True
            sudoku[row][col]="."
        return False # no valid numbeer found
  return True # no empty cells left


sudoku = [
  ["5","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],
  ["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],
  [".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]
]
print(solve(sudoku))
print(sudoku)

# Output: [
#   ["5","3","4","6","7","8","9","1","2"],["6","7","2","1","9","5","3","4","8"],["1","9","8","3","4","2","5","6","7"],
#   ["8","5","9","7","6","1","4","2","3"],["4","2","6","8","5","3","7","9","1"],["7","1","3","9","2","4","8","5","6"],
#   ["9","6","1","5","3","7","2","8","4"],["2","8","7","4","1","9","6","3","5"],["3","4","5","2","8","6","1","7","9"]
# ]
