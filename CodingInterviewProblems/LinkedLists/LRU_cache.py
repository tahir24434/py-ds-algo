"""
https://www.youtube.com/watch?v=R0GTqg3pJKg
NOTE: In video, guy is adding the latest item at last. And thus LRU item is on head.
In our implementation, we are doing it in other way around.
"""


class DoubleLinkedList:
    class _Node:
        def __init__(self, e, prev, next):
            self._element = e
            self._next = next
            self._prev = prev

    def __init__(self):
        self._head = self._Node(None, None, None)
        self._tail = self._Node(None, None, None)
        self._head._next = self._tail
        self._tail._prev = self._head
        self._size = 0

    def __len__(self):
        return self._size

    def is_empty(self):
        return self._size == 0

    def _insert_between(self, pred, succ, e):
        node = self._Node(e, pred, succ)
        pred._next = node
        succ._prev = node
        self._size += 1
        return node

    def delete_node(self, node):
        pred = node._prev
        succ = node._next
        pred._next = succ
        succ._prev = pred
        self._size -= 1
        element = node._element
        node._prev = node._next = node._element = None
        return element

    def add_first(self, e):
        return self._insert_between(self._head, self._head._next, e)

    def delete_last(self):
        self.delete_node(self._tail._prev)

    def get_last(self):
        return self._tail._prev

class LRU:
    def __init__(self, max_size):
        self.key_node_dict = dict()
        self.key_val_dll = DoubleLinkedList()
        self._size = 0
        self._max_size = max_size

    def is_full(self):
        return self._size == self._max_size

    def put(self, k, v):
        # If we are putting something which is already there. It needs to be
        # refreshed.
        # If key is in dict
        #   1. Get node
        #   2. Delete node from dll
        #   3. Add node at head with updated value.
        #   4. Add new node to dict
        # Otherwise, just follow step 3 and 4.
        if k in self.key_node_dict.keys():
            node = self.key_node_dict[k]
            self.key_val_dll.delete_node(node)
        new_node = self.key_val_dll.add_first((k, v))
        self.key_node_dict[k] = new_node

        # In case LRU is already filled, we need to delete last element from dll
        # and dict.
        if len(self.key_val_dll) > self._max_size:
            node = self.key_val_dll.get_last()
            del(self.key_node_dict[node.key])
            self.key_val_dll.delete_last()

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if key is self.key_node_dict:
            node = self.key_node_dict[key]
            res = node[1]
            # We also need to refresh stuff.
            self.key_val_dll.delete_node(node)
            new_node = self.key_val_dll.add_first((key, res))
            self.key_node_dict[key] = new_node
            return res
        return -1






