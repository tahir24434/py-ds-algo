"""
Please implement a function that gets the minimal number of coins with values
v1, v2 , …, vn
to make change for an amount of money with value t. There are an infinite number
of coins for each value vi.
For example, the minimum number of coins to make change for 15 out of a set of coins
with values 1, 3, 9, 10 is 3. We can choose two coins with value 3 and a coin with
value 9. The number of coins for other choices should be greater than 3.

Coding Interview: Questions, analysis and Solutions
"""
from nose.tools import assert_equal


def min_num_coins(V, target, n):
    if target == 0:
        return 0
    if n == 0:
        return float('inf')
    if target == V[n-1]:
        return 1

    if target < V[n-1]:
        return min_num_coins(V, target, n-1)

    incl = 1 + min_num_coins(V, target-V[n-1], n)
    excl = min_num_coins(V, target, n-1)
    return min(incl, excl)


if __name__ == "__main__":
    V = [1, 3, 9, 10]
    t = 15
    mem = [[0] * (len(V)+1)] * (t+1)
    assert_equal(min_num_coins(V, t, n=len(V)), 3)
    print("Success ...")

