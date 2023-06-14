import sys
sys.path.append(sys.path[0] + '/../../../library/python')

from typing import Generic, Tuple, TypeVar
import unittest


from linear import Stack


K = TypeVar('K')
# implement a class that has three stacks without using stack class 
class ArrayStack(Generic[K]): 
    def __init__(self, n_stacks) -> None:
        self.n_stacks = n_stacks

    def push(self, i: int, val: K) -> None: 
        self._check(i)

    def pop(self, i: int) -> K: 
        self._check(i)
        val = self.peek(i)
        self.remove(i)
        return val

    def peek(self, i: int) -> K: 
        self._check(i)

    def remove(self, i: int) -> None: 
        self._check(i)

    def _check(self, i: int) -> None: 
        if i < 0 or i >= self.n_stacks: 
            raise IndexError("Index out of range of the stacks")


class SolutionTest(unittest.TestCase):
    def __init__(self, methodName: str, param: Tuple) -> None:
        super().__init__(methodName)
        self.input, self.output = param[0], param[1]
    def test_runs(self): 
        self.assertEqual(solution(*self.input), self.output)

if __name__ == '__main__': 
    '''
    cases = [] # edit here
    suite = unittest.TestSuite()
    for i, o in cases: 
        suite.addTest(SolutionTest('test_runs', (i, o)))
    unittest.TextTestRunner(verbosity=2).run(suite)
    '''
    print(solution(Stack(1, 2, 3), Stack(100, 105, 120), Stack(205, 201, 304, 6, 8, 9, 106, 243)))
