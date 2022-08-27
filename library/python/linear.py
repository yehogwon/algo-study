from typing import List, Union


class Node: 
    def __init__(self, val: Union[int, str]=None, next=None) -> None: 
        self.val = val
        self.next = next
    
    def __str__(self) -> str:
        text = ''
        cursor = self
        while cursor is not None: 
            text += str(cursor.val) + ' -> '
            cursor = cursor.next
        if len(text) > 0: 
            text = text[:-4]
        return text

class LinkedList: 
    @classmethod
    def create(cls, l: List[Union[int, str]], cycle: int=-1) -> Node: 
        if (not l) or len(l) == 0: 
            return
        if cycle >= 0: 
            return cls._create_cycle(l, cycle)
        else: 
            return cls._create(l)
    
    @staticmethod
    def _create(l: List[Union[int, str]]) -> Node: 
        head = Node()
        cur = head
        for val in l: 
            cur.next = Node(val)
            cur = cur.next
        return head.next
    
    @staticmethod
    def _create_cycle(l: List[Union[int, str]], cycle: int=-1) -> Node: 
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
        for val in l: 
            cur.next = Node(val)
            cur = cur.next
        root.next = head.next
