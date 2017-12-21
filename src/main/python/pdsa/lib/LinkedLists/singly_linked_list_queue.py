"""
we can use a singly linked list to implement the queue ADT while supporting
worst-case O(1)-time for all operations. Because we need to perform
operations on both ends of the queue, we will explicitly maintain both a
head reference and a tail reference as instance variables for each queue.
The natural orientation for a queue is to align the front of the queue with
the head of the list, and the back of the queue with the tail of the list,
because we must be able to enqueue elements at the back, and dequeue them
from the front. (Recall that we are unable to efficiently remove elements
from the tail of a singly linked list. see singly_linked_list remove_last().)

Analysis:
---------
the LinkedQueue is similar to the LinkedStack in that all operations run in
worst-case constant time, and the space usage is linear in the current
number of elements.

Operation       Running Time
S.push(e)       O(1)
S.pop()         O(1)
S.top()         O(1)
len(S)          O(1)
S.is_empty()    O(1)
"""
from nose.tools import assert_equal


class SinglyLinkedListQueue(object):
    """
    FIFO queue implementation using a singly linked list for storage.
    """
    class _Node:
        """
        Lightweight, nonpublic class for storing a singly linked node.
        """
        __slots__ = '_element', '_next'  # streamline memory usage

        def __init__(self, element, nxt=None):  # Initialize node fields
            self._element = element  # Reference to user element
            self._next = nxt  # Reference to next node

    def __init__(self):
        """
        Create an empty queue.
        """
        self._head = None
        self._tail = None
        self._size = 0

    def is_empty(self):
        """
        Returns True if the queue is empty.
        """
        return self._size == 0

    def enqueue(self, e):
        """
        Add element to the back of the queue.
        """
        newest = self._Node(e)  # New tail node
        if self.is_empty():     # Special case. Previously empty.
            self._head = self._tail = newest
        else:
            self._tail._next = newest
            self._tail = newest  # Updater reference to tail node.
        self._size += 1

    def deque(self):
        """
        Remove and return the first element of the queue (i.e., FIFO).
        """
        if self.is_empty():
            raise Exception("Empty queue")
        element = self._head._element
        self._head = self._head._next
        self._size -= 1
        if self.is_empty():     # special case as queue is empty
            self._tail = None   # removed head had been the tail
        return element

    def first(self):
        """
        Return (but do not remove) the element at the front of the queue
        """
        if self.is_empty():
            raise Exception("Empty queue")
        return self._head._element  # front aligned with head of list


if __name__ == "__main__":
    q = SinglyLinkedListQueue()
    q.enqueue(1)
    q.enqueue(2)
    assert_equal(q.first(), 1)
    q.enqueue(3)
    assert_equal(q.deque(), 1)
    assert_equal(q.deque(), 2)
    q.enqueue(4)
    assert_equal(q.deque(), 3)
    print("Success ...")
