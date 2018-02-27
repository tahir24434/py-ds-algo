import operator
import math


def merge(A, p, q, r):
    print(p, q, r)
    left = A[p:q+1] + [float('inf')]
    right = A[q+1:r+1] + [float('inf')]
    print(left)
    print(right)
    i = j = 0

    for x in range(p, r+1):
        if left[i] < right[j]:
            A[x] = left[i]
            i += 1
        else:
            A[x] = right[j]
            j += 1


def merge_sort(A, p, r):
    if p < r:
        q = (p+r)//2
        merge_sort(A, p, q)
        merge_sort(A, q+1, r)
        merge(A, p, q, r)

if __name__ == "__main__":
    # [0, 0, 1, 5, 8, 9, 9, 10, 11, 20, 20, 33, 42, 43, 44, 97]
    A = [20, 10, 5, 33, 44, 20, 1, 0, 8, 9, 43, 42, 97, 11, 9, 0]
    merge_sort(A, 0, len(A)-1)
    print(A)
