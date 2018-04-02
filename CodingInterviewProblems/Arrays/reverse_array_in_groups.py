"""
Given an array, reverse every sub-array formed by consecutive k elements.
"""


def rev_arr_in_groups(A, k):
    len_A = len(A)
    for i in range(0, len_A, k):   # Total number of groups
        left = i
        right = min(i + k - 1, len_A-1)
        while left < right:
            A[left], A[right] = A[right], A[left]
            left += 1
            right -= 1


if __name__ == "__main__":
    A = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    rev_arr_in_groups(A, 3)
    print(A)

