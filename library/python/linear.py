from typing import Tuple, Generic, List, Optional, TypeVar

K = TypeVar('K')

class Node(Generic[K]): 
    def __init__(self, val: K, next=None) -> None: 
        self.val = val
        self.next: Node = next

    def tolist(self) -> List[K]: 
        _cursor = self
        _list = []
        while _cursor: 
            _list.append(_cursor.val)
            _cursor = _cursor.next
        return _list
    
    def __repr__(self, name='Node') -> str:
        _str = ' -> '.join([str(item) for item in self.tolist()])
        return f'[{name} : ' + _str + ']'
    
    def __eq__(self, comp: object) -> bool:
        return self.tolist() == comp.tolist()

class LinkedList(Generic[K]): 
    def __init__(self, *args: Tuple[K]) -> None:
        self.__head = None
        self.__cur = self.__head # always points the last node
        self._len = 0

        for _val in args: 
            self.add(_val)
    
    def add(self, val: K) -> None: 
        if not self.__head: 
            self.__head = Node(val)
            self.__cur = self.__head
        else:
            self.__cur.next = Node(val)
            self.__cur = self.__cur.next
        self._len += 1

    def insert(self, index: int, val: K) -> None: 
        if index < 0: 
            index += self._len
        if index > self._len: 
            index = self._len
        if index < 0: 
            raise IndexError(f'Index {index} out of range {self._len} : LinkedList')
        if index == 0: 
            self.__head = Node(val, self.__head)
        else: 
            _cursor = self.__head
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
        _cursor = self.__head
        for _ in range(index): 
            _cursor = _cursor.next
        return _cursor.val

    def remove(self, index: int=-1): 
        if index < 0: 
            index += self._len
        if index >= self._len or index < 0:
            raise IndexError(f'Index {index} out of range {self._len} : LinkedList')
        if index == 0: 
            self.__head = self.__head.next
        else:
            _cursor = self.__head
            for _ in range(index - 1):
                _cursor = _cursor.next
            _cursor.next = _cursor.next.next
        self._len -= 1

    def empty(self) -> bool: 
        return self._len == 0

    def __len__(self) -> int: 
        return self._len
    
    def tolist(self) -> List[K]: 
        _cursor = self.__head
        _list = []
        while _cursor: 
            _list.append(_cursor.val)
            _cursor = _cursor.next
        return _list
    
    def __repr__(self, name='LinkedList') -> str:
        _str = ' -> '.join([str(item) for item in self.tolist()])
        return f'[{name} : ' + _str + ']'
    
    def __eq__(self, comp: object) -> bool:
        return self.tolist() == comp.tolist()

    @property
    def head(self) -> Node:
        return self.__head

# TODO: Refactor: remove-dups.py, return-kth-to-last.py
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
    def __init__(self, *args) -> None:
        self.__list: List[K] = list(args)
    
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
        return '[Stack : ' + ', '.join([str(item) for item in self.__list]) + ']'

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
    stack = Stack(1, 2, 3)
    print(stack)
