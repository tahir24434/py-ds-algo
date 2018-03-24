"""
Given an array of size n-1 and given that there are numbers from 1 to n with one
missing, the missing number is to be found.
"""
from nose.tools import assert_equal


def find_missing(A):
    n = len(A)
    sum_of_n_numbers = (n + 1) * (n + 2) / 2  # actual sum formula: n * (n+1) / 2
    actual_sum = sum(A)
    missing = sum_of_n_numbers - actual_sum
    return missing


if __name__ == "__main__":
    A = [3, 4, 1, 5, 6, 8, 7, 9]
    print(find_missing(A))
