"""
Longest palindromic subsequence problem is the problem of finding the longest
subsequence of a string that is also palindrom.

Consider sequence ABBCDEGA
LPS: ABBA

http://www.techiedelight.com/longest-palindromic-subsequence-using-dynamic-programming/
"""
from nose.tools import assert_equal


def lps_len(X):
    memo = {}
    res = _lps_len(X, 0, len(X)-1, memo)
    print(memo)
    return res


def _lps_len(X, i, j, memo):
    if i == j:
        return 1
    if i > j:
        return 0

    key = (i, j)
    if key not in memo:
        if X[i] == X[j]:
            memo[key] = 2 + _lps_len(X, i+1, j-1, memo)
        else:
            memo[key] = max(_lps_len(X, i+1, j, memo), _lps_len(X, i, j-1, memo))
    return memo[key]


if __name__ == "__main__":
    A = "abbdcacb"
    assert_equal(lps_len(A), 5)
    A = "accada"
    assert_equal(lps_len(A), 4)
    A = "abdea"
    assert_equal(lps_len(A), 3)
    print("Success ...")
