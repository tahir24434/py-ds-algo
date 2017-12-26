from pdsa.lib.Stacks.array_stack import ArrayStack
from nose.tools import assert_equal


class SetStacks():
    MAX_CAP = 3

    def __init__(self):
        s = ArrayStack()
        self.sos = {0: s}
        self.csi = 0        # Current Stack index

    def push(self, e):
        if len(self.sos[self.csi]) == self.MAX_CAP:
            s = ArrayStack()
            self.csi += 1
            self.sos[self.csi] = s
        self.sos[self.csi].push(e)

    def pop(self):
        e = self.sos[self.csi].pop()
        if len(self.sos[self.csi]) == 0:
            if self.csi != 0:
                self.csi -= 1
        return e

    def popat(self, idx):
        return self.sos[idx].pop()



if __name__ == "__main__":
    sos = SetStacks()
    sos.push(9)
    sos.push(8)
    sos.push(7)
    sos.push(6)
    sos.push(5)
    sos.push(4)
    sos.push(3)
    sos.push(2)
    sos.push(1)
    assert_equal(sos.pop(), 1)
    assert_equal(sos.pop(), 2)
    assert_equal(sos.pop(), 3)
    assert_equal(sos.pop(), 4)
    assert_equal(sos.pop(), 5)
    assert_equal(sos.pop(), 6)
    assert_equal(sos.pop(), 7)
    assert_equal(sos.pop(), 8)
    assert_equal(sos.pop(), 9)

    sos.push(15)
    sos.push(14)
    sos.push(13)
    sos.push(12)
    sos.push(11)
    sos.push(10)
    assert_equal(sos.popat(1), 10)
    print("Success ...")
