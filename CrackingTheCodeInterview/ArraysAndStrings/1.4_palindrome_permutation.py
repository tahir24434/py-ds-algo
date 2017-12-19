from nose.tools import assert_true, assert_false


def palindrome_permutation(string):
    string = string.replace(" ", "")
    count = [0] * 128
    for c in string:
        count[ord(c)] = not count[ord(c)]
    # if sum(count) > 1:
    #    return False
    if count.count(True) > 1:
        return False
    return True

if __name__ == "__main__":
    assert_true(palindrome_permutation("tact coa"))
    assert_true(palindrome_permutation("tact ca"))
    assert_true(palindrome_permutation("tactcoa"))
    assert_false(palindrome_permutation("tacttcoa"))
    print("Success ...")
