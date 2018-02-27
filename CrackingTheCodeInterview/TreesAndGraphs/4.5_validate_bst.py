from nose.tools import assert_true, assert_false
from pdsa.lib.Trees.tree_map import TreeMap


def validate_bst(bst):
    return _validate_bst(bst.root(), float('-inf'), float('inf'))


def _validate_bst(p, min, max):
    if p.key() < str(min) or p.key() > str(max):
        return False
    if bst.left(p) is not None:
        _validate_bst(bst.left(p), min, p.key())
    if bst.right(p) is not None:
        _validate_bst(bst.right(p), p.key(), max)
    return True


if __name__ == "__main__":
    bst = TreeMap()
    bst["21"] = 1
    bst["32"] = 9
    bst["24"] = 7
    bst["15"] = 0
    bst["13"] = 0
    bst["18"] = 0
    assert_true(validate_bst(bst))

    print("Success")
