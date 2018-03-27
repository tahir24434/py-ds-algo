# TODO: This was written as part of practice. Many missing functions like has_left,
# has_right. See max_heap implementation for more comprehensive idea.

class MinHeap:
    def __init__(self):
        self._data = [0]
        self._size = 0

    def _parent(self, i):
        return i // 2

    def _left(self, i):
        return i * 2

    def _right(self, i):
        return i * 2 + 1

    def _swap(self, i, j):
        if (0 < i <= self._size) and (0 < j <= self._size):
            self._data[i], self._data[j] = self._data[j], self._data[i]

    def insert_key(self, k):
        self._data.append(float('inf'))
        self._size += 1
        self.decrease_key(self._size, k)

    def decrease_key(self, ki, new_key):
        if new_key > self._data[ki]:
            raise KeyError('New key is bigger ...')

        old_key = self._data[ki]
        self._data[ki] = new_key
        walk = ki
        # TODO: Can be simplified
        while walk > 1:
            pi = self._parent(walk)
            if self._data[pi] > self._data[walk]:
                self._swap(pi, walk)
                walk = pi
            else:
                break

    def min_heapify(self, i):
        walk = i
        while walk < self._size:
            left = self._left(walk)
            right = self._right(walk)
            smaller_child = left if self._data[left] < self._data[right] else right
            if self._data[walk] > self._data[smaller_child]:
                self._swap(walk, smaller_child)
                walk = smaller_child
            else:
                break

    def extract_min(self):
        self._swap(1, self._size)
        min_elem = self._data.pop()
        self._size -= 1
        self.min_heapify(1)
        return min_elem


if __name__ == "__main__":
    mh = MinHeap()
    mh.insert_key(5)
    mh.insert_key(6)
    mh.insert_key(9)
    print(mh.extract_min())
    mh.insert_key(1)
    print(mh.extract_min())
    mh.insert_key(0)
    print(mh.extract_min())
    print(mh._data)
    mh.insert_key(10)

