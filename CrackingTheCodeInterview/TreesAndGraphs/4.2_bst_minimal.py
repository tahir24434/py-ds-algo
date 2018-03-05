"""
Given a sorted (increasing order) array with unique integer elements, write an algorithm
to create a binary search tree with minimal height.
A = [5, 7, 9, 11, 12, 13, 20, 21]
"""
class BST:
    class Node:
        def __init__(self, k, parent=None, left=None, right=None):
            self.key = k
            self.parent = parent
            self.left = left
            self.right = right

    def build_bst(self, A, p, r):
        if p < r:
            return None
        mid = (p + r) // 2
        node = self.Node(A[mid])
        node.left = self.build_bst(A, p, mid-1)
        node.right = self.build_bst(A, mid + 1, r)
        return node


if __name__ == "__main__":
    A = [5, 7, 9, 11, 12, 13, 20, 21]
    bst = BST()
    bst.build_bst(A, 0, len(A) - 1)
