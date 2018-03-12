"""
Find the contiguous subarray within an array (containing at least one number) which
has the largest sum.

For example, given the array [-2,1,-3,4,-1,2,1,-5,4],
the contiguous subarray [4,-1,2,1] has the largest sum = 6.

https://www.quora.com/Why-does-Kadanes-algorithm-work-Why-is-it-an-example-of-dynamic-programming
"""


def max_subarray(A):
    max_ending_here = max_so_far = 0
    for x in A:
        max_ending_here = max(0, max_ending_here + x)
        max_so_far = max(max_so_far, max_ending_here)
    return max_so_far

