"""
Write a method to return all subsets of a set.
"""


def power_set(S, m, subsets):
    if m == 0:
        subsets.append([S[m]])
        return [S[m]]

    res = power_set(S, m-1, subsets)
    print(res)

    for i in range(len(res)):
        subsets.append([res[i], S[m]])
    subsets.append([S[m]])
    return subsets


if __name__ == "__main__":
    S = [1, 2, 3]
    print(power_set(S, len(S)-1, []))
