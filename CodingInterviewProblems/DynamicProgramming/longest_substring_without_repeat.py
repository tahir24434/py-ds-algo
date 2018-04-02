"""
Given a string, find the length of the longest substring without repeating
characters.
https://www.youtube.com/watch?v=sZosU8JjVaA
"""


def longest_substring_len(string):
    s_len = len(string)
    start = max_len = 0
    ind_vals = dict()

    for end in range(s_len):
        c = string[end]
        if c in ind_vals.keys():
            start = ind_vals[c] + 1
        ind_vals[c] = end
        max_len = max(end - start, max_len)
    return max(s_len-start, max_len)

if __name__ == "__main__":
    print(longest_substring_len("abcaaefghia"))
    print(longest_substring_len("a"))

