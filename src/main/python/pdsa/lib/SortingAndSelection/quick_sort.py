# Worst-case running time : O(n^2)
# However it is best practical choice for sorting as it is remarkably efficient on average O(nlogn).
# Constant factors hidden in O(nlogn) are quite small.
# It also has advantage of in place sorting.


def swap(A, i, j):
    A[i], A[j] = A[j], A[i]


def quick_sort(A, p, r):
    if p < r:
        pivot_pos = partition(A, p, r)
        quick_sort(A, p, pivot_pos - 1)
        quick_sort(A, pivot_pos + 1, r)


# Partition rearranges the sub-array A[p..r] in place.
# Partition always selects an element x = A[r] as pivot element around which to partition the subarray A[p..r].
# As the procedure runs, it partitions the array into four (possibly empty) regions.
#   First partition will hold elements with values smaller than or equal to pivot.
#   Second partition will hold elements greater than pivot.
#   Third partition will hold elements which have not been yet put in one of the first two partitions.
#   Fourth partition holds pivot.
def partition(A, p, r):
    pivot = A[r]
    lte = p - 1
    for i in range(p, r):
        if A[i] <= pivot:
            lte += 1
            swap(A, i, lte)

    swap(A, lte + 1, r)  # Put the pivot at right place
    return lte + 1  # Return pivot position.


A = [4, 3, 1, 7, 9, 11, 0, 2, 90, 70, 23]
quick_sort(A, 0, len(A)-1)
print (A)
