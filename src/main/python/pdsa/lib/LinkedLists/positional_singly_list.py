from nose.tools import assert_equal, assert_true, assert_false


class SinglyLinkedList:
    class _Node:
        def __init__(self, e, next):
            self._element = e
            self._next = next

    class Position:
        def __init__(self, node, container):
            self._node = node
            self._container = container

        def element(self):
            return self._node._element

        def __eq__(self, other):
            return type(other) is type(self) and self._node is other._node

    def __init__(self):
        self._header = self._Node(None, None)
        self._trailer = self._Node(None, None)
        self._header._next = self._trailer
        self._size = 0

    def _make_position(self, node):
        if node is self._header or node is self._trailer:
            return None
        else:
            return self.Position(node, self)

    def _validate(self, p):
        if not isinstance(p, self.Position):
            raise TypeError("Position is not of Type p")
        if p._container is not self:
            raise ValueError("Position does not belong to this container")
        if p._node._next is None:
            raise ValueError("position is not valid anymore")
        return p._node

    def __len__(self):
        return self._size

    def is_empty(self):
        return self._size == 0

    def add_first(self, e):
        """
        Add element at front of the list.
        """
        node = self._Node(e, self._header._next)
        self._header._next = node
        self._size += 1
        return self._make_position(node)

    def add_before(self, p, e):
        """
        Add element at front of the list.
        """
        node = self._validate(p)
        elem_node = self._Node(e, node)
        self._header._next = elem_node
        self._size += 1
        return self._make_position(elem_node)

    def first(self):
        return self._make_position(self._header._next)

    def after(self, p):
        node = self._validate(p)
        return self._make_position(node._next)

    def delete(self, pred_p, p):
        node = self._validate(p)
        if pred_p is None:
            pred = self._header
        else:
            pred = self._validate(pred_p)
        element = node._element
        pred._next = node._next
        node._next = node._element = None
        self._size -= 1
        return element

    def remove_first(self):
        try:
            pred_p = self._make_position(self._header)
            p = self._make_position(self._header._next)
            return self.delete(pred_p, p)
        except Exception as e:
            print("can not remove first element. Maybe it does not exist")
            print(e)

if __name__ == "__main__":
    sl = SinglyLinkedList()
    sl.remove_first()
    sl.add_first(5)
    assert_equal(sl.remove_first(), 5)
    sl.add_first(7)
    sl.add_first(3)
    assert_equal(len(sl), 2)
    assert_equal(sl.remove_first(), 3)
    assert_equal(len(sl), 1)
    assert_false(sl.is_empty())
    assert_equal(sl.remove_first(), 7)
    assert_true(sl.is_empty())
    print("Success ...")


