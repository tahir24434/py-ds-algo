"""
Given a square matrix, print maximum length snake sequence in it.
"""


def max_snake_seq(A):
    memo = {}
    return _max_snake_seq(A, len(A)-1, len(A[0])-1, memo)


def _max_snake_seq(A, m, n, memo):
    if m == 0 and n == 0:
        return 1
    if m < 0 or n < 0:
        return 0

    key = (m, n)
    if key not in memo:
        add_bottom = add_right = 0
        if m-1 > 0 and A[m][n] == (A[m-1][n] + 1) or A[m][n] == (A[m-1][n] - 1):
            add_bottom = 1
        if n-1 > 0 and A[m][n] == A[m][n-1] + 1 or A[m][n] == A[m][n-1] - 1:
            add_right = 1

        memo[key] = max(_max_snake_seq(A, m-1, n, memo) + add_bottom,
                        _max_snake_seq(A, m, n-1, memo) + add_right)
    return memo[key]


if __name__ == "__main__":
    mat = [[7, 5, 2, 3, 1],
           [3, 4, 1, 4, 4],
           [1, 5, 6, 7, 8],
           [3, 4, 5, 8, 9],
           [3, 2, 2, 7, 6]]
    print(max_snake_seq(mat))
