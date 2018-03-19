"""
Write a method to compute all permutations of a string of unique characters.
"""


def find_permutation(s, m, perms):
    res = []
    if m == 0:
        res.append(s[m])
        perms.append(res)
        return res

    prev_perm = find_permutation(s, m-1, perms)
    for p in prev_perm:
        # append s[m-1] at every possible place of p.
        for i in range(len(p)+1):
            res.append(p[:i] + s[m] + p[i:])

    perms.append(res)
    return res


if __name__ == "__main__":
    string = "abc"
    perms = []
    find_permutation(string, len(string)-1, perms)
    print(perms)

