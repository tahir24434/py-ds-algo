import sys
from nose.tools import assert_equal, assert_raises
from pdsa.lib.Stacks.array_stack import ArrayStack


class Empty(Exception):
    pass


class MinStack(ArrayStack):
    def __init__(self):
        super(MinStack, self).__init__()
        self._min = ArrayStack()

    def minimum(self):
        try:
            return self._min.top()
        except Exception as e:
            return sys.maxsize

    def push(self, e):
        super(MinStack, self).push(e)
        if e < self.minimum():
            self._min.push(e)

    def pop(self):
        e = super(MinStack, self).pop()
        if e == self.minimum():
            self._min.pop()
        return e

if __name__ == "__main__":
    print('Test: Push on empty stack, non-empty stack')
    stack = MinStack()
    stack.push(5)
    assert_equal(stack.top(), 5)
    assert_equal(stack.minimum(), 5)
    stack.push(1)
    assert_equal(stack.top(), 1)
    assert_equal(stack.minimum(), 1)
    stack.push(3)
    assert_equal(stack.top(), 3)
    assert_equal(stack.minimum(), 1)
    stack.push(0)
    assert_equal(stack.top(), 0)
    assert_equal(stack.minimum(), 0)

    print('Test: Pop on non-empty stack')
    assert_equal(stack.pop(), 0)
    assert_equal(stack.minimum(), 1)
    assert_equal(stack.pop(), 3)
    assert_equal(stack.minimum(), 1)
    assert_equal(stack.pop(), 1)
    assert_equal(stack.minimum(), 5)
    assert_equal(stack.pop(), 5)
    assert_equal(stack.minimum(), sys.maxsize)

    #print('Test: Pop empty stack')
    #assert_raises(Empty, stack.pop())

    print('Success ...')
