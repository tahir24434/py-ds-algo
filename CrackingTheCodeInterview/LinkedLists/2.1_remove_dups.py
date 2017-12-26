from pdsa.lib.LinkedLists.positional_doubly_list import DoublyLinkedList


def remove_dups(pl):
    unique_elems = set()
    walk = pl.first()
    while walk is not None:
        after = pl.after(walk)
        e = walk.element()
        if e in unique_elems:
            pl.delete(walk)
        else:
            unique_elems.add(e)
        walk = after

if __name__ == "__main__":
    pl = DoublyLinkedList()
    pl.add_first(7)
    pl.add_first(2)
    pl.add_first(7)
    pl.add_first(9)             #   9 7 2 7
    p = pl.add_first(7)         # 7 9 7 2 7
    pl.add_after(4, p)          # 7 4 9 7 2 7
    p = pl.add_before(5, p)     # 5 7 4 9 7 2 7
    pl.add_after(7, p)          # 5 7 7 4 9 7 2 7
    for e in pl:
        print(e)
    remove_dups(pl)
    print("After removing duplicates")
    for e in pl:
        print(e)


