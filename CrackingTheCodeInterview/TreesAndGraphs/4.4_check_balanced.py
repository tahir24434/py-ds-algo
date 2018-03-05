from nose.tools import assert_false, assert_true
from pdsa.lib.Trees.tree_map import TreeMap

def _is_balanced(bst, p):
    if p is None:
        return 0

    lh = _is_balanced(bst, bst.left(p))
    if lh == -1:  # If left child is not balanced
        return -1
    rh = _is_balanced(bst, bst.right(p))
    if rh == -1:  # If right child is not balanced
        return -1

    if abs(lh - rh) > 1:
        return -1
    else:
        return max(lh, rh) + 1  # Return Height


def is_balanced(bst):
    if _is_balanced(bst, bst.root()) == -1:
        return False
    else:
        return True


if __name__ == "__main__":
    bst = TreeMap()
    bst["21"] = 1
    assert_true(is_balanced(bst))
    bst["32"] = 9
    assert_true(is_balanced(bst))
    bst["24"] = 7
    assert_false(is_balanced(bst))
    bst["15"] = 0
    assert_true(is_balanced(bst))
    bst["13"] = 0
    assert_true(is_balanced(bst))
    bst["18"] = 0
    assert_true(is_balanced(bst))
    print("Success ...")
