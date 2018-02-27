"""
Sorting in linear time
Counting sort assumes that each of the n input elements is an integer in the range
0 to k, for some integer k.
In the code for counting sort, we assume that the input is any array A[1...n], and thus
A.length=n. We require two other arrays: the array B[1...n] holds the sorted output, and
the array C[0...k] provides temporary working storage.
"""


def counting_sort(A, max_element):
    count = [0] * (max_element + 1)
    output = [0] * len(A)

    # Count number of individual elements
    # count[i] will contain the number of elements equal to i
    for e in A:
        count[e] += 1

    # Count number of elements less than equal to i
    for i in range(1, len(count)):
        count[i] += count[i - 1]

    # A: 4, 1, 3, 1, 0
    # count: 1, 2, 0, 1, 1
    # count: 1, 3, 3, 4, 5. We have 1 element which is less than equal to 0, 3 elements which are less than equal to 1.
    for i in range(len(A)):
        # There are count[element] items which are less than equal to element. So, element should go at index
        # "count[element-1]".
        # So, in-short, count is becoming index of output array for element.
        output[count[A[i]]-1] = A[i]
        count[A[i]] -= 1

    print (output)
