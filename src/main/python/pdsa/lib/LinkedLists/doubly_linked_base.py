"""
Section 7.3 of Data Structures and algorithms in Python by Goodrich
"""


class _DoublyLinkedBase(object):
    class _Node:
        """
        Lightweight, nonpublic class for storing a singly linked node.
        """
        __slots__ = '_element', '_prev', '_next'  # streamline memory usage

        def __init__(self, element, prev, nxt):  # Initialize node fields
            self._element = element  # Reference to user element
            self._prev = prev
            self._next = nxt  # Reference to next node

    def __init__(self):
        """
        Create an empty list.
        In order to avoid some special cases when operating near boundaries of a
        doubly linked list, it helps to add special nodes at both ends of the list: a
        header node at the beginning of the list, and a trailer node at the end of the
        list. These dummy nodes are known as "sentinels".
        """
        self._header = self._Node(None, None, None)
        self._trailer = self._Node(None, None, None)
        self._header._next = self._trailer
        self._trailer._prev = self._header
        self._size = 0

    def __len__(self):
        """
        Returns number of elements in list.
        """
        return self._size

    def is_empty(self):
        """
        Returns True if list is empty.
        """
        return self._size == 0

    def _insert_between(self, e, predecessor, successor):
        """
        Add element e between two existing nodes and return new node.
        """
        newest = self._Node(e, predecessor, successor)
        predecessor._next = newest
        successor._prev = newest
        self._size += 1
        return newest

    def _delete_node(self, node):
        """
        Delete non-sentinel node from the list and return its element
        """
        if self.is_empty():
            raise Exception("node does not exist.")
        pred = node._prev
        succ = node._next
        pred._next = succ
        succ._prev = pred
        self._size -= 1
        element = node._element
        node._prev = node._next = node._element = None
        return element

    def print_ll(self):
        header = self._header._next
        while header._next is not None:
            print(header._element)
            header = header._next


if __name__ == "__main__":
    dll = _DoublyLinkedBase()
