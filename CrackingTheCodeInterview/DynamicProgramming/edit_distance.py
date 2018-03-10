"""
Given two strings str1 and str2 and below operations that can performed on str1.
Find minimum number of edits (operations) required to convert ‘str1’ into ‘str2’.
Insert
Remove
Replace
All of the above operations are of equal cost.

https://www.geeksforgeeks.org/dynamic-programming-set-5-edit-distance/
https://www.youtube.com/watch?v=qY_XKCgrgbM
"""
from nose.tools import assert_equal


def edit_distance_rec(str1, str2, m, n):
    """
    Recursive
    :param str1:
    :param str2:
    :param m:
        len of str1
    :param n:
        len of str2
    :return:
    """
    if m == 0:
        return n
    if n == 0:
        return m

    if str1[m-1] == str2[n-1]:
        return edit_distance_rec(str1, str2, m-1, n-1)
    else:
        ed_insert = edit_distance_rec(str1, str2, m, n-1)
        ed_remove = edit_distance_rec(str1, str2, m-1, n)
        ed_replace = edit_distance_rec(str1, str2, m-1, n-1)
        return min(ed_insert, ed_remove, ed_replace) + 1


def edit_distance_mem(str1, str2, m, n):
    """
    Memoized
    :param str1:
    :param str2:
    :param m:
        len of str1
    :param n:
        len of str2
    :return:
    """
    if mem[m][n] is not None:
        return mem[m][n]

    res = 0
    if m == 0:
        res = n
    elif n == 0:
        res = m
    elif str1[m-1] == str2[n-1]:
        res = edit_distance_mem(str1, str2, m-1, n-1)
    else:
        ed_insert = edit_distance_mem(str1, str2, m, n-1)
        mem[m][n-1] = ed_insert
        ed_remove = edit_distance_mem(str1, str2, m-1, n)
        mem[m-1][n] = ed_remove
        ed_replace = edit_distance_mem(str1, str2, m-1, n-1)
        mem[m-1][n-1] = ed_replace
        res = min(ed_insert, ed_remove, ed_replace) + 1
    mem[m][n] = res
    return res


if __name__ == "__main__":
    str1 = "geek"
    str2 = "gesek"
    assert_equal(edit_distance_rec(str1, str2, len(str1), len(str2)), 1)
    str1 = "cat"
    str2 = "cut"
    assert_equal(edit_distance_rec(str1, str2, len(str1), len(str2)), 1)
    str1 = "sunday"
    str2 = "saturday"
    assert_equal(edit_distance_rec(str1, str2, len(str1), len(str2)), 3)

    str1 = "geek"
    str2 = "gesek"
    mem = [[None] * (len(str2) + 1) for i in range(len(str1) + 1)]
    assert_equal(edit_distance_mem(str1, str2, len(str1), len(str2)), 1)
    str1 = "cat"
    str2 = "cut"
    mem = [[None] * (len(str2)+1) for i in range(len(str1)+1)]
    assert_equal(edit_distance_mem(str1, str2, len(str1), len(str2)), 1)
    str1 = "sunday"
    str2 = "saturday"
    mem = [[None] * (len(str2) + 1) for i in range(len(str1) + 1)]
    assert_equal(edit_distance_mem(str1, str2, len(str1), len(str2)), 3)
    print("Success ...")

