# solved
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        l = []
        node = head
        while node is not None: 
            l.append(node.val)
            node = node.next
        return l == l[::-1]
