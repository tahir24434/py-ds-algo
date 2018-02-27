from pdsa.lib.Trees.tree_map import TreeMap
from pdsa.lib.LinkedLists.singly_linked_list_queue import SinglyLinkedListQueue


def list_of_depths(bst):
    if not bst.is_empty():
        prev_level = SinglyLinkedListQueue()
        prev_level.enqueue(bst.root())
        lod = []
        while True:
            curr_level = SinglyLinkedListQueue()
            l = []
            while not prev_level.is_empty():
                p = prev_level.deque()
                l.append(p)
                for c in bst.children(p):
                    curr_level.enqueue(c)
            lod.append(l)
            prev_level = curr_level
            if curr_level.is_empty():
                break
        return lod

if __name__ == "__main__":
    bst = TreeMap()
    bst["21"] = 1
    bst["32"] = 9
    bst["24"] = 7
    bst["15"] = 0
    bst["13"] = 0
    bst["18"] = 0
    for level in list_of_depths(bst):
        for p in level:
            print(p.key())
        print("-----")
