"""
Given an input stream of n integers the task is to insert integers to stream and
print the kth smallest element in the stream at each insertion.
"""
from pdsa.lib.Heaps.max_heap import MaxHeap


def kth_smallest(A, k):
    # Assumptions taken for this function.
    # 1. len(A) is greater than k.
    # 2. Stream starts after k elements. So, we can have a heap of size k beforehand.
    # Assume A as a stream of integers

    mh = MaxHeap()
    for i in range(k):
        mh.insert(A[i])

    for i in range(k, len(A)):
        if A[i] < mh.get_max().key:
            mh.extract_max()
            mh.insert(A[i])
            print("kth smallest element of stream is %s" % mh.get_max().key)


if __name__ == "__main__":
    A = [10, 20, 11, 70, 9, 7, 100, 5]
    kth_smallest(A, 3)
