"""
Consider a matrix with  rows and  columns, where each cell contains either 0 or a 1
and any cell containing a 1 is called a filled cell. Two cells are said to be
connected if they are adjacent to each other horizontally, vertically, or diagonally;
in other words, cell  is connected to cells , , , , , , , and , provided that the
location exists in the matrix for that .

If one or more filled cells are also connected, they form a region. Note that each
cell in a region is connected to at least one other cell in the region but is not
necessarily directly connected to all the other cells in the region.

Task
Given an  matrix, find and print the number of cells in the largest region in the
matrix. Note that there may be more than one region in the matrix.

https://www.hackerrank.com/challenges/ctci-connected-cell-in-a-grid/problem
"""


def get_region_size(A, row, col):
    if row < 0 or row >= len(A) or col < 0 or col >= len(A[0]):
        return 0
    if A[row][col] == 0:
        return 0

    A[row][col] = 0
    size = 1
    for i in range(row - 1, row + 2):
        for j in range(col - 1, col + 2):
            size += get_region_size(A, i, j)
    return size


def largest_region(A):
    num_rows = len(A)
    num_cols = len(A[0])

    max_region_size = 0
    for row in range(num_rows):
        for col in range(num_cols):
            if A[row][col] == 1:
                max_region_size = max(max_region_size, get_region_size(A, row, col))
    return max_region_size


if __name__ == "__main__":
    A = [[1, 0, 0, 0],
         [1, 1, 0, 0],
         [1, 0, 0, 0],
         [1, 1, 0, 1],
         [0, 0, 0, 1]]
    print(largest_region(A))
