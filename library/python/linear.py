from collections import deque
from typing import Deque, List, Optional, TypeVar, Union


class Node: 
    def __init__(self, val: Union[int, str]=None, next=None) -> None: 
        self.val = val
        self.next: Node = next
    
    def __str__(self, reverse=False) -> str:
        text = ''
        cursor = self
        sep = ' -> ' if reverse is False else ' <- '
        while cursor is not None: 
            text += str(cursor.val) + sep
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

class Stack(): 
    K = TypeVar('K')
    def __init__(self) -> None:
        self.__list: List[self.K] = []
    
    def push(self, val: K) -> None:
        self.__list.append(val)

    def pop(self) -> K: 
        return self.__list.pop()
    
    def peek(self) -> Optional[K]: 
        if self.empty(): 
            return None
        return self.__list[-1]
    
    def __len__(self) -> int:
        return len(self.__list)
    
    def empty(self) -> bool: 
        return len(self) == 0
    
    def __str__(self) -> str:
        return str(self.__list)

class Queue(): 
    K = TypeVar('K')
    def __init__(self) -> None:
        self.__root = Node()
        self.__cursor = self.__root
        self.__len = 0
    
    def add(self, val: K) -> None: 
        self.__cursor = self.__cursor.next
        self.__cursor = Node(val)
        self.__len += 1
    
    def peek(self) -> Optional[K]: 
        if self.empty(): 
            return None
        return self.__root.next.val
    
    def remove(self) -> Optional[K]: 
        if self.empty(): 
            return None
        val = self.__root.next.val
        self.__root.next = self.__root.next.next
        self.__len -= 1
        return val
    
    def poll(self) -> Optional[K]: 
        return self.remove()
    
    def __len__(self) -> int:
        return self.__len
    
    def empty(self) -> bool:
        return len(self) == 0
    
    def __str__(self) -> str:
        return self.__root.next.__str__(reverse=True)
