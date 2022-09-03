import sys
sys.path.append(sys.path[0] + '/../../../library/python')

from typing import Dict, Generic, TypeVar
import unittest


from linear import Stack

K = TypeVar('K')

# My original solution
class MinStack(Stack, Generic[K]): 
    def __init__(self) -> None:
        super().__init__()
        self._mins = Stack()

    def push(self, val: K) -> None: 
        super().push(val)
        if len(self._mins) == 0 or val <= self._mins.peek(): 
            self._mins.push(val)
    
    def pop(self) -> K: 
        val = super().pop()
        if val == self._mins.peek(): 
            self._mins.pop()
        return val
    
    def min(self) -> K: 
        return self._mins.peek()

# Non-optimal solution from the textbook
class MinStack(Stack, Generic[K]): 
    def __init__(self) -> None:
        super().__init__()
        self._mins = Stack()

    def push(self, val: K) -> None: 
        super().push(val)
        self._mins.push(min(val, self._mins.peek() if not self._mins.empty() else val))
    
    def pop(self) -> K: 
        val = super().pop()
        self._mins.pop()
        return val
    
    def min(self) -> K: 
        return self._mins.peek()
 

class SolutionTest(unittest.TestCase):
    def test_runs(self): 
        stack = MinStack()
        self.assertIsNone(stack.min())

        stack.push(5)
        self.assertEqual(stack.min(), 5)

        stack.push(6)
        self.assertEqual(stack.min(), 5)

        stack.push(3)
        self.assertEqual(stack.min(), 3)

        stack.push(7)
        self.assertEqual(stack.min(), 3)

        stack.push(3)
        self.assertEqual(stack.min(), 3)

        stack.pop()
        self.assertEqual(stack.min(), 3)

        stack.pop()
        self.assertEqual(stack.min(), 3)

        stack.pop()
        self.assertEqual(stack.min(), 5)

        stack.push(1)
        self.assertEqual(stack.min(), 1)

if __name__ ==  '__main__': 
    unittest.main()
