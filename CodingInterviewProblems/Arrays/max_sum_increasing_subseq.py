"""
Given an array of n positive integers. Write a program to find the sum of maximum
sum subsequence of the given array such that the integers in the subsequence are
sorted in increasing order.
"""
from nose.tools import assert_equal


def max_sum(A):
    return _max_sum(A, 0, float('-inf'), 0)


def _max_sum(A, m, prev, sum_so_far):
    if m == len(A):
        return sum_so_far

    exclude = _max_sum(A, m + 1, prev, sum_so_far)
    include = 0
    if prev < A[m]:
        include = _max_sum(A, m + 1, A[m], sum_so_far + A[m])

    return max(include, exclude)


if __name__ == "__main__":
    A = [5, 1, 3, 7, 9, 2]
    assert_equal(max_sum(A), 21)
    A = [8, 4, 12, 2, 10, 6, 14, 1, 9, 5, 13, 3, 11, 7, 15]
    assert_equal(max_sum(A), 49)
    A = [1, 101, 2, 3, 100, 4, 5]
    assert_equal(max_sum(A), 106)
    A = [10, 5, 4, 3]
    assert_equal(max_sum(A), 10)
    A = [10, 5, 4, 300]
    assert_equal(max_sum(A), 310)
    print("Success ...")
