from nose.tools import assert_equal


def compress_string(s):
    count = 1
    cs = ""
    for front in range(1, len(s)):
        if s[front] == s[front-1]:
            count += 1
        else:
            cs = cs + s[front-1] + str(count)
            count = 1

    cs = cs + s[len(s) - 1] + str(count)
    if len(cs) >= len(s):
        return s
    return cs


if __name__ == "__main__":
    assert_equal(compress_string("aabcccccaad"), "a2b1c5a2d1")
    assert_equal(compress_string("aabcccccaaa"), "a2b1c5a3")
    assert_equal(compress_string("abca"), "abca")
    assert_equal(compress_string("aa"), "aa")
    assert_equal(compress_string("aaaaa"), "a5")
    assert_equal(compress_string("aAaAa"), "aAaAa")
    assert_equal(compress_string("aaaAAAaAA"), "a3A3a1A2")
    print("Success ...")