"""
A thief breaks into a clock store. His knapsack will hold at most w ounces of clocks.
Clock i weighs wi ounces and retails for vi dollars. The thief must either take or
leave a clock, and he cannot take a fractional amount of an item. His intention is
to take clocks whose total value is maximum subject to the knapsack's weight
constraint.
Write a program for the knapsack problem that selects a subset of items that has
maximum value and satisfies the weight constraint.
"""
from nose.tools import assert_equal


# TODO: It prints all possible solutions. To print the solution with maximum
# value, I guess we have to follow the DP approach.
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
    assert_equal(max_pick(W, V, N, 60, len(W), " "), 255)
