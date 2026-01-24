# t.c O(row * col)
# aux complexity O(1)
# approach is to turn clockwise at the every end. left to right -> top to bottom -> right to left -> bottom to top and repeat same again

matrix = [ [ 1, 2, 3, 4],[ 5, 6, 7, 8 ],[ 9, 10, 11, 12],[ 13, 14, 15, 16 ] ]

top = 0
bottom = len(matrix)-1
left = 0
right = len(matrix[0])-1

# top row
while top <= bottom and left <= right:
     # left to right
     for i in range(top, right+1):
         print(matrix[top][i])
     top +=1

     # top right
     for i in range(top, bottom+1):
         print(matrix[i][right])
     right = right - 1

     # right to left on bottom
     for i in range(right, left-1, -1):
         print(matrix[bottom][i])
     bottom = bottom - 1

     # bottom to top left
     for i in range(bottom, top+1, -1):
         print(matrix[i][left])
     left+=1
