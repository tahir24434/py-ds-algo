from nose.tools import assert_equal


def remove_dups(ll):
    unique_elems = set()
    walk = ll._header
    while walk._next is not None:
        e = walk._next._element
