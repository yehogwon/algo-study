# solved
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None or head.next is None or head.next.next is None: 
            return None
        tortoise, hare = head.next, head.next.next
        while True: # O(n)
            if hare.next is None or hare.next.next is None: # there is no cycle
                return None
            if tortoise == hare: 
                break
            tortoise = tortoise.next
            hare = hare.next.next
        tortoise = head
        while True: # O(n)
            if tortoise == hare: 
                return tortoise
            tortoise = tortoise.next
            hare = hare.next
