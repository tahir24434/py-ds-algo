"""
Given two strings ‘X’ and ‘Y’, find the length of the longest common substring.
"""
from nose.tools import assert_equal


def lc_substring(X, Y):
    m = len(X)
    n = len(Y)
    tab = [[0 for x in range(n+1)] for i in range(m+1)]
    return _lc_substring(X, Y, m, n, tab)


def _lc_substring(X, Y, m, n, tab):
    max_substring_len = 0
    for i in range(1, m+1):
        for j in range(1, n+1):
            if X[i-1] == Y[j-1]:
                tab[i][j] = tab[i-1][j-1] + 1
                max_substring_len = max(max_substring_len, tab[i][j])
            else:
                tab[i][j] = 0
    return max_substring_len


if __name__ == "__main__":
    X = 'OldSite:GeeksforGeeks.org'
    Y = 'NewSite:GeeksQuiz.com'
    assert_equal(lc_substring(X, Y), 10)
    print("Success ...")


