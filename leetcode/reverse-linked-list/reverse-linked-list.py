# solved
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def append(parent, node): 
            if parent.next is not None: 
                append(parent.next, node)
            else: 
                parent.next = node
        def reverse(node): 
            if node is None: 
                return None
            if node.next is None: 
                return node
            else: 
                _rev = reverse(node.next)
                append(_rev, ListNode(node.val))
                return _rev
        return reverse(head)