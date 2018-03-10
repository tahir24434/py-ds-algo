"""
Given a value N, if we want to make change for N cents, and we have infinite supply
of each of S = { S1, S2, .. , Sm} valued coins, how many ways can we make the
change? The order of coins doesn’t matter.

For example, for N = 4 and S = {1,2,3}, there are four solutions:
{1,1,1,1},{1,1,2},{2,2},{1,3}. So output should be 4.
For N = 10 and S = {2, 5, 3, 6}, there are five solutions:
{2,2,2,2,2}, {2,2,3,3}, {2,2,6}, {2,3,5} and {5,5}. So the output should be 5.

https://www.youtube.com/watch?v=k4y5Pr0YVhg
"""
from nose.tools import assert_equal


def coin_change_ways(amount, coins, current_coin):
    if amount == 0:
        return 1
    if amount < 0:
        return 0

    nw = 0
    for i in range(current_coin, len(coins)):
        nw += coin_change_ways(amount-coins[i], coins, i)
    return nw


if __name__ == "__main__":
    N = 4
    S = [1, 2, 3]
    assert_equal(coin_change_ways(N, S, 0), 4)

    N = 10
    S = [2, 5, 3, 6]
    assert_equal(coin_change_ways(N, S, 0), 5)
    print("Success ...")
