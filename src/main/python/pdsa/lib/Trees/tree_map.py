from pdsa.lib.Trees.linked_binary_tree import LinkedBinaryTree


class TreeMap(LinkedBinaryTree):
    class Element:
        def __init__(self, key, value):
            self._key = key
            self._value = value

        def __eq__(self, other):
            return self._key == other._key

        def __ne__(self, other):
            return not (self == other)

    class Position(LinkedBinaryTree.Position):
        def key(self):
            return self.element()._key

        def value(self):
            return self.element()._value

    def _subtree_search(self, p, k):
        """
        Search position of item with key k. Return the neighbour element in case of failed
        search.
        :param p:
        :param k:
        :return:
        """
        if p.key() == k:
            return p
        elif k > p.key():
            if self.right(p) is not None:
                return self._subtree_search(self.right(p), k)
        else:
            if self.left(p) is not None:
                return self._subtree_search(self.left(p), k)
        return p

    def _subtree_first_position(self, p):
        """
        Return position of element with minimum key in tree rooted at p.
        :param p:
        :return:
        """
        # Element with minimum key will be the right most element of tree.
        walk = p
        while self.left(walk) is not None:
            walk = self.left(walk)
        return walk

    def _subtree_last_position(self, p):
        """
        Return position of element with maximum key in tree rooted at p.
        :param p:
        :return:
        """
        self._validate(p)
        # Element with minimum key will be the left most element of tree.
        walk = p
        while self.right(walk) is not None:
            walk = self.right(walk)
        return walk

    def find_position(self, k):
        """
        Find element with key k.
        :param k:
        :return:
        """
        if self.is_empty():
            return None
        return self._subtree_search(self.root(), k)

    def __getitem__(self, k):
        if self.is_empty():
            raise KeyError("Key Error: " + repr(k))
        p = self.find_position(k)
        if p.key() == k:
            return p.value()
        else:
            raise KeyError("Key Error: " + repr(k))

    def __setitem__(self, k, v):
        if self.is_empty():
            return self.add_root(self.Element(k, v))
        else:
            p = self.find_position(k)
            if p.key() == k:
                p.element()._value = v
                return
            else:
                elem = self.Element(k, v)
                if k < p.key():
                    return self.add_left(p, elem)
                else:
                    return self.add_right(p, elem)

    def insert(self, k, v):
        if self.is_empty():
            return self.add_root(self.Element(k, v))
        else:
            p = self.find_position(k)
            if p.key() == k:
                p.element()._value = v
                return
            else:
                elem = self.Element(k, v)
                if k < p.key():
                    return self.add_left(p, elem)
                else:
                    return self.add_right(p, elem)

    def first(self):
        if self.is_empty():
            return None
        else:
            return self._subtree_first_position(self.root())

    def last(self):
        if self.is_empty():
            return None
        else:
            return self._subtree_last_position(self.root())

    def before(self, p):
        self._validate(p)
        if self.left(p):
            return self._subtree_last_position(self.left(p))

        # Keep going up untill node becomes right of parent node
        walk = p
        while walk is not None and self.right(self.parent(walk)) is not walk:
            walk = self.parent(walk)
        return walk

    def after(self, p):
        self._validate(p)
        if self.right(p):
            return self._subtree_first_position(self.right(p))

        # Keep going up untill node becomes left of parent node
        walk = p
        while self.parent(walk) is not None and (self.right(self.parent(walk)) == walk):
            walk = self.parent(walk)
        return self.parent(walk)

    def find_min(self):
        if self.is_empty():
            return None
        p = self.first()
        return p.key(), p.value()

    def find_ge(self, k):
        if self.is_empty():
            return None
        p = self.find_position(k)
        if p.key() < k:
            p = self.after(p)
        return (p.key(), p.value()) if p is not None else None

    def __iter__(self):
        walk = self.first()
        while walk is not None:
            yield walk.key()
            walk = self.after(walk)


if __name__ == "__main__":
    bst = TreeMap()
    bst["21"] = 1
    bst["32"] = 9
    bst["24"] = 7
    bst["15"] = 0
    bst["13"] = 0
    bst["18"] = 0
    for k in bst:
        print("%s = %s" % (k, bst[k]))
    for p in bst.positions():
        print(p.key())
    print("-------")
    for p in bst.breadth_first():
        print(p.key())
