"""
We demonstrate use of a singly linked list by providing a complete Python
implementation of the stack ADT (see Section 6.1). In designing such an
implementation, we need to decide whether to model the top of the stack at the
head or at the tail of the list. There is clearly a best choice here; we can
efficiently insert and delete elements in constant time only at the head.
Since all stack operations affect the top, we orient the top of the stack at
the head of our list.

Operation       Running Time
S.push(e)       O(1)
S.pop()         O(1)
S.top()         O(1)
len(S)          O(1)
S.is_empty()    O(1)
"""
from nose.tools import assert_equal


class SinglyLinkedListStack(object):
    class _Node:
        __slots__ = '_element', '_next' # streamline memory usage

        def __init__(self, element, nxt=None):   # Initialize node fields
            self._element = element         # Reference to user element
            self._next = nxt                # Reference to next node

    def __init__(self):
        self._head = None
        self._size = 0

    def __len__(self):
        return self._size

    def is_empty(self):
        return self._size == 0

    def push(self, e):
        self._head = self._Node(e, self._head)
        self._size += 1

    def pop(self):
        if self.is_empty():
            raise Exception("Stack is empty")
        element = self._head._element
        self._head = self._head._next
        self._size -= 1
        return element

    def top(self):
        if self.is_empty():
            raise Exception("Stack is empty")
        return self._head._element

if __name__ == "__main__":
    stack = SinglyLinkedListStack()
    stack.push(5)
    stack.push(7)
    assert_equal(stack.top(), 7)
    stack.push(4)
    stack.push(3)
    assert_equal(stack.pop(), 3)
    stack.push(3)
    assert_equal(stack.pop(), 3)
    stack.push(9)
    stack.push(0)
    assert_equal(stack.pop(), 0)
    assert_equal(len(stack), 4)
    print('Success ...')
