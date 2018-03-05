from nose.tools import assert_equal
from pdsa.lib.Trees.tree_map import TreeMap


class Rank(TreeMap):
    def get_rank(self, k):
        rank = 0
        for p in self._subtree_inorder(self.root()):
            if p.key() == k:
                return rank
            elif p.key() < k:
                rank += 1

    # NOTE: For this question, we need only below code.
    def _subtree_inorder(self, p):
        if self.left(p) is not None:
            for other in self._subtree_inorder(self.left(p)):
                yield other
        yield p
        if self.right(p) is not None:
            for other in self._subtree_inorder(self.right(p)):
                yield other

if __name__ == "__main__":
    A = [14, 5, 9, 6, 7]
    bst = Rank()
    for i in A:
        bst.insert(i, None)
        print("%s inserted" % i)
    assert_equal(bst.get_rank(5), 0)
    assert_equal(bst.get_rank(9), 3)
    bst.insert(11, None)
    assert_equal(bst.get_rank(11), 4)
    bst.insert(1, None)
    assert_equal(bst.get_rank(1), 0)
    print("Success ...")
