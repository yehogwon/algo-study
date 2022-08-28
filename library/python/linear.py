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

        for _val in args: 
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
        if index >= self._len or index < 0: 
            raise IndexError(f'Index {index} out of range {self._len} : LinkedList')
        _cursor = self.head
        for _ in range(index): 
            _cursor = _cursor.next
        return _cursor.val

    def remove(self, index: int=-1): 
        if index < 0: 
            index += self._len
        if index >= self._len or index < 0:
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
    
    def __str__(self, name='LinkedList') -> str:
        _str = ''
        _cursor = self.head
        while _cursor: 
            _str += str(_cursor.val) + ' -> '
            _cursor = _cursor.next
        if len(_str) > 0:
            _str = _str[:-4]
        return f'[{name} : ' + _str + ']'
    
    def __eq__(self, comp: object) -> bool:
        return self.__str__() == comp.__str__()

# TODO: Refactor: palindrome.py, remove-dups.py, return-kth-to-last.py
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

class Queue(Generic[K]): # Insert backward, Pop forward
    def __init__(self, *args: Tuple[K]) -> None: 
        self.__ll: LinkedList[K] = LinkedList(*args)

    def add(self, val: K) -> None: 
        self.__ll.add(val)

    def pop(self) -> K: 
        return self.__ll.pop(0)

    def peek(self) -> K: 
        return self.__ll.peek(0)

    def remove(self): 
        self.__ll.remove(0)

    def empty(self) -> bool:
        return self.__ll.empty()

    def __len__(self) -> int:
        return len(self.__ll)

    def __str__(self) -> str:
        return self.__ll.__str__('Queue')

if __name__ == '__main__': 
    queue: Queue[int] = Queue(1, 2, 3, 4, 5, 6)
    print(queue)
    queue.remove()
    print(queue)
    queue.remove()
    print(queue)
    queue.remove()
    print(queue)
    queue.add(100)
    print(queue)
    queue.add(58)
    print(queue)
    queue.add(37)
    print(queue)
    print('POP: ', queue.pop())
    print(queue)
    print('POP: ', queue.pop())
    print(queue)
    print('PEEK: ', queue.peek())
    print(queue)
    print('PEEK: ', queue.peek())
    print(queue)
    print('POP: ', queue.pop())
    print(queue)
    print('POP: ', queue.pop())
    print(queue)
    print('POP: ', queue.pop())
    print(queue)
    print(queue.empty())
    print('POP: ', queue.pop())
    print(queue)
    print(queue.empty())
