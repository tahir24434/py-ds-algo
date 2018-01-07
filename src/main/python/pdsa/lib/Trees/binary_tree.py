from pdsa.lib.Trees.tree import Tree


class BinaryTree(Tree):
    """
    Abstract base class representing a binary tree structure.
    """
    # ------------ Additional abstract method --------------
    def left(self, p):
        """
        Returns p's left child.
        """
        raise NotImplementedError("Must be implemented by a subclass")

    def right(self, p):
        """
        Returns p's right child.
        """
        raise NotImplementedError("Must be implemented by a subclass")

    # ------------- Concrete method implementing in this class -------------
    def sibling(self, p):
        """
        Returns p's sibling (or None if no sibling)
        """
        parent = self.parent(p)
        if parent is None:  # p must be root
            return None     # Root has no sibling
        if p == self.left(parent):
            return self.right(parent)   # Possibly None
        else:
            return self.left(parent)    # Possibly None

    def children(self, p):
        """
        Generate an iteration of nodes representing p's children
        """
        if self.left(p) is not None:
            yield self.left(p)
        if self.right(p) is not None:
            yield self.right(p)

    def inorder(self):
        """
        The inorder traversal algorithm, because it explicitly relies on the notion of a left
        and right child of a node, only applies to binary trees. We therefore include its
        definition within the body of BinaryTree class.
        :return:
        """
        if not self.is_empty():
            for p in self._subtree_inorder(self.root()):
                yield p

    def _subtree_inorder(self, p):
        if self.left(p) is not None:
            for other in self._subtree_inorder(self.left(p)):
                yield other
        yield p
        if self.right(p) is not None:
            for other in self._subtree_inorder(self.right(p)):
                yield other
