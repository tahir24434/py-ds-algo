"""
Given a boolean 2D matrix, find the number of islands. A group of connected 1s forms
an island. For example, the below matrix contains 5 islands

Input : mat[][] = {{1, 1, 0, 0, 0},
                   {0, 1, 0, 0, 1},
                   {1, 0, 0, 1, 1},
                   {0, 0, 0, 0, 0},
                   {1, 0, 1, 0, 1}
Output : 5
This is an variation of the standard problem: “Counting number of connected
components in a undirected graph”.
"""


def island_dfs(A, row, col):
    if row < 0 or row >= len(A) or col < 0 or col >= len(A[0]):
        return 0
    if A[row][col] == 0:
        return 0

    A[row][col] = 0
    for i in range(row - 1, row + 2):
        for j in range(col - 1, col + 2):
            island_dfs(A, i, j)


def num_islands(A):
    num_rows = len(A)
    num_cols = len(A[0])

    num_islands = 0
    for row in range(num_rows):
        for col in range(num_cols):
            if A[row][col] == 1:
                num_islands += 1
                island_dfs(A, row, col)
    return num_islands


if __name__ == "__main__":
    A = [[1, 0, 0, 0],
         [1, 1, 0, 0],
         [1, 0, 0, 0],
         [1, 1, 0, 1],
         [0, 0, 0, 1]]
    print(num_islands(A))
