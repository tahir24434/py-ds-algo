from nose.tools import assert_true, assert_false
from pdsa.lib.Stacks.array_stack import ArrayStack
from pdsa.lib.LinkedLists.positional_singly_list import SinglyLinkedList


def is_palindrom(sl):
    st = ArrayStack()
    sl_size = len(sl)
    skip_mid = False if sl_size % 2 == 0 else True

    walk = sl.first()
    for i in range(sl_size//2):
        st.push(walk.element())
        walk = sl.after(walk)
    if skip_mid:
        walk = sl.after(walk)

    while walk is not None:
        if walk.element() != st.pop():
            return False
        walk = sl.after(walk)
    return True


if __name__ == "__main__":
    sl = SinglyLinkedList()
    sl.add_first(5)
    sl.add_first(4)
    sl.add_first(3)
    sl.add_first(4)
    sl.add_first(5)
    assert_true(is_palindrom(sl))

    sl = SinglyLinkedList()
    sl.add_first(5)
    sl.add_first(4)
    sl.add_first(3)
    sl.add_first(2)
    sl.add_first(5)
    assert_false(is_palindrom(sl))
    print("Success ...")
