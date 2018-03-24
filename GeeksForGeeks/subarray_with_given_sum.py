"""
Given an unsorted array of non-negative integers, find a continuous sub-array
which adds to a given number.
"""


def subarray_with_given_sum(A, desired_sum):
    for i in range(len(A)):
        sum = A[i]
        j = i + 1
        while sum <= desired_sum and j < len(A):
            if sum == desired_sum:
                return A[i:j]
            sum += A[j]
            j += 1

    return None


if __name__ == "__main__":
    A = [5, 3, 4, 9, 2, 5]
    desired_sum = 16
    print(subarray_with_given_sum(A, desired_sum))
    A = [5, 3, -3, 9, -2, 5]
    desired_sum = 6
    print(subarray_with_given_sum(A, desired_sum))
    A = [5, 3, 4, 9, 2, 5]
    desired_sum = 5
    print(subarray_with_given_sum(A, desired_sum))
