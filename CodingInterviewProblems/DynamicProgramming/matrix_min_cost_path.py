"""
Given a cost matrix cost[][] and a position (m, n) in cost[][], write a function
that returns cost of minimum cost path to reach (m, n) from (0, 0). Each cell of the
matrix represents a cost to traverse through that cell. Total cost of a path to
reach (m, n) is sum of all the costs on that path (including both source and
destination). You can only traverse down, right and diagonally lower cells from a
given cell, i.e., from a given cell (i, j), cells (i+1, j), (i, j+1) and (i+1, j+1)
can be traversed. You may assume that all costs are positive integers.
"""
from nose.tools import assert_equal


def min_cost(cost_mat, m, n):
    if m == 0 and n == 0:
        return cost_mat[m][n]

    if m < 0 or n < 0:
        return float('inf')

    return cost_mat[m][n] + \
           min(min_cost(cost_mat, m-1, n),      # up
               min_cost(cost_mat, m, n-1),      # left
               min_cost(cost_mat, m-1, n-1))    # diagonal


if __name__ == "__main__":
    cost = [[1, 2, 3],
            [4, 8, 2],
            [1, 5, 3]]
    assert_equal(min_cost(cost, 2, 2), 8)
    print("Success ...")
