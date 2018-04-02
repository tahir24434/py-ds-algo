"""
In MS-Paint, when we take the brush to a pixel and click, the color of the region of
that pixel is replaced with a new selected color. Following is the problem statement
to do this task.
Given a 2D screen, location of a pixel in the screen and a color, replace color of
the given pixel and all adjacent same colored pixels with the given color.

Input:
       screen[M][N] = [[1, 1, 1, 1, 1, 1, 1, 1],
                      [1, 1, 1, 1, 1, 1, 0, 0],
                      [1, 0, 0, 1, 1, 0, 1, 1],
                      [1, 2, 2, 2, 2, 0, 1, 0],
                      [1, 1, 1, 2, 2, 0, 1, 0],
                      [1, 1, 1, 2, 2, 2, 2, 0],
                      [1, 1, 1, 1, 1, 2, 1, 1],
                      [1, 1, 1, 1, 1, 2, 2, 1],
                      ];
    x = 4, y = 4, newColor = 3
The values in the given 2D screen indicate colors of the pixels.
x and y are coordinates of the brush, newColor is the color that
should replace the previous color on screen[x][y] and all surrounding
pixels with same color.

Output:
Screen should be changed to following.
       screen[M][N] = [[1, 1, 1, 1, 1, 1, 1, 1],
                      [1, 1, 1, 1, 1, 1, 0, 0],
                      [1, 0, 0, 1, 1, 0, 1, 1],
                      [1, 3, 3, 3, 3, 0, 1, 0],
                      [1, 1, 1, 3, 3, 0, 1, 0],
                      [1, 1, 1, 3, 3, 3, 3, 0],
                      [1, 1, 1, 1, 1, 3, 1, 1],
                      [1, 1, 1, 1, 1, 3, 3, 1],
                      ];
"""

row_moves = [-1, 1, 0, 0]
col_moves = [0, 0, -1, 1]


def fill(M, cell, new_fill):
    # Check that cell is valid.
    num_rows = len(M)
    num_cols = len(M[0])
    row = cell[0]
    col = cell[1]
    if row < 0 or col < 0 or row >= num_rows or col >= num_cols:
        return
    orig_val = M[row][col]
    _fill(M, row, col, orig_val, new_fill)


def _fill(M, row, col, orig_val, new_val):
    if row < 0 or col < 0 or row >= len(M) or col >= len(M[0]):
        return
    if M[row][col] != orig_val:
        return
    M[row][col] = new_val

    for k in range(4):
        r = row+row_moves[k]
        c = col+col_moves[k]
        _fill(M, r, c, orig_val, new_val)


if __name__ == "__main__":
    M = [[1, 1, 1, 1, 1, 1, 1, 1],
         [1, 1, 1, 1, 1, 1, 0, 0],
         [1, 0, 0, 1, 1, 0, 1, 1],
         [1, 3, 3, 3, 3, 0, 1, 0],
         [1, 1, 1, 3, 3, 0, 1, 0],
         [1, 1, 1, 3, 3, 3, 3, 0],
         [1, 1, 1, 1, 1, 3, 1, 1],
         [1, 1, 1, 1, 1, 3, 3, 1]]
    cell = (3, 1)
    fill(M, cell, 2)
    print(M)