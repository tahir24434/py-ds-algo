"""
Given a distance ‘dist, count total number of ways to cover the distance with
1, 2 and 3 steps.

Examples:
Input:  n = 3
Output: 4
Below are the four ways
 1 step + 1 step + 1 step
 1 step + 2 step
 2 step + 1 step
 3 step
Input:  n = 4
Output: 7
"""
from nose.tools import assert_equal


def num_ways(d):
    if mem[d] is not None:
        return mem[d]
    res = 0
    if d == 0:
        res = 1
    elif d == 1 or d == 2:
        res = d
    else:
        res = num_ways(d-3) + num_ways(d-2) + num_ways(d-1)
    mem[d] = res
    return res


if __name__ == "__main__":
    num_steps = 4
    mem = [None] * (num_steps+1)
    assert_equal(num_ways(4), 7)
    print("Success ...")
