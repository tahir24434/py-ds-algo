
class MinStack:
    def __init__(self):
        self._data = []
        self._size = 0
        self._min_data = [float('inf')]
        self._min_size = 0

    def __len__(self):
        return self._size

    def is_empty(self):
        return self._size == 0

    def top(self):
        if self._size == 0:
            raise KeyError("Empty Stack")
        return self._data[self._size-1]

    def push(self, element):
        self._data.append(element)
        self._size += 1
        if element < self._min_data[self._min_size]:
            self._min_data.append(element)
            self._min_size += 1

    def pop(self):
        if self._size == 0:
            raise KeyError("Empty Stack")
        e = self._data.pop()
        self._size -= 1
        if e == self._min_data[self._min_size]:
            self._min_data.pop()
            self._min_size -= 1
        return e

    def get_min(self):
        return self._min_data[self._min_size]

if __name__ == "__main__":

