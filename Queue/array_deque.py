from nose.tools import assert_list_equal


class Empty(Exception):
    """Error attempting to access an element from an empty container"""
    pass


class ArrayDeque(object):
    DEFAULT_CAPACITY = 15  # Initial capacity of new queue

    def __init__(self):
        self._data = [None] * ArrayDeque.DEFAULT_CAPACITY
        self._size = 0
        self._front = 0

    def __len__(self):
        """
        Returns number of elements in deque.
        :return:
        """
        return self._size

    def add_first(self, e):
        """
        Add element e to the front of the deque
        :param e:
        :return:
        """
        if self._size == len(self._data):
            self._resize(2 * len(self._data))
        avail = (self._front - 1) % len(self._data)
        self._data[avail] = e
        self._size += 1
        self._front = avail

    def add_last(self, e):
        """
        Add element e to the back of the queue
        :param e:
        :return:
        """
        if self._size == len(self._data):
            self._resize(2 * len(self._data))
        avail = (self._front + self._size) % len(self._data)
        self._data[avail] = e
        self._size += 1

    def delete_first(self):
        """
        Remove and delete the first element of Deque. An error occurs if deque is empty.
        :return:
        """
        if self.is_empty():
            raise Empty("Queue is empty")
        else:
            res = self._data[self._front]
            self._data[self._front] = None
            self._front = (self._front + 1) % len(self._data)
            self._size -= 1

            # If we're down to smaller than a quarter occupied,
            # cut array size in half.
            if self._size < len(self._data) // 4:
                self._resize(len(self._data) // 2)

            return res

    def delete_last(self):
        """
        Remove and return the last element of Deque. An error occurs if deque is empty.
        :return:
        """
        if self.is_empty():
            raise Empty("Queue is empty")
        else:
            last_idx = (self._front + self._size) % len(self._data)
            res = self._data[last_idx]
            self._data[last_idx] = None
            self._size -= 1

            # If we're down to smaller than a quarter occupied,
            # cut array size in half.
            if self._size < len(self._data) // 4:
                self._resize(len(self._data) // 2)
            return res

    def first(self):
        """
        Return (but do not remove) the first element of Deque. An error occurs if deque is
        empty.
        :return:
        """
        if self.is_empty():
            raise Empty("Queue is empty")
        else:
            return self._data[self._front]

    def last(self):
        """
        Return (but do not remove) the last element of Deque. An error occurs if deque is
        empty.
        :return:
        """
        if self.is_empty():
            raise Empty("Queue is empty")
        else:
            last_idx = (self._front + self._size) % len(self._data)
            return self._data[last_idx]

    def _resize(self, new_cap):
        """
        Resize the data array. Assumption is that new capacity will always be greater than
        current size of the deque.
        :param new_cap: int
            New capacity of array.
        :return:
        """
        new = [None] * new_cap
        walk = self._front
        for i in range(self._size):
            new[i] = self._data[walk]
            walk = (walk + 1) % len(self._data)
        self._data = new
        self._front = 0

    def is_empty(self):
        return self._size == 0