from pdsa.lib.Stacks.array_stack import ArrayStack


def insert_element_in_sorted_order(uss, ss, e):
    """
    Insert element in sorted stack at right position.
    :param st:
    :param e:
    :return:
    """
    while not ss.is_empty() and e < ss.top():
        uss.push(ss.pop())
    ss.push(e)


def sort_stack(uss):
    ss = ArrayStack()
    while not uss.is_empty():
        e = uss.pop()
        insert_element_in_sorted_order(uss, ss, e)
    while not ss.is_empty():
        uss.push(ss.pop())


if __name__ == "__main__":
    us = ArrayStack()
    us.push(5)
    us.push(1)
    us.push(9)
    us.push(7)
    us.push(10)
    us.push(6)
    us.push(0)
    us.push(15)
    sort_stack(us)
    while not us.is_empty():
        print(us.pop())
