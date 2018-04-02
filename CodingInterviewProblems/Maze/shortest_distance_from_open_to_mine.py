"""
Given a maze in the form of a rectangular matrix, filled with either O, X or M,
where O represents an open cell, X represents a blocked cell and M represents
landmines in the maze. We need to find shortest distance of every open cell in the
maze from its nearest mine.

We're only allowed to travel in either of the four directions and diagonal moves
are not allowed. We can assume that cells with mine have distance 0. Also,
blocked cells and unreachable cells have distance -1.
"""
from pdsa.lib.Queue.array_queue import Queue


# Below array details all 4 possible movements from a cell.
row = [-1, 1, 0, 0]
col = [0, 0, -1, 1]


def find_open_cells(M):
    open_cells = []
    for row in range(len(M)):
        for col in range(len(M[0])):
            if M[row][col] == "O":
                open_cells.append((row, col))
    return open_cells


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
    if c_row < 0 or c_col < 0 or c_row >= num_rows or c_col >= num_cols or \
            M[c_row][c_col] == "X":
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
                if M[c_row][c_col] == "M":
                    return (c_row, c_col)


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


def find_shortest_path(M, open_cells):
    open_to_mine = {}
    for open_cell in open_cells:
        discovered = {open_cell: None}
        mine_cell = BFS(M, open_cell, discovered)
        open_to_mine[open_cell] = (mine_cell, discovered)
        # print(open_cell, mine_cell, discovered)
    return open_to_mine


if __name__ == "__main__":
    M = [['O', 'M', 'O', 'O', 'X'],
        ['O', 'X', 'X', 'O', 'M'],
        ['O', 'O', 'O', 'O', 'O'],
        ['O', 'X', 'X', 'X', 'O'],
        ['O', 'O', 'M', 'O', 'O'],
        ['O', 'X', 'X', 'M', 'O']]
    open_cells = find_open_cells(M)
    open_to_mine = find_shortest_path(M, open_cells)
    for open_cell in open_cells:
        mine_cell = open_to_mine[open_cell][0]
        discovered = open_to_mine[open_cell][1]
        print(construct_path(open_cell, mine_cell, discovered))
