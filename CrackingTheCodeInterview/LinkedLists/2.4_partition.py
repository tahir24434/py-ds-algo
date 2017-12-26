from pdsa.lib.LinkedLists.positional_doubly_list import DoublyLinkedList

def partition(dl, e):
    walk = dl.first()
    i = 0
    while walk is not None and i < len(dl):
        curr_e = walk.element()
        next = dl.after(walk)
        if curr_e < e:
            dl.delete(walk)
            dl.add_first(curr_e)
        elif curr_e > e:
            dl.delete(walk)
            dl.add_last(curr_e)
        walk = next
        i += 1


if __name__ == "__main__":
    dl = DoublyLinkedList()
    dl.add_first(10)
    dl.add_first(2)
    dl.add_first(5)
    dl.add_first(11)
    dl.add_first(3)
    dl.add_first(5)
    dl.add_first(5)
    dl.add_first(12)
    dl.add_first(4)
    dl.add_first(13)
    dl.add_first(5)
    dl.add_first(3)
    dl.add_first(14)
    partition(dl, 5)
    for e in dl:
        print(e)
