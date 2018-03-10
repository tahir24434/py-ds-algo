"""
Please implement a function which returns the nth number in Fibonacci sequences with an input n.
Fibonacci sequence is defined as:
F0 = 0 and F1 = 1
"""
from nose.tools import assert_equal


def fib(n):
    nm2 = 0
    nm1 = 1
    nth_fib = 0
    for i in range(2, n):
        nth_fib = nm2 + nm1
        nm2 = nm1
        nm1 = nth_fib
    return nth_fib


if __name__ == "__main__":
    assert_equal(fib(3), 1)
    assert_equal(fib(4), 2)
    assert_equal(fib(5), 3)
    assert_equal(fib(6), 5)
    assert_equal(fib(7), 8)
    assert_equal(fib(8), 13)
    assert_equal(fib(9), 21)
    assert_equal(fib(10), 34)
    print("Success ...")
