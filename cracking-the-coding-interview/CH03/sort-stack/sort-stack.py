import sys
sys.path.append(sys.path[0] + '/../../../library/python')

from typing import Generic, Tuple, TypeVar
import unittest


from linear import Stack

K = TypeVar('K')
class SortedStack(Stack, Generic[K]): 
    def __init__(self) -> None:
        super().__init__()
        self._stack: Stack[K] = Stack()
    
    def push(self, val: K) -> None: 
        while not self.empty() and self.peek() < val: 
            self._stack.push(self.pop())
        super().push(val)
        while not self._stack.empty(): 
            super().push(self._stack.pop())


class SolutionTest(unittest.TestCase):
    def test_push_one(self):
        stack = SortedStack()
        stack.push(1)
        assert len(stack) == 1

    def test_push_two(self):
        stack = SortedStack()
        stack.push(1)
        stack.push(2)
        assert len(stack) == 2

    def test_push_three(self):
        stack = SortedStack()
        stack.push(1)
        stack.push(2)
        stack.push(3)
        assert len(stack) == 3

    def test_pop_one(self):
        stack = SortedStack()
        stack.push(1)
        assert stack.pop() == 1

    def test_pop_two(self):
        stack = SortedStack()
        stack.push(1)
        stack.push(2)
        assert stack.pop() == 1
        assert stack.pop() == 2

    def test_pop_three(self):
        stack = SortedStack()
        stack.push(1)
        stack.push(2)
        stack.push(3)
        assert stack.pop() == 1
        assert stack.pop() == 2
        assert stack.pop() == 3

    def test_push_mixed(self):
        stack = SortedStack()
        stack.push(3)
        stack.push(2)
        stack.push(1)
        stack.push(4)
        assert stack.pop() == 1
        assert stack.pop() == 2
        assert stack.pop() == 3
        assert stack.pop() == 4

if __name__ == '__main__': 
    unittest.main()
