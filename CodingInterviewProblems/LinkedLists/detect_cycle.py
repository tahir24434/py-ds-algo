"""
https://leetcode.com/problems/linked-list-cycle/discuss/44489/O(1)-Space-Solution
http://codingfreak.blogspot.com/2012/09/detecting-loop-in-singly-linked-list_22.html

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None
"""


def has_cycle(head):
    hare = tortoise = head
    while hare is not None and hare._next is not None:
        hare = hare._next._next
        tortoise = tortoise._next
        if hare == tortoise:
            return True
    return False
