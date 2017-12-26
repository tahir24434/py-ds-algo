"""
Implementation analysis:
------------------------
S.is_empty()        O(1)
S.push(e)           O(1)
S.pop(e)            O(1)
S.top(e)            O(1)
Note: The O(1) time for push and pop are amortized bounds.
push() and pop() occasionally may take O(n)-time worst case, when an operation
causes the list to resize its internal array.
"""
from nose.tools import assert_equal


class Empty(Exception):
    """Error attempting to access an element from an empty container"""
    pass


class ArrayStack(object):
    """
    LIFO stack implementation using a python list
    """
    def __init__(self):
        """
        Create an empty stack.
        """
        self._data = []

    def __len__(self):
        """
        length of stack.
        Returns
        -------
        number of element in a stack
        """
        return len(self._data)

    def is_empty(self):
        """
        Check whether stack is empty or Not?
        Returns
        -------
        Boolean value. True if stack is empty.
        """
        return self._data == []

    def push(self, e):
        """
        Push an element to the stack.
        Parameters
        ----------
        e : Any data type
        Element to push
        Returns
        -------
        """
        self._data.append(e)

    def pop(self):
        """
        Remove and return the element from the top of the stack (i.e LIFO).
        Raise empty exception if the stack is empty
        Returns
        -------
        Top element of the stack
        """
        if self.is_empty():
            raise Empty("Stack is empty")
        return self._data.pop()

    def top(self):
        """
        Return (but do NOT remove) top element of the stack. Raises 'Empty'
        exception if the stack is empty.
        Returns
        -------
        Top element of stack.
        """
        if self.is_empty():
            raise Empty("Stack is empty")
        return self._data[-1]

if __name__ == '__main__':
    stack = ArrayStack()
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
    print('Success: test_grid_path')
