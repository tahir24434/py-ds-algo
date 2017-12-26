from nose.tools import assert_equal
from pdsa.lib.LinkedLists.positional_singly_list import SinglyLinkedList


def sum_lists(l1, l2):
    """
    :param l1: SinglyLinkedList
    :param l2: SinglyLinkedList
    :return:
    """
    res = ""
    carry = 0
    l1_walk = l1.first()
    l2_walk = l2.first()
    while l1_walk is not None and l2_walk is not None:
        tmp = l1_walk.element() + l2_walk.element() + carry
        res = str(tmp % 10) + res
        carry = tmp // 10
        l1_walk = l1.after(l1_walk)
        l2_walk = l2.after(l2_walk)

    if l1_walk is None and l2_walk is None:
        res = str(carry) + res
    else:
        while l1_walk is not None:
            tmp = l1_walk.element() + carry
            res += tmp // 2
            carry = tmp % 2
            l1_walk = l1.after(l1_walk)

        while l2_walk is not None:
            tmp = l2_walk.element() + carry
            res += tmp // 2
            carry = tmp % 2
            l2_walk = l2.after(l2_walk)

    return res


if __name__ == "__main__":
    l1 = SinglyLinkedList()
    l1.add_first(6)
    l1.add_first(1)
    l1.add_first(7)
    l2 = SinglyLinkedList()
    l2.add_first(4)
    l2.add_first(9)
    l2.add_first(5)
    assert_equal(sum_lists(l1, l2), "1112")
    print("Success ...")
