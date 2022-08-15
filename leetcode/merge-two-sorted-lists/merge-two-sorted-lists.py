# solved
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        top = ListNode()
        cur = top
        while list1 != None or list2 != None:
            if list1 == None: 
                cur.next = list2
                list2 = list2.next
            elif list2 == None: 
                cur.next = list1
                list1 = list1.next
            elif list1.val <= list2.val: 
                cur.next = list1
                list1 = list1.next
            else: 
                cur.next = list2
                list2 = list2.next
            cur = cur.next
        return top.next