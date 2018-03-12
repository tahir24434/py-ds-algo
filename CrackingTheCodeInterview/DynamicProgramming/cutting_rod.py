"""
Given a rod of length n inches and an array of prices that contains prices of all
pieces of size smaller than n. Determine the maximum value obtainable by cutting up
the rod and selling the pieces. For example, if length of the rod is 8 and the
values of different pieces are given as following, then the maximum obtainable value
is 22 (by cutting in two pieces of lengths 2 and 6)
length   | 1   2   3   4   5   6   7   8
--------------------------------------------
price    | 1   5   8   9  10  17  17  20

And if the prices are as following, then the maximum obtainable value is 24 (by
cutting in eight pieces of length 1)
length   | 1   2   3   4   5   6   7   8
--------------------------------------------
price    | 3   5   8   9  10  17  17  20
"""
from nose.tools import assert_equal


def max_profit(length, price, n, index):
    if n == 0 or index == 0:
        return 0
    if length[index-1] > n:
        return max_profit(length, price, n, index-1)

    return max(price[index-1] + max_profit(length, price, n-length[index-1],
                                           index),
               max_profit(length, price, n, index-1))


def max_profit_alt(length, price, n):
    if n <= 0:
        return 0

    max_gain = float("-inf")
    for i in range(len(length)):
        if length[i] <= n:
            max_gain = max(max_gain, price[i] + max_profit_alt(length, price, n-length[i]))
    return max_gain


if __name__ == "__main__":
    l = [1, 2, 3, 4, 5, 6, 7, 8]
    p = [1, 5, 8, 9, 10, 17, 17, 20]
    assert_equal(max_profit(l, p, 8, len(l)), 22)

    l = [2, 4, 6, 7, 8, 3, 5, 1]
    p = [5, 9, 17, 17, 20, 8, 10, 1]
    assert_equal(max_profit(l, p, 8, len(l)), 22)

    l = [2, 4, 6, 7, 8, 3, 1, 5]
    p = [5, 9, 17, 17, 20, 8, 10, 10]
    assert_equal(max_profit(l, p, 8, len(l)), 80)

    print("Success ...")
