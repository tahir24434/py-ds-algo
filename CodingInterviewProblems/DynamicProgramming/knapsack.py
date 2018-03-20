"""
A thief breaks into a clock store. His knapsack will hold at most w ounces of clocks.
Clock i weighs wi ounces and retails for vi dollars. The thief must either take or
leave a clock, and he cannot take a fractional amount of an item. His intention is
to take clocks whose total value is maximum subject to the knapsack's weight
constraint.
Write a program for the knapsack problem that selects a subset of items that has
maximum value and satisfies the weight constraint.

http://www.techiedelight.com/0-1-knapsack-problem/
http://oucsace.cs.ohiou.edu/~razvan/courses/cs4040/lecture16.pdf
https://www.programminglogic.com/knapsack-problem-dynamic-programming-algorithm/
"""
from nose.tools import assert_equal


def knapsack(W, V, N, c):
    """

    :param W:
        Weights stored in array
    :param V:
        Values stored in array
    :param N:
        Labels stored in array
    :param c:
        knapsack capacity
    :return:
    """
    memo = {}
    subset = {}
    res = _knapsack(W, V, N, c, len(W), subset, memo)
    print(subset)
    print(memo)
    return res


def _knapsack(W, V, N, c, m, subset, memo):
    """

    :param W:
        Weights stored in array
    :param V:
        Values stored in array
    :param N:
        Labels stored in array
    :param c:
        knapsack capacity
    :param m:
        Number of distinct items
    :param subset:
        Subset to keep track of selected items
    :param memo:
        Map to store solution of sub-problems
    :return:
    """
    # Base case: no items left.
    if m == 0:
        return 0
    # Base case: No capacity in knapsack
    if c <= 0:
        return 0

    # Construct a unique map key from dynamic elements of the input.
    key = (c, m)
    if key not in memo:
        # Case 1: Include current item in knapsack and then recurse for remaining
        # elements with decreased capacity.
        if W[m-1] > c:
            memo[key] = _knapsack(W, V, N, c, m-1, subset, memo)
        else:
            include = V[m-1] + _knapsack(W, V, N, c-W[m-1], m-1, subset, memo)
            exclude = _knapsack(W, V, N, c, m-1, subset, memo)
            if include > exclude:
                subset[key] = 1
            else:
                subset[key] = -1
            memo[key] = max(include, exclude)

    # Return solution to current sub-problem
    return memo[key]


# TODO: It prints all possible solutions.
def max_pick(W, V, N, w, m, subset):
    # if capacity is 0 or available items are 0
    if w == 0:
        print(subset)
        return 0
    if m == 0:
        print(subset)
        return 0

    if W[m-1] > w:
        return max_pick(W, V, N, w, m-1, subset)

    return max(V[m-1] + max_pick(W, V, N, w-W[m-1], m-1, subset+str(N[m-1])+" "),
               max_pick(W, V, N, w, m-1, subset))


if __name__ == "__main__":
    W = [20, 8, 60, 55, 40, 70, 85, 25]
    V = [65, 35, 45, 195, 65, 150, 275, 155]
    N = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']
    #assert_equal(max_pick(W, V, N, 60, len(W), ""), 255)
    assert_equal(knapsack(W, V, N, 60), 255)
    W = [1, 5, 10, 15]
    V = [20, 25, 8, 35]
    N = ['A', 'B', 'C', 'D']
    #assert_equal(max_pick(W, V, N, 10, len(W), ""), 45)
    assert_equal(knapsack(W, V, N, 11), 45)

