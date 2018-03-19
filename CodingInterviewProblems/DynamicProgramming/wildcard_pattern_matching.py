"""
Given a text and a wildcard pattern, implement wildcard pattern matching algorithm
that finds if wildcard pattern is matched with text. The matching should cover the
entire text (not partial text).

The wildcard pattern can include the characters ‘?’ and ‘*’
‘?’ – matches any single character
‘*’ – Matches any sequence of characters (including the empty sequence)

For example,

Text = "baaabab",
Pattern = “*****ba*****ab", output : true
Pattern = "baaa?ab", output : true
Pattern = "ba*a?", output : true
Pattern = "a*ab", output : false

https://www.geeksforgeeks.org/wildcard-pattern-matching/
https://www.geeksforgeeks.org/wildcard-character-matching/
https://www.youtube.com/watch?time_continue=2&v=Q6ZX95GadA8
"""
from nose.tools import assert_true, assert_false


def is_match(text, wc, m, n):
    if m == 0 and n != 0:
        while n != 0:
            if wc[n-1] != '*':
                return False
            n -= 1

    if m == 0 and n == 0:
        return True

    if n == 0 and m != 0:
        return False

    if wc[n-1] == "?" or text[m-1] == wc[n-1]:
        return is_match(text, wc, m-1, n-1)

    if text[m - 1] != wc[n - 1] and wc[n-1] != "*":
        return False

    if wc[n-1] == "*":
        return is_match(text, wc, m-1, n) or is_match(text, wc, m, n-1)


if __name__ == "__main__":
    t = "baaabab"
    p = "*****ba*****ab"
    assert_true(is_match(t, p, len(t), len(p)))

    p = "baaa?ab"
    assert_true(is_match(t, p, len(t), len(p)))

    p = "ba*a?"
    assert_true(is_match(t, p, len(t), len(p)))

    p = "a*ab"
    assert_false(is_match(t, p, len(t), len(p)))

    t = "abaca"
    p =  "a*a"
    assert_true(is_match(t, p, len(t), len(p)))

    t = "aa"
    p = "*"
    assert_true(is_match(t, p, len(t), len(p)))

    t = "aab"
    p = "c*a*b"
    assert_false(is_match(t, p, len(t), len(p)))

    t = "a"
    p = "?"
    assert_true(is_match(t, p, len(t), len(p)))

    print("Success ...")

