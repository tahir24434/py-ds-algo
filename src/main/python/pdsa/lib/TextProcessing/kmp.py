"""
Knuth-Morris-Pratt Algorithm


https://www.youtube.com/watch?v=L9s6zuJugZM
https://www.youtube.com/watch?v=KG44VoDtsAA&t=181s
"""


def compute_kmp_fail(p):
    n = len(p)
    fail = [0] * n
    i = 1
    j = 0
    while i < n:
        if p[i] == p[j]:        # A character match. i + 1 characters match
            fail[i] = j + 1
            i += 1
            j += 1
        elif j > 0:
            j = fail[j-1]
        else:
            i += 1
    return fail