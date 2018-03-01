from nose.tools import assert_equal


def sparse_search(A, left, right, val):
    while left < right:
        mid = (left + right) // 2
        if not A[mid]:      # Mid is empty
            i = mid - 1
            j = mid + 1
            while True:
                if i == left and j == right and not A[i] and not A[j]:
                    return None
                if A[i]:
                    mid = i
                    break
                elif i > left and not A[i]:
                    i -= 1
                if A[j]:
                    mid = j
                    break
                elif j < right and not A[j]:
                    j += 1

        if A[mid] == val:
            return mid
        elif A[mid] < val:
            left = mid + 1
        else:
            right = mid - 1

    return None

if __name__ == "__main__":
    A = ["at", "", "", "", "ball", "", "", "car", "", "", "dad", "", ""]
    assert_equal(sparse_search(A, 0, len(A)-1, 'ball'), 4)
    A = ["at", "", "", "", "", "", "", "", "dad"]
    assert_equal(sparse_search(A, 0, len(A)-1, 'at'), 0)
    A = ["at", "", "", "", "", "", "", "", "dad"]
    assert_equal(sparse_search(A, 0, len(A)-1, 'dad'), 8)
    A = ["", "", "", "", "", "", "", "", ""]
    assert_equal(sparse_search(A, 0, len(A)-1, 'dad'), None)
    print("Success ...")
