def group_anagrams(A):
    e_dict = dict()
    for e in A:
        se = ''.join(sorted(e))
        if se not in e_dict:
            e_dict[se] = []
        e_dict[se].append(e)

    print(e_dict)
    i = 0
    for vals in e_dict.values():
        for anags in vals:
            A[i] = anags
            i += 1
    print(A)


if __name__ == "__main__":
    A = ["acre", "race", "gab", "don", "rcea", "bag"]
    group_anagrams(A)

