"""
Reverse a singly linked list.
"""

def reverse_sll(sll):
    prev = None
    curr = sll._head
    while curr is not None:
        next = curr._next
        curr._next = prev
        prev = curr
        curr = next