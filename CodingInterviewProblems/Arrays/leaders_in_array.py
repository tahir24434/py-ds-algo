"""
Write a program to print all the LEADERS in the array. An element is leader if it is
greater than all the elements to its right side. The rightmost element is always a
leader.
"""


def leader(A):
    max = float('-inf')
    leaders = []
    for i in range(len(A) - 1, 0, -1):
        if A[i] > max:
            leaders.append(A[i])
            max = A[i]
    return leaders


if __name__ == "__main__":
    A = [3, 16, 15, 2, 9]
    print(leader(A))
    A = [16, 17, 4, 3, 5, 2]
    print(leader(A))
