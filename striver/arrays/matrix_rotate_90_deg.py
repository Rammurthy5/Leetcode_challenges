# use transpose and then reverse each row method
# t.c O(n*n) aux comp O(1)

matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

row = len(matrix)
col = len(matrix[0])

for i in range(row):
    for j in range(i+1, col):
        print(i, j)
        matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
        print("matrix ", matrix[i][j], " ji ", matrix[j][i])

for k in range(row):
    matrix[k] = matrix[k][::-1]

print(matrix)
