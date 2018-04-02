"""

1 is allowed. 0 is NOT allowed.
"""
from pdsa.lib.Queue.array_queue import Queue


# Below array details all 4 possible movements from a cell.
row = [-1, 1, 0, 0]
col = [0, 0, -1, 1]


def is_valid(M, c):
    """

    :param c: Tuple
        cell coordinates
    :return:
    """
    num_rows = len(M)
    num_cols = len(M[0])
    c_row = c[0]
    c_col = c[1]
    if c_row < 0 or c_col < 0 or c_row >= num_rows or c_col >= num_cols or M[c_row][c_col] == 0:
        return False
    return True


def BFS(M, s, discovered):
    """

    :param M: list
        2D Maze Matrix
    :param s: tuple
        Coordinates of Source cell
    :param discovered: dictionary
        Dictionary holding so far discovered cells.
    :return:
    """
    q = Queue()
    q.enqueue(s)
    while not q._is_empty():
        cell = q.dequeue()
        # Check for all possible movements from current cell and enqueue each
        # valid movement.
        c_row = cell[0]
        c_col = cell[1]
        for k in range(4):
            cell_to_move = (c_row + row[k], c_col+col[k])
            if is_valid(M, cell_to_move) and cell_to_move not in discovered:
                discovered[cell_to_move] = cell
                q.enqueue(cell_to_move)


def construct_path(u, v, discovered):
    path = []
    if v in discovered:
        path.append(v)
        walk = v
        while walk is not u:
            parent = discovered[walk]
            path.append(parent)
            walk = parent
        path.reverse()
    return path


if __name__ == "__main__":
    M = [[1, 1, 1, 1, 1, 0, 0, 1, 1, 1],
        [0, 1, 1, 1, 1, 1, 0, 1, 0, 1],
        [0, 0, 1, 0, 1, 1, 1, 0, 0, 1],
        [1, 0, 1, 1, 1, 0, 1, 1, 0, 1],
        [0, 0, 0, 1, 0, 0, 0, 1, 0, 1],
        [1, 0, 1, 1, 1, 0, 0, 1, 1, 0],
        [0, 0, 0, 0, 1, 0, 0, 1, 0, 1],
        [0, 1, 1, 1, 1, 1, 1, 1, 0, 0],
        [1, 1, 1, 1, 1, 0, 0, 1, 1, 1],
        [0, 0, 1, 0, 0, 1, 1, 0, 0, 1]]

    s = (0, 0)
    discovered = {s: None}
    BFS(M, s, discovered)
    print(construct_path(s, (7, 5), discovered))
