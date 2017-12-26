from nose.tools import assert_true, assert_equal
from pdsa.lib.LinkedLists.positional_singly_list import SinglyLinkedList


def find_intersection(sl1, sl2):
    sl1_size = len(sl1)
    sl2_size = len(sl2)
    longer = sl1
    shorter = sl2
    if sl1_size < sl2_size:
        longer = sl2
        shorter = sl1
    size_diff = abs(sl1_size - sl2_size)

    shorter_walk = shorter.first()
    longer_walk = longer.first()
    for i in range(size_diff):
        longer_walk = longer.after(longer_walk)

    while longer_walk is not None:
        if longer_walk == shorter_walk:
            return longer_walk
        longer_walk = longer.after(longer_walk)
        shorter_walk = shorter.after(shorter_walk)
    return False

if __name__ == "__main__":
    sl1 = SinglyLinkedList()
    sl1.add_first(1)
    sl1.add_first(2)
    i = sl1.add_first(7)
    sl1.add_first(9)
    sl1.add_first(5)
    sl1.add_first(1)
    sl1.add_first(3)
    sl2 = SinglyLinkedList()
    sl2.add_before(i, 6)
    sl2.add_first(4)
    assert_equal(find_intersection(sl1, sl2), i)
