"""
Given a MxN binary matrix, find the size of largest square sub-matrix of 1's present
in it.

https://www.youtube.com/watch?v=FO7VXDfS8Gk&t=4s
http://www.techiedelight.com/find-size-largest-square-sub-matrix-1s-present-given-binary-matrix/
"""


def largest_square_mat_len(mat):
    m = len(mat)
    n = len(mat[0])
    aux = [[0 for _ in range(n)] for _ in range(m)]
    return _largest_square_mat_len(mat, m, n, aux)


def _largest_square_mat_len(mat, m, n, aux):
    largest = float('-inf')
    for i in range(m):
        for j in range(n):
            if i == 0 or j == 0 or mat[i][j] == 0:
                aux[i][j] = mat[i][j]
            else:
                aux[i][j] = min(aux[i-1][j], aux[i][j-1], aux[i-1][j-1]) + 1
            largest = max(largest, aux[i][j])
    print(aux)
    return largest


if __name__ == "__main__":
    M = [[0, 1, 1, 0, 1],
         [1, 1, 0, 1, 0],
         [0, 1, 1, 1, 0],
         [1, 1, 1, 1, 0],
         [1, 1, 1, 1, 1],
         [0, 0, 0, 0, 0]]
    print(largest_square_mat_len(M))