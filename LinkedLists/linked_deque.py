from .doubly_linked_base import _DoublyLinkedBase


class LinkedDeque(_DoublyLinkedBase):
    def first(self):
        """
        Return (but do not remove) the element at the front of the deque.
        """
        if self.is_empty():
            raise Exception("Deque is empty")
        return self._header._next._element

    def last(self):
        """
        Return (but do not remove) the element at the back of the deque.
        """
        if self.is_empty():
            raise Exception("Deque is empty")
        return self._trailer._prev._element

    def _insert_first(self, e):
        """
        Add an element to the front of the deque.
        """
        return self._insert_between(e, self._header, self._header.next)

    def _insert_last(self, e):
        """
        Add an element to the back of the deque.
        """
        return self._insert_between(e, self._trailer._prev, self._trailer)

    def delete_first(self):
        """
        Remove and return the element from the front of the deque.
        Raise Empty exception if the deque is empty
        """
        if self.is_empty():
            raise Exception("Deque is empty")
        return self._delete_node(self._header._next)

    def delete_last(self):
        """
        Remove and return the element from the back of the deque.
        Raise Empty exception if the deque is empty
        """
        if self.is_empty():
            raise Exception("Deque is empty")
        return self._delete_node(self._trailer._prev)

