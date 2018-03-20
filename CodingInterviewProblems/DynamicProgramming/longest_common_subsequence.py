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

To find length:
http://www.techiedelight.com/longest-common-subsequence/
To find actual LCS:
http://www.techiedelight.com/longest-common-subsequence-finding-lcs/
"""
from nose.tools import assert_equal

"""
******************************* Memoized ******************************* 
"""
def lcs_len(X, Y):
    """
    Function to find length of longest common subsequence of sequence X and Y.
    :param X:
        First string
    :param Y:
        Second string
    :return:
        Length of longest common subsequence of string X and string Y.
    """
    memo = {}
    res = _lcs_len(X, Y, len(X), len(Y), memo)
    return res


def _lcs_len(X, Y, m, n, memo):
    """
    Function to find length of longest common subsequence of sequence X and Y with
    length m and n respectively.

    :param X:
        First string
    :param Y:
        Second string
    :param m:
        Number of elements in first string
    :param n:
        Number of elements in second string
    :param memo:
        Map to hold solutions to subproblems
    :return:
    """
    # If there are no more elements in either string.
    if m == 0 or n == 0:
        return 0
    key = (m, n)
    if key not in memo:
        # If last charachter of X and Y matches
        if X[m-1] == Y[n-1]:
            memo[key] = _lcs_len(X, Y, m-1, n-1, memo) + 1
        else:
            # Else if last charachter does NOT match.
            memo[key] = max(_lcs_len(X, Y, m-1, n, memo), _lcs_len(X, Y, m, n-1, memo))
    return memo[key]


"""
************************** Tabulation (Bottom-up) ************************** 
"""


def lcs_len_tab(X, Y):
    m = len(X)
    n = len(Y)
    tab = [[0 for x in range(n+1)] for i in range(m+1)]
    lcs_length = _lcs_len_tab(X, Y, m, n, tab)
    return lcs_length, tab


def _lcs_len_tab(X, Y, m, n, tab):
    for i in range(1, m+1):
        for j in range(1, n+1):
            if X[i-1] == Y[j-1]:
                tab[i][j] = tab[i-1][j-1] + 1
            else:
                tab[i][j] = max(tab[i][j-1], tab[i-1][j])
    return tab[m][n]


def lcs(X, Y, m, n):
    tab = lcs_len_tab(X, Y)[1]
    if m == 0 or n == 0:
        return ""

    if X[m-1] == Y[n-1]:
        return lcs(X, Y, m-1, n-1) + X[m-1]
    else:
        if tab[m-1][n] > tab[m][n-1]:
            return lcs(X, Y, m-1, n)
        else:
            return lcs(X, Y, m, n-1)


if __name__ == "__main__":
    x = "ABCDGH"
    y = "AEDFHR"
    assert_equal(lcs_len(x, y), 3)
    u = "AGGTAB"
    v = "GXTXAYB"
    assert_equal(lcs_len(u, v), 4)

    x = "ABCDGH"
    y = "AEDFHR"
    assert_equal(lcs_len_tab(x, y)[0], 3)
    u = "AGGTAB"
    v = "GXTXAYB"
    assert_equal(lcs_len_tab(u, v)[0], 4)

    print(lcs(u, v, len(u), len(v)))
    print("Success ...")
