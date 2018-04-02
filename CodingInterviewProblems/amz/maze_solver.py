"""
Solve a maze. A matrix of binary (1/0) represents a maze. Write a function to find a
path from a given point(source) to destination pt. Make it
modular/readable/maintainable as much as u can.

1 S 1 1 1
0 0 1 0 1
1 0 1 0 1
0 1 D 1 1

Consider 0 as a wall.
"""


def find_start(M):
    rows = len(M)
    cols = len(M[0])
    for row in range(rows):
        for col in range(cols):
            if M[row][col] == 'S':
                return row, col
    return None


def maze_walk(M, row, col, walk):
    if row < 0 or col < 0 or row >= len(M) or col >= len(M[0]):
        return ""

    if M[row][col] == 0:
        return ""




