# time complexity is O(n!)
# space is O(S * n^2), S = # of solutions
# this is using hashing to track attacked rows /col. improves the time complexity much better

def create_matrix(n):
    matrix = [["." for _ in range(n)] for _ in range(n)]
    rows, diag_up, diag_down = hashing(n)
    return place_n_queens(0, n, matrix, rows, diag_up, diag_down)

def place_n_queens(c, n, matrix, rows, diag_up, diag_down):
    result = []
    if c == n:
        result.append(["".join(row) for row in matrix])
        return result

    for r in range(n):
        if not rows[r] and not diag_up[r-c+n-1] and not diag_down[r+c]:
            matrix[r][c] = "Q"
            rows[r] = diag_up[r-c+n-1] = diag_down[r+c] = True
            result += place_n_queens(c+1, n, matrix, rows, diag_up, diag_down)
            matrix[r][c] = "."
            rows[r] = diag_up[r-c+n-1] = diag_down[r+c] = False
    return result

# we are creating 3 diff arrays to keep track of diagonals, rows which already got Q placed so to avoid lookup on each cell in the matrix. saves time
def hashing(n):
    rows = [False] * n
    diag_up = [False] * (2*n - 1)
    diag_down = [False] * (2*n - 1)
    return rows, diag_up, diag_down

print(create_matrix(4))
