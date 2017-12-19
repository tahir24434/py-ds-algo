from nose.tools import assert_true, assert_false


def is_unique(string):
    if string is None or len(string) > 128:
        return False

    count = [0] * 128
    for c in string:
        count[ord(c)] += 1
        if count[ord(c)] > 1:
            return False
    return True


def is_unique_set(string):
    if string is None or len(string) > 128:
        return False
    char_set = set()
    for char in string:
        if char in char_set:
            return False
        else:
            char_set.add(char)
    return True

if __name__ == "__main__":
    assert_false(is_unique(None))
    assert_true(is_unique(""))
    assert_false(is_unique("a b "))
    assert_true(is_unique("a b"))
    assert_true(is_unique("abcdefghijkl"))
    assert_true(is_unique("aAbBcCdDefghijkl"))
    assert_false(is_unique("aba"))
    assert_true(is_unique("~`:;.,@_-(*&^\"'%$#!"))
    assert_false(is_unique("~`\"\':;.,'@@"))
    print("SUCCESS")
