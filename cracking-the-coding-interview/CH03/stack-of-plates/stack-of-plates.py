import sys
sys.path.append(sys.path[0] + '/../../../library/python')

from typing import Generic, List, Tuple, TypeVar
import unittest


from linear import Stack

K = TypeVar('K')
class SetOfStacks(Generic[K]): 
    def __init__(self, capacity) -> None:
        self.stacks: List[Stack[K]] = []
        self.capacity = capacity
    
    def push(self, val: K) -> None: 
        if len(self.stacks) == 0 or len(self.stacks[-1]) == self.capacity: 
            self.stacks.append(Stack())
        self.stacks[-1].push(val)
    
    def pop(self) -> K: 
        if len(self.stacks) == 0:
            raise IndexError('pop from empty stack')
        val = self.stacks[-1].pop()
        if len(self.stacks[-1]) == 0:
            del self.stacks[-1]
        return val

    def pop_at(self, index: int) -> K: 
        val = self.stacks[index].pop()
        if len(self.stacks[index]) == 0:
            del self.stacks[index]
        return val


class SolutionTest(unittest.TestCase):
    def __init__(self, methodName: str, param: Tuple) -> None:
        super().__init__(methodName)
        self.input, self.output = param[0], param[1]
    def test_runs(self): 
        popAt = self.input[-1] if len(self.input) == 4 else -1
        capacity, _input = self.input[:2]
        stack = SetOfStacks(capacity)
        for val in _input:
            stack.push(val)
        lst = []
        for _ in range(len(_input)): 
            lst.append(stack.pop() if popAt == -1 else stack.pop_at(popAt))
        self.assertEqual(lst, self.output)

if __name__ == '__main__': 
    cases = [
        ((5, list(range(39))), list(reversed(range(39)))), 
        ((5, list(range(39)), 0), list(reversed(range(39))))
    ] # edit here
    suite = unittest.TestSuite()
    for i, o in cases: 
        suite.addTest(SolutionTest('test_runs', (i, o)))
    unittest.TextTestRunner(verbosity=2).run(suite)
