"""
Write a method to return all subsets of a set.
"""


def power_set(S, chosen, result):
    result.append([item for item in chosen])
    for i in range(len(S)):
        chosen.append(S[i])
        power_set(S[i+1:], chosen, result)
        chosen.pop()


if __name__ == "__main__":
    S = [1, 2, 3]
    chosen = []
    result = []
    power_set(S, chosen, result)
    print(result)
