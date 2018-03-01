from nose.tools import assert_equal

def elementAt(A, i):
    try:
        element = A[i]
    except IndexError:
        element = -1
    return element


def binary_search(A, item, low, high):
    while low <= high:
        mid = (low + high)//2
        if A[mid] == item:
            return mid
        elif A[mid] < item:
            low = mid + 1
        else:
            high = mid - 1
    return -1


def sorted_search(A, item):
    idx = 1
    while (elementAt(A, idx) >= 0) and (elementAt(A, idx) <= item):
        idx *= 2
    return binary_search(A, item, idx//2, idx)

if __name__ == "__main__":
    A = [3, 4, 5, 6, 7, 8, 9]
    assert_equal(sorted_search(A, 3), 0)
    assert_equal(sorted_search(A, 9), 6)
    assert_equal(sorted_search(A, 4), 1)
    assert_equal(sorted_search(A, 8), 5)
    assert_equal(sorted_search(A, 6), 3)
    print("Success ...")
