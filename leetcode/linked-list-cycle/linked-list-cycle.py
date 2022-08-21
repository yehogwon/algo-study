# solved
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        visits = []
        node = head
        while node is not None: 
            if node in visits: 
                return True
            visits.append(node)
            node = node.next
        return False
