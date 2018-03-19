"""
Imagine a robot sitting on the upper left corner of grid with r rows and c columns.
The robot can only move in two directions, right and down, but certain cells are
"off limits" such that the robot cannot step on them.
Design an algorithm to find a path for the robot from the top left to the bottom
right.
"""
from nose.tools import assert_list_equal


def find_path(grid):
    cache = {}
    path = []
    _find_path(grid, len(grid)-1, len(grid[0])-1, path, cache)
    return path


def _find_path(grid, m, n, path, cache):
    cell = (m, n)
    if cell in cache:
        return cache[cell]

    # Off limit cell
    if grid[m][n] == 0:
        return None

    # Invalid cell
    if m < 0 or n < 0:
        return None

    # ToDo: Is it really required?
    if m == 0 and n == 0:
        path.append((m, n))
        return m, n

    cache[cell] = _find_path(grid, m-1, n, path, cache) or \
                  _find_path(grid, m, n-1, path, cache)
    if cache[cell]:
        path.append(cell)
    return cache[cell]


if __name__ == "__main__":
    max_rows = 8
    max_cols = 4
    matrix = [[1] * max_cols for _ in range(max_rows)]
    matrix[1][1] = 0
    matrix[2][2] = 0
    matrix[3][0] = 0
    matrix[4][2] = 0
    matrix[5][3] = 0
    matrix[6][1] = 0
    matrix[6][3] = 0
    matrix[7][1] = 0
    result = find_path(matrix)
    expected = [(0, 0), (1, 0), (2, 0),
                (2, 1), (3, 1), (4, 1),
                (5, 1), (5, 2), (6, 2),
                (7, 2), (7, 3)]
    assert_list_equal(result, expected)
    print("Success ...")


