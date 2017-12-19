class Tree:
    """
    Abstract base class representing a tree structure.
    """
    class Position:
        """
        An abstraction representing the location of a single element.
        """
        def element(self):
            """
            :return: Returns an element stored at this position.
            """
            raise NotImplementedError('Must be implemented by subclass')

        def __eq__(self, other):
            """
            :param other:
            :return: Returns True if other Position represents the same location.
            """
            raise NotImplementedError('Must be implemented by subclass')

        def __ne__(self, other):
            """
            :param other:
            :return: Returns True if other Position does NOT represents the same location.
            """

    def root(self):
        """
        :return: Return Position representing the tree's root (or none if empty).
        """
        raise NotImplementedError('Must be implemented by subclass')

    def parent(self, p):
        """
        Parameters
        ----------
        p : Position
        Returns
        -------
            Return Position representing p's parent (or None of p is root).
        """
        raise NotImplementedError('Must be implemented by subclass')

    def num_children(self, p):
        """
        Returns
        -------
            the number of children that position p has.
        """
        raise NotImplementedError('Must be implemented by subclass')

    def children(self, p):
        """
        Generate an iteration of positions representing p's children.
        """
        raise NotImplementedError('Must be implemented by subclass')

    def __len__(self):
        """
        Returns the total number of elements in the tree.
        """
        raise NotImplementedError('Must be implemented by subclass')

    # --------- Concrete methods implemented in this class ----------
    def is_root(self, p):
        """
        Returns True if position p represents the root of the tree.
        """
        return self.root() == p

    def is_leaf(self, p):
        """
        Returns True if position p does NOT have any children.
        """
        return self.num_children(p) == 0

    def is_empty(self):
        """
        Returns True if tree is empty
        """
        return len(self) == 0

    def depth(self, p=None):
        """
        Depth of p is number of ancestors of p, excluding p itself.
        Depth of the root of the tree is 0.
        """
        if p is None:
            p = self.root()
        return self._depth(p)

    def _depth(self, p):
        if self.is_root(p):
            return 0
        return 1 + self._depth(self.parent(p))

    def height(self, p=None):
        """
        Height of node p is number of descendants of p.
        Height of the leaf node of tree is 0.
        """
        if p is None:
            p = self.root()
        return self._height(p)

    def _height(self, p):
        if self.is_leaf(p):
            return 0
        return 1 + max(self._height(c) for c in self.children(p))
