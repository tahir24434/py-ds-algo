"""
An important task when processing arithmetic expressions is to make sure their delimiting
symbols match up correctly. Write code to verify the correctly matched delimiters.
"""
from array_stack import ArrayStack
from nose.tools import assert_true, assert_false


def is_matched_delimiters(expr):
    sym_stack = ArrayStack()
    lefty = "[{("
    righty = "]})"
    for c in expr:
        if c in lefty:
            sym_stack.push(c)
        elif c in righty:
            if sym_stack.is_empty():
                return False
            e = sym_stack.pop()
            if lefty.index(e) != righty.index(c):
                return False
    return sym_stack.is_empty()

if __name__ == "__main__":
    ex = "[(5+3) * {(4 - 3) / (5 + 1)}]"
    assert_true(is_matched_delimiters(ex))
    ex = "[(5+3) * {(4 - 3) / (5 + 1]}]"
    assert_false(is_matched_delimiters(ex))
    ex = "[(5+3) * {(4 - 3) / (5 + 1)}"
    assert_false(is_matched_delimiters(ex))
    print("Success ...")
