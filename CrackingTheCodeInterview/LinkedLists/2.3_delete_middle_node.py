from nose.tools import assert_equal
from pdsa.lib.LinkedLists.positional_singly_list import SinglyLinkedList


def delete_middle_node(sl, p):
    front = back = sl.first()
    if front == p:
        return sl.remove_first()

    while front is not None:
        front = sl.after(front)
        if front == p:
            return sl.delete(back, front)
        back = front
    return None


if __name__ == "__main__":
    sl = SinglyLinkedList()
    fn = sl.add_first(6)
    assert_equal(delete_middle_node(sl, fn), 6)
    sl.add_first(5)
    test = sl.add_first(4)
    sl.add_first(3)
    mn = sl.add_first(2)
    ln = sl.add_first(1)
    assert_equal(delete_middle_node(sl, test), 4)
    assert_equal(delete_middle_node(sl, ln), 1)
    print("Success ...")
