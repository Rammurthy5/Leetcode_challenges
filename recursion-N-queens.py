# time complexity is O(n^{n+1})
# space is O(S * n^2), S = # of solutions

def is_safe(r, c, n, matrix):
    # same row
    for i in range(n):
        if matrix[r][i] == "Q":
            return False

    # same column
    for i in range(n):
        if matrix[i][c] == "Q":
            return False

    # Diagonal Down right
    i, j = r+1, c+1
    while i < n and j < n:
        if matrix[i][j] == "Q":
            return False
        i += 1
        j += 1

    # Diagonal Down left
    i, j = r+1, c-1
    while i < n and j >= 0:
        if matrix[i][j] == "Q":
            return False
        i += 1
        j -= 1

    # Diagonal Up left
    i, j = r-1, c-1
    while i >= 0 and j >= 0:
        if matrix[i][j] == "Q":
            return False
        i -= 1
        j -= 1

    # Diagonal Up right
    i, j = r-1, c+1
    while i >= 0 and j < n:
        if matrix[i][j] == "Q":
            return False
        i -= 1
        j += 1

    return True

def create_matrix(n):
    matrix = [["." for _ in range(n)] for _ in range(n)]
    return place_n_queens(0, n, matrix)

def place_n_queens(c, n, matrix):
    result = []
    if c == n:
        result.append(["".join(row) for row in matrix])
        return result

    for r in range(n):
        if is_safe(r, c, n, matrix):
            matrix[r][c] = "Q"
            result += place_n_queens(c+1, n, matrix)
            matrix[r][c] = "."
    return result

print(create_matrix(4))
