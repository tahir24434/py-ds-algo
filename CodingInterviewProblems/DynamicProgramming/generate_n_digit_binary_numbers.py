"""
Generate binary numbers of n digits.
https://www.youtube.com/watch?v=HvGkzDT2ffI&list=PLnfg8b9vdpLn9exZweTJx44CII1bYczuk&index=14
"""
from nose.tools import assert_list_equal


def _generate_binary(num_digits, prefix, ans):
    if num_digits == 0:
        ans.append(prefix)
    else:
        _generate_binary(num_digits - 1, prefix + "0", ans)
        _generate_binary(num_digits - 1, prefix + "1", ans)


def generate_binary(num_digits):
    ans = []
    _generate_binary(num_digits, "", ans)
    return ans


def _generate_decimal(num_digits, prefix, ans):
    if num_digits == 0:
        ans.append(prefix)
    else:
        for i in range(10):
            _generate_decimal(num_digits - 1, prefix + str(i), ans)


def generate_decimal(num_digits):
    ans = []
    _generate_decimal(num_digits, "", ans)
    return ans


if __name__ == "__main__":
    generate_binary(32)
    assert_list_equal(generate_binary(2), ['00', '01', '10', '11'])
    assert_list_equal(generate_binary(3), ['000', '001', '010', '011', '100', '101', '110', '111'])

    assert_list_equal(generate_decimal(1), ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9'])
    print("Success ...")
