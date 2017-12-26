from nose.tools import assert_equal
from pdsa.lib.Stacks.array_stack import ArrayStack


class Queue:
    def __init__(self):
        self.oldest = ArrayStack()
        self.newest = ArrayStack()

    def enqueue(self, e):
        self.newest.push(e)

    def dequeue(self):
        if self.oldest.is_empty():
            while not self.newest.is_empty():
                self.oldest.push(self.newest.pop())
        return self.oldest.pop()


if __name__ == "__main__":
    q = Queue()
    q.enqueue(4)
    assert_equal(q.dequeue(), 4)
    q.enqueue(2)
    q.enqueue(3)
    q.enqueue(4)
    q.enqueue(5)
    assert_equal(q.dequeue(), 2)
    assert_equal(q.dequeue(), 3)
    assert_equal(q.dequeue(), 4)
    assert_equal(q.dequeue(), 5)
    print("Success ...")
