"""
Write a program to sort an array of 0's,1's and 2's in ascending order.
input:  0 2 1 2 0
output: 0 0 1 2 2
"""


def sort_012_array(A):
    count = [0, 0, 0]
    for item in A:
        count[item] += 1

    j = 0
    for c in range(len(count)):
        for i in range(count[c]):
            A[j] = c
            j += 1


if __name__ == "__main__":
    A = [0, 2, 1, 2, 0]
    sort_012_array(A)
    print(A)
