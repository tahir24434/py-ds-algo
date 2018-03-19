"""
Write a program to count number of ways to calculate a target number from elements
of specified array by using only addition and subtraction operator. The use of any
other operator is forbidden.
"""
from nose.tools import assert_equal, assert_list_equal


def num_ways(A, target):
    memo = {}
    return _num_ways(A, target, len(A), memo)


def _num_ways(A, target, m, memo):
    if target == 0:
        return 1
    if m == 0:
        return 0

    key = (target, m)
    if key not in memo:
        if A[m-1] > target:
            memo[key] = _num_ways(A, target, m-1, memo)
        else:
            include = _num_ways(A, target - A[m-1], m-1, memo) + \
                      _num_ways(A, target + A[m-1], m-1, memo)
            exclude = _num_ways(A, target, m-1, memo)
            memo[key] = include + exclude
    return memo[key]


def ways_to_reach_target(A, target):
    memo = {}
    chosen = []
    return _ways_to_reach_target(A, target, len(A), memo, chosen)


def _ways_to_reach_target(A, target, m, memo, chosen):
    if target == 0:
        print(chosen)
        return 1
    if m == 0:
        return 0

    key = (target, m)
    if key not in memo:
        if A[m-1] > target:
            memo[key] = _num_ways(A, target, m-1, memo)
        else:
            chosen.append(A[m-1])
            include = _ways_to_reach_target(A, target - A[m-1], m-1, memo, chosen) + \
                      _ways_to_reach_target(A, target + A[m-1], m-1, memo, chosen)
            chosen.pop()
            exclude = _ways_to_reach_target(A, target, m-1, memo, chosen)
            memo[key] = include + exclude
    return memo[key]


def num_ways_alt(A, target):
    if target == 0:
        return 1
    if len(A) == 0:
        return 0

    res = 0
    for i in range(len(A)-1, -1, -1):
        res += num_ways_alt(A[:i], target - A[i])
        res += num_ways_alt(A[:i], target + A[i])
    return res


if __name__ == "__main__":
    A = [5, 3, -6, 2]
    assert_equal(num_ways(A, 6), 2)
    A = [1, 2]
    assert_equal(num_ways(A, 3), 1)

    A = [1, 2]
    assert_equal(ways_to_reach_target(A, 3), 1)

    print("Success ...")
