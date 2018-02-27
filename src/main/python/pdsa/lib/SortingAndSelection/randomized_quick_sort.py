import random
from nose.tools import assert_list_equal


def swap(A, i, j):
    A[i], A[j] = A[j], A[i]


def randomized_quick_sort(A, p, r):
    if p < r:
        pivot_pos = randomized_partition(A, p, r)
        randomized_quick_sort(A, p, pivot_pos - 1)
        randomized_quick_sort(A, pivot_pos + 1, r)


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
    swap(A, lte+1, r)  # Put the pivot at right place
    return lte + 1  # Return pivot position.

if __name__ == "__main__":
    A = [20, 10, 5, 33, 44, 20, 1, 0, 8, 9, 43, 42, 97, 11, 9, 0]
    randomized_quick_sort(A, 0, len(A)-1)
    assert_list_equal(A, [0, 0, 1, 5, 8, 9, 9, 10, 11, 20, 20, 33, 42, 43, 44, 97])
