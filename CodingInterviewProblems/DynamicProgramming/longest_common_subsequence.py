"""
LCS Problem Statement: Given two sequences, find the length of longest subsequence
present in both of them. A subsequence is a sequence that appears in the same
relative order, but not necessarily contiguous.
For example, “abc”, “abg”, “bdf”, “aeg”, ‘”acefg”, .. etc are subsequences of
“abcdefg”. So a string of length n has 2^n different possible subsequences.

Examples:
LCS for input Sequences “ABCDGH” and “AEDFHR” is “ADH” of length 3.
LCS for input Sequences “AGGTAB” and “GXTXAYB” is “GTAB” of length 4.

https://www.youtube.com/watch?v=Qf5R-uYQRPk
https://www.youtube.com/watch?v=43P0xZp3FU4
"""
from nose.tools import assert_equal


def lcs_recursive(X, Y, n, m):
    """

    :param X: string
    :param Y: string
    :param n: int
        length of string X
    :param m: int
        length of string Y.
    :return:
    """
    if n == 0 or m == 0:
        return 0
    elif X[n-1] == Y[m-1]:
        return lcs_recursive(X, Y, n-1, m-1) + 1
    else:
        lcs1 = lcs_recursive(X, Y, n, m-1)
        lcs2 = lcs_recursive(X, Y, n-1, m)
        return max(lcs1, lcs2)


def lcs_memoized(X, Y, n, m):
    """

    :param X: string
    :param Y: string
    :param n: int
        length of string X
    :param m: int
        length of string Y.
    :return:
    """
    if mem[n][m] is None:
        if n == 0 or m == 0:
            mem[n][m] = 0
        elif X[n-1] == Y[m-1]:
            mem[n][m] = lcs_memoized(X, Y, n-1, m-1) + 1
        else:
            lcs1 = lcs_memoized(X, Y, n, m-1)
            lcs2 = lcs_memoized(X, Y, n-1, m)
            mem[n][m] = max(lcs1, lcs2)
    return mem[n][m]


if __name__ == "__main__":
    x = "ABCDGH"
    y = "AEDFHR"
    assert_equal(lcs_recursive(x, y, len(x), len(y)), 3)
    u = "AGGTAB"
    v = "GXTXAYB"
    assert_equal(lcs_recursive(u, v, len(u), len(v)), 4)

    x = "ABCDGH"
    y = "AEDFHR"
    mem = [[None] * (len(y)+1)] * (len(x)+1)
    assert_equal(lcs_memoized(x, y, len(x), len(y)), 3)
    u = "AGGTAB"
    v = "GXTXAYB"
    mem = [[None] * (len(v)+1)] * (len(u)+1)
    assert_equal(lcs_memoized(u, v, len(u), len(v)), 4)
    print("Success ...")
