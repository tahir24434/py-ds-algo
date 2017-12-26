from .doubly_linked_base import _DoublyLinkedBase


class DoublyLinkedList(_DoublyLinkedBase):
    class Position:
        def __init__(self, node, container):
            self._node = node
            self._container = container

        def element(self):
            return self._node._element

        def __eq__(self, other):
            return isinstance(other, self) and self._node is other._node

        def __ne__(self, other):
            return not (self == other)

    def _validate(self, p):
        if not isinstance(p, self.Position):
            raise TypeError("position is not of type Position")
        if p._container is not self:
            raise ValueError("position does not belong to this container")
        if p._node._next is None:
            raise ValueError("position is not valid anymore")
        return p._node

    def _make_position(self, node):
        if node is self._header or node is self._trailer:
            return None
        else:
            return self.Position(node, self)

    def first(self):
        """
        Return position of first element.
        """
        return self._make_position(self._header._next)

    def last(self):
        """
        Return position of last element or None if empty.
        """
        return self._make_position(self._trailer._prev)

    def before(self, p):
        node = self._validate(p)
        return self._make_position(node._prev)

    def after(self, p):
        """
        Return position after position p (or None if p is last).
        """
        node = self._validate(p)
        return self._make_position(node._next)

    def __iter__(self):
        walk = self.first()
        while walk is not None:
            yield walk.element()
            walk = self.after(walk)

    # ------------------------------ mutators ----------------------------
    def _insert_between(self, e, pred, succ):
        """"
        Insert elemnt at middle of two positions
        """
        node = self._Node(e, pred, succ)
        pred._next = node
        succ._prev = node
        self._size += 1
        return self._make_position(node)

    def add_first(self, e):
        """
        Add element at head of list.
        """
        return self._insert_between(e, self._header, self._header._next)

    def add_last(self, e):
        """
        Add element at end of list.
        """
        return self._insert_between(e, self._trailer._prev, self._trailer)

    def add_before(self, e, p):
        node = self._validate(p)
        return self._insert_between(e, node._prev, node)

    def add_after(self, e, p):
        node = self._validate(p)
        return self._insert_between(e, node, node._next)

    def delete(self, p):
        node = self._validate(p)
        element = node._element
        node._prev._next = node._next
        node._next._prev = node._prev
        node._next = node._prev = node._element = None
        self._size -= 1
        return element

    def remove_first(self):
        """
        Remove and return first element of list.
        """
        p = self._make_position(self._header._next)
        return self.delete(p)

    def remove_last(self):
        """
        Remove and return last element of list or None if it is empty.
        """
        p = self._make_position(self._trailer._prev)
        return self.delete(p)
