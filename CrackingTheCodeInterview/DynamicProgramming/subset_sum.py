"""
Given a set of non-negative integers, and a value sum, determine if there is a
subset of the given set with sum equal to given sum.

Examples: set[] = {3, 34, 4, 12, 5, 2}, sum = 9
Output:  True  //There is a subset (4, 5) with sum 9.

https://www.youtube.com/watch?v=GdZSzita5V8
http://www.edufyme.com/code/?id=c0c7c76d30bd3dcaefc96f40275bdc0a
https://www.geeksforgeeks.org/dynamic-programming-subset-sum-problem/
"""
from nose.tools import assert_true
from nose.tools import assert_false


def subset_sum(set, sum, n):
    # Base case
    if sum == 0:
        return True
    if sum != 0 and n == 0:
        return False

    # If last element is greater than sum, then ignore it
    if set[n-1] > sum:
        return subset_sum(set, sum, n-1)
    # else, check if sum can be obtained by any of the following
    #   (a) including the last element
    #   (b) excluding the last element
    return subset_sum(set, sum-set[n-1], n-1) or subset_sum(set, sum, n-1)


def subset_sum_print(set, sum, n, subset):
    """
    Subset Sum: Print all subsets with the required sum, Python code
    """
    # Base case
    if sum == 0:
        print(subset)
        return
    if n == 0:
        return

    # If last element is greater than sum, then ignore it
    if set[n-1] > sum:
        return subset_sum_print(set, sum, n-1, subset)
    # else, check if sum can be obtained by any of the following
    #   (a) including the last element
    #   (b) excluding the last element
    return subset_sum_print(set, sum-set[n-1], n-1, subset+str(set[n-1])+" ") or \
           subset_sum_print(set, sum, n-1, subset)

if __name__ == "__main__":
    s = [3, 34, 4, 12, 5, 2]
    assert_true(subset_sum(s, 9, len(s)))
    s = [3, 34, 4, 12, 5, 2]
    assert_false(subset_sum(s, 900, len(s)))

    s = [3, 34, 4, 12, 5, 2]
    subset_sum_print(s, 9, len(s), " ")
    print("Success ...")
