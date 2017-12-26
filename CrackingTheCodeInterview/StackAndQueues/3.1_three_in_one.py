from nose.tools import assert_equal


class Empty(Exception):
    pass


class ThreeStacks:
    MAX_SIZE = 10
    def __init__(self):
        self._data = [None] * (self.MAX_SIZE * 3)
        self.stack_size = {0: 0, 1: 0, 2: 0}

    def top_index(self, stack_num):
        """
        stack1:
        :param stack_num:
        :return:
        """
        # 0-10, 10-20, 20-30
        return stack_num * self.MAX_SIZE

    def push(self, stack_num, e):
        if self.stack_size[stack_num] == self.MAX_SIZE:
            raise Exception("Stack is full")
        index = stack_num * self.MAX_SIZE + self.stack_size[stack_num]
        self.stack_size[stack_num] += 1
        self._data[index] = e

    def is_empty(self, stack_num):
        return self.stack_size[stack_num] == 0

    def pop(self, stack_num):
        if self.is_empty(stack_num):
            raise Empty("Stock is empty")
        index = stack_num * self.MAX_SIZE + self.stack_size[stack_num] - 1
        self.stack_size[stack_num] -= 1
        element = self._data[index]
        self._data[index] = None
        return element

if __name__ == "__main__":
    ts = ThreeStacks()
    ts.push(0, 4)
    ts.push(1, 6)
    ts.push(2, 7)
    assert_equal(ts.pop(0), 4)
    assert_equal(ts.pop(1), 6)
    assert_equal(ts.pop(2), 7)
    ts.push(0, 7)
    ts.push(0, 8)
    ts.push(1, 9)
    ts.push(1, 6)
    ts.push(2, 7)
    ts.push(2, 11)
    assert_equal(ts.pop(0), 8)
    assert_equal(ts.pop(1), 6)
    assert_equal(ts.pop(2), 11)
    print("Success ...")
