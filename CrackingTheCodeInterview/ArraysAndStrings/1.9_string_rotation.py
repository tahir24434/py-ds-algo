"""
Assume that you have a method isSubstring which checks if one word is a substring of another.
Given two strings, s1 and s2, write code to check if s2 is a rotation of s1 using only one call
 to isSubstring (e.g, "waterbottle" is rotation of "erbottlewat")

Note: https://stackoverflow.com/questions/35220418/runtime-of-pythons-if-substring-in-string
"""
from nose.tools import assert_true, assert_false


def is_rotation(s1, s2):
    s2s2 = s2 + s2
    return s1 in s2s2


if __name__ == "__main__":
    assert_true(is_rotation("waterbottle", "erbottlewat"))
    assert_false(is_rotation("abcdef", "eabcd"))
    print("Success ...")

