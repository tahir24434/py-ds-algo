"""
Binary Heap Data Structure is an array object that we can view as a nearly complete
binary tree. The tree is completely filled on all levels except possibly the lowest,
which is filled from the left up to a point.
In a max-heap, the max-heap property is that for every node i other than the root,
 A[Parent(i)] >= A[i]
that is, the value of node is at most the value of its parents. Thus the largest
element in a max-heap is stored at the root, and the subtree rooted at a node contains
values no larger than that contained at the node itself.
"""
from nose.tools import assert_equal


class HeapItem(object):
    def __init__(self, key, value=None):
        self.key = key
        self.value = value

    def __lt__(self, other):
        return self.key < other.key

    def __gt__(self, other):
        return self.key > other.key


class MaxHeap(object):
    # Since the entire binary heap can be represented by a single list, all
    # the constructor will do is initialize the
    # list and an attribute currentSize to keep track of the current size of
    # the heap
    def __init__(self):
        # notice that an empty binary heap has a single zero as the first
        # element of heapList and that this zero is not used, but is there
        # so that simple integer division can be used in later methods.
        self._data = [0]
        self._size = 0

    @staticmethod
    def _parent(i):
        return i//2

    @staticmethod
    def _left(i):
        return 2*i

    @staticmethod
    def _right(i):
        return 2 * i + 1

    def _has_left(self, i):
        return self._left(i) <= self._size   # index beyond end of list?

    def _has_right(self, i):
        return self._right(i) <= self._size  # index beyond end of list?

    def _swap(self, i, j):
        self._data[i], self._data[j] = self._data[j], self._data[i]

    def __len__(self):
        return self._size

    def _max_heapify(self, i):
        """
        max_heapify assumes that the binary tree rooted at left(i) and right(i)
        are max-heaps, but that A[i] might be smaller than its children,
        thus violating the max-heap property.
        max_heapify() lets the value at _data[i] 'float down' in the
        max-heap so that the subtree rooted at index i obeys the max-heap
        property.
        It runs in O(lgn) time.
        Parameters
        ----------
        i : int
            index of the element which is violating the max-heap property.
        Returns
        -------
        """
        if self._has_left(i):
            left = MaxHeap._left(i)
            bigger_child = left
            if self._has_right(i):
                right = MaxHeap._right(i)
                if self._data[right] > self._data[left]:
                    bigger_child = right

            if self._data[bigger_child] > self._data[i]:
                # Exchange A[i] with A[largest_val_idx]
                self._swap(i, bigger_child)
                # Call max_heapify
                self._max_heapify(bigger_child)

    def build_heap_from_list(self, item_lst):
        """
        We can use the procedure max-heapify in a bottom-up manner to convert
        an array A[1 .. n], where n=A.length, into a max-heap.
        Elements in the subarray A[(floor(n/2)+1) .. n] are all leaves of the
        tree, and so each is a 1-element heap to
        begin with. The procedure Build-max-heap goes through the remaining
        nodes of the tree and run max-heapify on each one.
        Returns
        -------
        """
        self._size = len(item_lst)
        self._data = [HeapItem(0, 0)] + item_lst[:]
        for i in range(self._size // 2, 0, -1):
            self._max_heapify(i)

    def increase_key(self, i, key):
        """
        Parameters
        ----------
        i : int
            index i identifies the priority queue element whose key we wish to
            increase.
        key
            new key with whom existing key will be replaced.
        Returns
        -------
        """
        if key < self._data[i].key:
            print ("new key is smaller than the current key")
            return

        self._data[i].key = key
        while i > 1 and self._data[MaxHeap._parent(i)] < self._data[i]:
            # exchange items at i and parent
            self._swap(i, MaxHeap._parent(i))
            i = MaxHeap._parent(i)

    def insert(self, key, value=None):
        """
        Insert takes as an input the key of the new element to be inserted into
        max-heap.
        """
        self._size += 1
        self._data.append(HeapItem(float("-inf"), value))
        self.increase_key(self._size, key)

    def extract_max(self):
        """
        Extract the maximum element of heap. It takes O(lgn) time
        """
        if self._size == 0:
            raise Exception("Empty heap")
        # Root item is max.
        max_item = self._data[1]
        # To restore root, place last item as root
        self._data[1] = self._data.pop()
        self._size -= 1
        # restore heap order property by moving root to appropriate place.
        # Swap the root with its smallest child less than the root. Keep doing
        # this unless root becomes smaller than both of his children.
        self._max_heapify(1)
        return max_item

    def get_max(self):
        """
        Get maximum element of heap in O(1) time.
        """
        if self._size == 0:
            raise Exception("Empty heap")
        return self._data[1]

    def sort(self, item_lst):
        """
        Sorts the input array.
        """
        self.build_heap_from_list(item_lst)
        while self._size > 1:
            self._data[1], self._data[self._size] = \
                self._data[self._size], self._data[1]
            self._size -= 1
            self._max_heapify(1)


if __name__ == '__main__':
    key_val = {4: "", 1: "", 3: "", 2: "", 16: "", 9: "", 10: "", 14: "", 8: "", 7: ""}
    item_lst = []
    for key, val in key_val.items():
        item_lst.append(HeapItem(key, val))
    mh = MaxHeap()
    mh.sort(item_lst)
    sorted_list = []
    for item in mh._data:
        sorted_list.append(item.key)
    assert_equal(sorted_list, [0, 1, 2, 3, 4, 7, 8, 9, 10, 14, 16])

    # Test priority queue
    key_val = {4: "", 1: "", 3: "", 2: "", 16: "", 9: "", 10: "", 14: "", 8: "", 7: ""}
    item_lst = []
    for key, val in key_val.items():
        item_lst.append(HeapItem(key, val))
    mh = MaxHeap()
    mh.build_heap_from_list(item_lst)
    mh.insert(5)
    assert_equal(mh.get_max().key, 16)
    assert_equal(mh.extract_max().key, 16)
    assert_equal(mh.extract_max().key, 14)
    mh.insert(25)
    assert_equal(mh.extract_max().key, 25)

    print("SUCCESS ...")
