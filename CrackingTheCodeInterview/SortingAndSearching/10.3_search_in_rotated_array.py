"""
Given a sorted array of n integers that has been rotated an unknown number of times,
write code to find an element in the array. You may assume that the array was
originally sorted in increasing order.
Input: find 5 in {15, 16, 19, 20, 25, 1, 3, 4, 5, 7, 10, 14}
"""
from nose.tools import assert_equal


def _search(A, left, right, val):
    while left <= right:
        mid = (left + right) // 2
        if A[mid] == val:
            return mid

        # Left side is sorted.
        if A[left] < A[mid]:
            if A[mid] < val:    # Search right
                left = mid + 1
            else:
                right = mid - 1
        # Right side is sorted
        elif A[mid] < A[right]:
            if A[mid] > val:    # Search left
                right = mid - 1
            else:
                left = mid + 1
        elif A[left] == A[mid]:     # Left side is all repeat
            if __name__ == '__main__':
                if A[mid] != A[right]:  # If right is different, search it
                    left = mid + 1
                else:   # We have to search both halves
                    res = _search(A, left, mid-1, val)
                    if res is None:
                        return _search(A, mid+1, right, val)
    return None


def search(A, val):
    return _search(A, 0, len(A)-1, val)


if __name__ == "__main__":
    A = [15, 16, 19, 20, 25, 1, 3, 4, 5, 7, 10, 14]
    assert_equal(search(A, 5), 8)
    A = [5, 7, 10, 14, 15, 16, 19, 20, 25, 1, 3, 4]
    assert_equal(search(A, 5), 0)
    A = [2, 2, 2, 3, 4, 2]
    assert_equal(search(A, 3), 3)
    A = [2, 2, 2, 2, 2, 2, 2, 2, 2, 3, 2]
    assert_equal(search(A, 3), 9)
    print("Success ...")
