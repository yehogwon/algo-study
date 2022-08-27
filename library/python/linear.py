from typing import List, Union


class Node: 
    def __init__(self, val: Union[int, str]=None, next=None) -> None: 
        self.val = val
        self.next = next

# Linked List without any cycle
class LinkedList: 
    @staticmethod
    def create(l: List[Union[int, str]]) -> Node: 
        if (not l) or len(l) == 0: 
            return
        head = Node()
        cur = head
        for val in l: 
            cur.next = Node(val)
            cur = cur.next
        return head.next
    
    @staticmethod
    def append(root: Node, l: List[Union[int, str]]) -> None: 
        if (not l) or len(l) == 0: 
            return
        head = Node()
        cur = head
        _cycle = None
        for i, val in enumerate(l): 
            cur.next = Node(val)
            cur = cur.next
        root.next = head.next

# Linked List with a cycle
class LinkedList: 
    @staticmethod
    def create(l: List[Union[int, str]], cycle: int=-1) -> Node: 
        if (not l) or len(l) == 0: 
            return None
        head = Node()
        cur = head
        _cycle = None
        for i, val in enumerate(l): 
            cur.next = Node(val)
            cur = cur.next
            if i == cycle: 
                _cycle = cur
        cur.next = _cycle
        return head.next
    
    @staticmethod
    def append(root: Node, l: List[Union[int, str]]) -> None: 
        if (not l) or len(l) == 0: 
            return
        head = Node()
        cur = head
        _cycle = None
        for i, val in enumerate(l): 
            cur.next = Node(val)
            cur = cur.next
        root.next = head.next
