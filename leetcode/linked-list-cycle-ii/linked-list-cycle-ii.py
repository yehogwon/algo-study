# solved
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        visits = set()
        node = head
        while node is not None: 
            if node in visits: 
                return node
            visits.add(node)
            node = node.next
        return None
