"""
Count the number of ways to traverse a 2D array
In this problem you are to count the number of ways of starting at the top-left
corner or a 2D array and getting to the bottom right corner. All moves must either go
right or down.
"""
from nose.tools import assert_equal


def num_ways(A, m, n):
    if m == n == 0:
        return 1
    if m < 0 or n < 0:
        return 0
    return num_ways(A, m-1, n) + num_ways(A, m, n-1)


if __name__ == "__main__":
    A = [[0] * 5] * 5
    assert_equal(num_ways(A, len(A)-1, len(A[0])-1), 70)
    print("Success ...")
