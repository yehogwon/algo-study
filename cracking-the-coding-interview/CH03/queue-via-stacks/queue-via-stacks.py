import sys
sys.path.append(sys.path[0] + '/../../../library/python')

from typing import Generic, TypeVar
import unittest


from linear import Stack

K = TypeVar('K')
class MyQueue(Generic[K]): 
    def __init__(self) -> None:
        self.new_stack: Stack[K] = Stack()
        self.old_stack: Stack[K] = Stack()
    
    def add(self, val: K) -> None: 
        self.new_stack.push(val)

    def pop(self) -> K: 
        self._move()
        return self.old_stack.pop()

    def peek(self) -> K: 
        self._move()
        return self.old_stack.peek()
    
    def remove(self) -> None: 
        self._move()
        self.old_stack.pop()

    def _move(self) -> None: 
        if not self.old_stack.empty(): 
            return
        while not self.new_stack.empty(): 
            self.old_stack.push(self.new_stack.pop())

    def empty(self) -> bool: 
        return len(self.new_stack) + len(self.old_stack) == 0

    def __len__(self): 
        return len(self.new_stack) + len(self.old_stack)


class SolutionTest(unittest.TestCase):
    test_cases = [([1, 2, 3]), ([-1, 0, 1]), (["a", "b", "c", "d", "e", "f"])]

    def test_size(self):
        for sequence in self.test_cases:
            q = MyQueue()
            for index, val in enumerate(sequence, start=1):
                q.add(val)
                self.assertEqual(len(q), index)
            for index, val in enumerate(sequence, start=1):
                q.remove()
                self.assertEqual(len(q), len(sequence) - index)

    def test_add(self):
        for sequence in self.test_cases:
            q = MyQueue()
            for val in sequence:
                q.add(val)
            self.assertEqual(q.peek(), sequence[0])
            self.assertEqual(len(q), len(sequence))

    def test_shift_stacks(self):
        for sequence in self.test_cases:
            q = MyQueue()
            for val in sequence:
                q.add(val)
            self.assertEqual(len(q.old_stack), 0)
            self.assertEqual(len(q.new_stack), len(sequence))
            self.assertEqual(q.new_stack.peek(), sequence[-1])
            q._move()
            self.assertEqual(len(q.old_stack), len(sequence))
            self.assertEqual(len(q.new_stack), 0)
            self.assertEqual(q.old_stack.peek(), sequence[0])

    def test_peek(self):
        for sequence in self.test_cases:
            q = MyQueue()
            for val in sequence:
                q.add(val)
                self.assertEqual(q.peek(), sequence[0])
            q.remove()
            self.assertEqual(q.peek(), sequence[1])

    def test_remove(self):
        for sequence in self.test_cases:
            q = MyQueue()
            for val in sequence:
                q.add(val)
            for i in range(len(sequence)):
                self.assertEqual(q.pop(), sequence[i])

    def test_peek_simple(self):
        q = MyQueue()
        q.add(4)
        q.add(6)
        self.assertEqual(q.peek(), 4)

    def test_add_simple(self):
        q = MyQueue()
        q.add(4)
        q.add(6)
        self.assertEqual(q.peek(), 4)
        q.add(101)
        self.assertNotEqual(q.peek(), 101)

    def test_remove_simple(self):
        q = MyQueue()
        q.add(4)
        q.add(6)
        self.assertEqual(len(q), 2)
        self.assertEqual(q.pop(), 4)
        self.assertEqual(q.pop(), 6)
        self.assertEqual(len(q), 0)
        self.assertRaises(Exception, q.pop)

if __name__ == '__main__': 
    unittest.main()
