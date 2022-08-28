from collections import deque
from typing import Tuple, Generic, List, Optional, TypeVar
import unittest

K = TypeVar('K')

class Node(Generic[K]): 
    def __init__(self, val: K, next=None) -> None: 
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

class LinkedList(Generic[K]): 
    def __init__(self, *args: Tuple[K]) -> None:
        self.head = None
        self.cur = self.head # always points the last node
        self._len = 0

        if len(args) > 0: 
            for _val in args[0]: 
                self.add(_val)
    
    def add(self, val: K) -> None: 
        if not self.head: 
            self.head = Node(val)
            self.cur = self.head
        else:
            self.cur.next = Node(val)
            self.cur = self.cur.next
        self._len += 1

    def insert(self, index: int, val: K) -> None: 
        if index < 0: 
            index += self._len
        if index > self._len: 
            index = self._len
        if index < 0: 
            raise IndexError(f'Index {index} out of range {self._len} : LinkedList')
        if index == 0: 
            self.head = Node(val, self.head)
        else: 
            _cursor = self.head
            for _ in range(index - 1):
                _cursor = _cursor.next
            _cursor.next = Node(val, _cursor.next)
        self._len += 1
    
    def pop(self, index: int=-1) -> K: 
        val = self.peek(index)
        self.remove(index)
        return val

    def peek(self, index: int=-1) -> K: 
        if index < 0: 
            index += self._len
        if index > self._len or index < 0: 
            raise IndexError(f'Index {index} out of range {self._len} : LinkedList')
        _cursor = self.head
        for _ in range(index): 
            _cursor = _cursor.next
        return _cursor.val

    def remove(self, index: int=-1): 
        if index < 0: 
            index += self._len
        if index > self._len or index < 0:
            raise IndexError(f'Index {index} out of range {self._len} : LinkedList')
        if index == 0: 
            self.head = self.head.next
        else:
            _cursor = self.head
            for _ in range(index - 1):
                _cursor = _cursor.next
            _cursor.next = _cursor.next.next
        self._len -= 1

    def empty(self) -> bool: 
        return self._len == 0

    def __len__(self) -> int: 
        return self._len
    
    def __str__(self) -> str:
        _str = ''
        _cursor = self.head
        while _cursor: 
            _str += str(_cursor.val) + ' -> '
            _cursor = _cursor.next
        if len(_str) > 0:
            _str = _str[:-4]
        return '[LinkedList : ' + _str + ']'

class LinkedListTool(Generic[K]): 
    @classmethod
    def create(cls, l: List[K], cycle: int=-1) -> Node: 
        if (not l) or len(l) == 0: 
            return
        if cycle >= 0: 
            return cls._create_cycle(l, cycle)
        else: 
            return cls._create(l)
    
    @staticmethod
    def _create(l: List[K]) -> Node: 
        head = Node()
        cur = head
        for val in l: 
            cur.next = Node(val)
            cur = cur.next
        return head.next
    
    @staticmethod
    def _create_cycle(l: List[K], cycle: int=-1) -> Node: 
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
    def append(root: Node, l: List[K]) -> None: 
        if (not l) or len(l) == 0: 
            return
        head = Node()
        cur = head
        for val in l: 
            cur.next = Node(val)
            cur = cur.next
        root.next = head.next

class Stack(Generic[K]): 
    def __init__(self) -> None:
        self.__list: List[K] = []
    
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

# FIXME: Re-Implement the queue datastructure
class Queue(Generic[K]): 
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

if __name__ == '__main__': 
    ll: LinkedList[int] = LinkedList([1, 2, 3, 4, 5])
    print(ll)
    ll.insert(0, 10)
    print(ll)
    ll.remove(3)
    print(ll)
    ll.remove(1)
    print(ll)
    ll.remove(0)
    print(ll)
    ll.add(100)
    print(ll)
    ll.add(58)
    print(ll)
    ll.add(37)
    print(ll)
    print('POP: ', ll.pop())
    print(ll)
    print('POP: ', ll.pop())
    print(ll)
    print('PEEK: ', ll.peek())
    print(ll)
    print('PEEK: ', ll.peek(0))
    print(ll)
    print('POP: ', ll.pop())
    print(ll)
    print('POP: ', ll.pop())
    print(ll)
    print('POP: ', ll.pop())
    print(ll)
    print(ll.empty())
    print('POP: ', ll.pop())
    print(ll)
    print(ll.empty())
