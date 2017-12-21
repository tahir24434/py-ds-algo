from nose.tools import assert_equal, assert_is_none
from pdsa.lib.LinkedLists.positional_singly_list import SinglyLinkedList


def kth_to_last(sl, k):
    front = back = sl.first()
    i = 0
    while front is not None and i != k:
        front = sl.after(front)
        i += 1
    if i != k:
        print("List does not have enough element")
        return None

    while front is not None:
        front = sl.after(front)
        back = sl.after(back)

    return back.element()


# Test second from last when there is only one element in linkedlist.
if __name__ == "__main__":
    sl = SinglyLinkedList()
    sl.add_first(4)
    sl.add_first(3)
    sl.add_first(2)
    sl.add_first(1)
    sl.add_first(0)
    assert_equal(kth_to_last(sl, 1), 4)
    assert_equal(kth_to_last(sl, 2), 3)
    assert_equal(kth_to_last(sl, 3), 2)
    assert_equal(kth_to_last(sl, 4), 1)
    assert_equal(kth_to_last(sl, 5), 0)
    assert_is_none(kth_to_last(sl, 7))
    print("Success ...")
