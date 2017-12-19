from tree import Tree


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

    def num_children(self, p):
        count = 0
        if self.left(p) is not None:
            count += 1
        if self.right(p) is not None:
            count += 1
        return count
