from nose.tools import assert_true, assert_false


def is_one_eidt_away(str1, str2):
    str1_len = len(str1)
    str2_len = len(str2)
    if abs(str1_len - str2_len) > 1:
        return False

    i = j = 0
    found_diff = False
    while i < str1_len and j < str2_len:
        if str1[i] != str2[j]:
            if found_diff:
                return False
            else:
                found_diff = True
                if str1_len > str2_len:
                    i += 1
                elif str2_len > str1_len:
                    j += 1
                else:
                    i += 1
                    j += 1
        else:
            i += 1
            j += 1

    # If last character is extra in any string.
    if (i < str1_len or j < str2_len) and found_diff:
        return False
    return True

if __name__ == "__main__":
    assert_true(is_one_eidt_away("pale", "ple"))
    assert_true(is_one_eidt_away("pales", "pale"))
    assert_true(is_one_eidt_away("pale", "bale"))
    assert_false(is_one_eidt_away("pale", "bake"))
    assert_false(is_one_eidt_away("paledd", "pale"))
    print("SUCCESS ...")
