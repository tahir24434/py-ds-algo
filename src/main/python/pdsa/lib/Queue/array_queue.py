class Empty(Exception):
    """Error attempting to access an element from an empty container"""
    pass


class Queue(object):
    DEFAULT_CAPACITY = 15  # Initial capacity of new queue

    def __init__(self):
        self._data = [None] * Queue.DEFAULT_CAPACITY
        self._front = 0
        self._size = 0

    def __len__(self):
        return self._size

    def _is_empty(self):
        return self._size == 0

    def resize(self, cap):
        old = self._data
        self._data = [None] * cap
        for i in range(self._size):
            self._data[i] = old[self._front]
            self._front = (self._front + 1) % len(old)
        self._front = 0

    def enqueue(self, e):
        if self._size == len(self._data):
            self.resize(2 * len(self._data))
        avail = (self._front + self._size) % len(self._data)
        self._data[avail] = e
        self._size += 1

    def dequeue(self):
        if self._is_empty():
            raise Empty("Queue is empty")
        e = self._data[self._front]
        self._data[self._front] = None  # Helps garbage collection
        self._front = (self._front + 1) % len(self._data)
        self._size -= 1
        if 0 < self._size < len(self._data) // 4:
            self.resize(len(self._data) // 2)
        return e

    def _first(self):
        if self._is_empty():
            raise Empty("Queue is empty")
        return self._data[self._front]
