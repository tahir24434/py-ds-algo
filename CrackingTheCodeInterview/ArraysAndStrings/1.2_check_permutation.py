from nose.tools import assert_true, assert_false


def check_permutation(str1, str2):
    if str1 is None or str2 is None or len(str1) != len(str2):
        return False
    count = [0] * 128
    for c in str1:
        count[ord(c)] += 1
    for c in str2:
        count[ord(c)] -= 1
        if count[ord(c)] < 0:
            return False
    for item in count:
        if item > 0:
            return False
    return True


def check_permutation_dict(str1, str2):
    if str1 is None or str2 is None or len(str1) != len(str2):
        return False

    char_dict = dict()
    for char in str1:
        char_dict[char] = char_dict.get(char, 0) + 1
    for char in str2:
        if char in char_dict:
            if char_dict[char] == 0:
                return False
            char_dict[char] -= 1
        else:
            return False
    return True

if __name__ == "__main__":
    assert_false(check_permutation("abc", "abcd"))
    assert_false(check_permutation("abcd", "abc"))
    assert_true(check_permutation("first", "risft"))
    assert_false(check_permutation("firstt", "risft"))
    assert_false(check_permutation("firs", "risft"))
    assert_true(check_permutation("f", "f"))
    print("Success ...")
