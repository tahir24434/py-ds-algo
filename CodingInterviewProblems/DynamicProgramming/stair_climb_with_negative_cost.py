"""
On a staircase, the i-th step has some non-negative cost cost[i] assigned (0 indexed).

Once you pay the cost, you can either climb one or two steps. You need to find
minimum cost to reach the top of the floor, and you can either start from the step
with index 0, or the step with index 1.

Example 1:
Input: cost = [10, 15, 20, 10]
Output: 15
Explanation: Cheapest is start on cost[1], pay that cost and go to the top.
Example 2:
Input: cost = [1, 100, 1, 1, 1, 100, 1, 1, 100, 1]
Output: 6
Explanation: Cheapest is start on cost[0], and only step on 1s, skipping cost[3].
Note:
cost will have a length in the range [2, 1000].
Every cost[i] will be an integer in the range [0, 999].
"""


def min_cost_to_reach(cost_array, n):
    cost_array.append(0)
    memo = {}
    if n > len(cost_array):
        return None
    res = min_cost(cost_array, n, memo)
    return res


def min_cost(cost_array, n, memo):
    if n == 0:
        return cost_array[0]
    if n == 1:
        return cost_array[1]

    if n not in memo:
        a = min_cost(cost_array, n - 1, memo) + cost_array[n]
        b = min_cost(cost_array, n-2, memo) + cost_array[n]
        memo[n] = min(a, b)
    return memo[n]


if __name__ == "__main__":
    costs = [10, 15, 20]
    step = 3
    print(min_cost_to_reach(costs, step))

    costs = [3, 1, 1, 10, 2, 4, 40, 50, 3]
    step = 8
    print(min_cost_to_reach(costs, step))