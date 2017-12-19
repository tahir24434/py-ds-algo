from nose.tools import assert_equal


def urlify(s, length):
    string = list(s)
    act_len = len(string)
    back = act_len - 1
    for front in range(length-1, -1, -1):
        c = string[front]
        if c == " ":
            string[back-2] = "%"
            string[back-1] = "2"
            string[back] = "0"
            back -= 3
        else:
            string[back] = c
            back -= 1
    return "".join(string)

if __name__ == "__main__":
    assert_equal(urlify("Mr Arslan  ", 9), "Mr%20Arslan")
    assert_equal(urlify("Mr John Smith    ", 13), "Mr%20John%20Smith")
    print("Success ...")
