"""
Given weights and values of n items, put these items in a knapsack of capacity W to
get the maximum total value in the knapsack. In other words, given two integer
arrays val[0..n-1] and wt[0..n-1] which represent values and weights associated
with n items respectively. Also given an integer W which represents knapsack
capacity,
find out the maximum value subset of val[] such that sum of the weights of this
subset is smaller than or equal to W.
You cannot break an item, either pick the complete item, or don’t pick it (0-1
property).
"""


def pick_items(w, v, n, target, subset):
    if target == 0:
        print(subset)
        return
    if n == 0:
        return

    if w[n-1] > target:
        return pick_items(w, v, n - 1, target, subset)

    return pick_items(w, v, n-1, target-w[n-1], subset+str(v[n-1])+ " ") or \
           pick_items(w, v, n - 1, target, subset)


def pick_items_max_val(w, v, n, target, subset):
    if target == 0:
        print(subset)
        return 0
    if n == 0:
        return 0

    if w[n-1] > target:
        return pick_items_max_val(w, v, n - 1, target, subset)

    included = pick_items_max_val(w, v, n-1, target-w[n-1], subset + str(v[n-1]) + " ")
    not_included = pick_items_max_val(w, v, n - 1, target, subset)
    return max(v[n-1] + included, not_included)


if __name__ == "__main__":
    wt = [20, 10, 30, 40]
    vl = [2, 1, 3, 4]
    pick_items(wt, vl, len(wt), 50, " ")
    print("*****")
    print(pick_items_max_val(wt, vl, len(wt), 51, " "))

