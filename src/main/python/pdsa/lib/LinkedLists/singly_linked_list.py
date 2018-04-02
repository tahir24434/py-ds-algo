"""
Read page 229 of Cormen

A linked list is a data structure in which the objects are arranged in a linear
order. Unlike an array, however, in which the linear order is determined by
the array indices, the order in a linked list is determined by a pointer in
each object. Linked lists provide a simple, flexible representation for
dynamic sets, supporting (though not necessarily efficiently) all the
operations search(), insert(), delete(), minimum(), maximum(), successor(),
predecessor().
A list may have one of several forms. It may be either singly linked or doubly
linked, it may be sorted or not, and it may be circular or not. If a list is
singly linked, we omit the pre pointer in each element. If a list is sorted,
the linear order of the list corresponds to the linear order of keys stored
in elements of the list; the minimum element is then the head of the list,
and the maximum element is the tail. If the list is unsorted, the elements
can appear in any order. In a circular list, the pre pointer of the head of
the list points to the tail, and the next pointer of the tail of the list
points to the head. We can think of a circular list as a ring of elements.
"""


class SinglyLinkedList(object):
    class _Node:
        __slots__ = '_element', '_next'  # streamline memory usage

        def __init__(self, element, nxt=None):   # Initialize node fields
            self._element = element              # Reference to user element
            self._next = nxt                     # Reference to next node

    def __init__(self):
        self._head = None
        self._tail = None
        self._size = 0

    def __len__(self):
        return self._size

    def is_empty(self):
        return self._size == 0

    def first(self):
        return self._head

    def last(self):
        return self._tail

    def add_first(self, e):
        """
        An important property of a linked list is that it does not have a
        predetermined fixed size; it uses space proportionally to its
        current number of elements. When using a singly linked list, we can
        easily insert an element at the head of the list
        """
        newest = self._Node(e, self._head)
        if self.is_empty():
            self._tail = newest
        self._head = newest
        self._size += 1
        return newest

    def add_last(self, e):
        """
        We can also easily insert an element at the tail of the list, provided
        we keep a reference to the tail node.
        """
        if self.is_empty():
            return self.add_first(e)
        newest = self._Node(e)
        self._tail._next = newest
        self._tail = newest
        self._size += 1
        return newest

    def remove_first(self):
        """
        Removing an element from the head of a singly linked list is
        essentially the reverse operation of inserting a new element at the
        head
        """
        if self.is_empty():
            return None
        element = self._head
        self._head = self._head._next
        self._size -= 1
        if self.is_empty():  # if there was only one element
            self._tail = None
        return element

    def remove_last(self):
        """
        Unfortunately, we cannot easily delete the last node of a singly
        linked list. Even if we maintain a tail reference directly to the
        last node of the list, we must be able to access the node before the
        last node in order to remove the last node. But we cannot reach the
        node before the tail by following next links from the tail. The only
        way to access this node is to start from the head of the list and
        search all the way through the list. But such a sequence of
        link-hopping operations could take a long time. If we want to
        support such an operation efficiently, we will need to make our list
        doubly linked.
        """
        pass
