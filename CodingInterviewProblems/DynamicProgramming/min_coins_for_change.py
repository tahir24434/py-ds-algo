"""
Given an unlimited supply of coins of given denominations, find the minimum number
of coins required to get a desired change.
"""


def min_coins(target, coins, m):
    if target == 0:
        return 0
    if m == 0:
        return float('inf')
    if coins[m-1] > target:
        return min_coins(target, coins, m-1)

    num_coins_incl = min_coins(target - coins[m-1], coins, m) + 1
    num_coins_excl = min_coins(target, coins, m-1)
    return min(num_coins_incl, num_coins_excl)


if __name__ == "__main__":
    coins = [1, 2, 3, 4]
    target = 10
    print(min_coins(target, coins, len(coins)))
