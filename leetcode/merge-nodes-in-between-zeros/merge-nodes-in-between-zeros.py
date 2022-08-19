# solved
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        node = head
        while node is not None and node.next is not None: 
            if node.val == 0: 
                node.val = node.next.val
                node.next = node.next.next
            else: 
                if node.next.val == 0: 
                    node.next = node.next.next
                    node = node.next
                else: 
                    node.val += node.next.val
                    node.next = node.next.next
        return head
        