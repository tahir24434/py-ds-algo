"""
Count ways to reach the n’th stair:
There are n stairs, a person standing at the bottom wants to reach the top.
The person can climb either 1 stair or 2 stairs at a time. Count the number of ways,
the person can reach the top.
"""


def num_ways(n):
    nw = [0] * (n + 1)
    nw[0] = 1
    nw[1] = 1
    for i in range(2, n+1):
        nw[i] = nw[i-2] + nw[i-1]
    return nw[n]