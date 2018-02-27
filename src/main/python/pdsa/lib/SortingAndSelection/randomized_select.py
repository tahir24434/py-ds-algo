"""
The ith order statistics of a set of n of elements is the ith smallest element.
For example, the minimum of a set of elements is the first order statistic (i = 1).
And the maximum is nth order statistic (i = n).
A median, informally, is the 'halfway point' of the set. When n is odd, the median
is unique, occuring at i=(n+1)/2. When n is even, there are two medians, occurring
at i=n/2 and i=n/2+1. Thus regardless of parity of n, medians occur at
i=floor[(n+1)/2] (lower median) and i=ceil[(n+1)/2] (upper median). We consistently
 use the phrase 'the median' to refer to the lower median.
Selection problem:
------------------
Input: A set A of n (distinct) numbers and an integer i, with 1<= i <=n.
Output: The element x belongs to A that is larger than exactly i-1 other elements of A.
We can solve the selection problem in O(nlogn) time, since we can sort the numbers using
heapsort or mergesort and then simply index the ith element in the output array. However,
we will solve this using faster algorithm.
--- minimum and maximum:
We can easily obtain an upper bound of n-1 comparisons: examine each element of the set
in turn and keep track of the smallest element seen so far.
-- Selection in linear time:
The general selection problem appears more difficult than the simple problem of finding
a minimum. Yet, surprisingly, the asymptotic running time for both problems is the same:
O(n).
"""
import random
from nose.tools import assert_equal


def swap(A, i, j):
    A[i], A[j] = A[j], A[i]


def randomized_partition(A, p, r):
    i = random.randint(p, r)
    swap(A, i, r)
    return partition(A, p, r)


def partition(A, p, r):
    pivot = A[r]
    lte = p - 1
    for i in range(p, r):
        if A[i] <= pivot:
            lte += 1
            swap(A, i, lte)
    swap(A, lte+1, r)
    return lte + 1


def randomized_select(A, p, r, i):
    if p == r:
        return A[p]
    q = randomized_partition(A, p, r)
    k = q - p + 1
    if i == k:
        return A[q]
    elif i < k:
        return randomized_select(A, p, q-1, i)
    else:
        return randomized_select(A, q+1, r, i-k)


if __name__ == "__main__":
    # [0, 0, 1, 5, 8, 9, 9, 10, 11, 20, 20, 33, 42, 43, 44, 97]
    A = [20, 10, 5, 33, 44, 20, 1, 0, 8, 9, 43, 42, 97, 11, 9, 0]
    elem = randomized_select(A, 0, len(A) - 1, 8)
    assert_equal(elem, 10)
    print("Success ...")
