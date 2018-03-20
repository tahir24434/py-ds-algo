"""
Matrix chain multiplication is an optimization problem that to find the most
efficient way to multiply given sequence of matrices. The problem is not actually
to perform the multiplications, but merely to decide the sequence of the matrix
multiplications involved.
https://www.youtube.com/watch?v=u6Y055g4mOE&t=861s
http://www.techiedelight.com/matrix-chain-multiplication/
"""
from nose.tools import assert_equal


def min_cost(dims):
    memo = {}
    return _min_cost(dims, 1, len(dims) - 1, memo)


def _min_cost(dims, i, j, memo):
    if i == j:
        return 0

    key = (i, j)
    if key not in memo:
        minimum = float('inf')
        for k in range(i, j):
            cost = _min_cost(dims, i, k, memo) + _min_cost(dims, k+1, j, memo) + \
                   (dims[i-1] * dims[k] * dims[j])
            minimum = min(minimum, cost)
        memo[key] = minimum

    return memo[key]


if __name__ == "__main__":
    dims = [10, 30, 5, 60]
    assert_equal(min_cost(dims), 4500)
    dims = [1, 2, 3, 4]
    assert_equal(min_cost(dims), 18)
    print("Success ...")
