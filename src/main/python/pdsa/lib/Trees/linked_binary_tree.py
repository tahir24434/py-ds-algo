from pdsa.lib.Trees.binary_tree import BinaryTree


class LinkedBinaryTree(BinaryTree):
    class _Node:
        _slots = '_element', '_parent', '_left', '_right'

        def __init__(self, element, parent=None, left=None, right=None):
            self._element = element
            self._parent = parent
            self._left = left
            self._right = right

    class Position(BinaryTree.Position):
        def __init__(self, container, node):
            self._container = container
            self._node = node

        def element(self):
            return self._node._element

        def __eq__(self, other):
            return type(self) == type(other) and self._node is other._node

    def __init__(self):
        self._root = None
        self._size = 0

    def root(self):
        return self._make_position(self._root)

    def _validate(self, p):
        if not isinstance(p, self.Position):
            raise TypeError("Not a valid type")
        if p._container is not self:
            raise ValueError("Position is not valid")
        elif p._node._parent is p._node:
            raise ValueError("p is no longer valid")
        return p._node

    def _make_position(self, node):
        return self.Position(self, node) if node is not None else None

    def parent(self, p):
        node = self._validate(p)
        return self._make_position(node._parent)

    def left(self, p):
        node = self._validate(p)
        return self._make_position(node._left)

    def right(self, p):
        node = self._validate(p)
        return self._make_position(node._right)

    def add_left(self, p, e):
        node = self._validate(p)
        if node._left is not None:
            raise ValueError("Left position is already occupied")
        node._left = self._Node(e, node)
        self._size += 1
        return self._make_position(node._left)

    def add_right(self, p, e):
        node = self._validate(p)
        if node._right is not None:
            raise ValueError("Right position is already occupied")
        node._right = self._Node(e, node)
        self._size += 1
        return self._make_position(node._right)

    def add_root(self, e):
        if self._root is not None:
            raise ValueError("Root already exists")
        self._root = self._Node(e)
        self._size += 1
        return self._make_position(self._root)

    def _replace(self, p, e):
        node = self._validate(p)
        old = node._element
        node._element = e
        return old

    def __len__(self):
        return self._size

    def num_children(self, p):
        node = self._validate(p)
        count = 0
        if node._left is not None:
            count += 1
        if node._right is not None:
            count += 1
        return count

