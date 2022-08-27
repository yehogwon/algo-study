import sys
sys.path.append(sys.path[0] + '/../../../library/python')

from typing import Tuple, Union
import unittest


from linear import Node, LinkedList


def solution(root: Node, k: int) -> Union[int, str]: 
    val_stack = []
    cursor = root
    while cursor is not None: 
        val_stack.append(cursor.val)
        cursor = cursor.next
    for _ in range(k - 1): 
        val_stack.pop()
    return val_stack.pop()


class SolutionTest(unittest.TestCase):
    def __init__(self, methodName: str, param: Tuple) -> None:
        super().__init__(methodName)
        self.input, self.output = param[0], param[1]
    def test_runs(self): 
        self.assertEqual(solution(*self.input), self.output)

if __name__ == '__main__': 
    cases = [((LinkedList.create([1, 2, 3, 4, 5]), 2), 4), ((LinkedList.create(['a', 'b', 'd', 'e', 'g', 'c']), 3), 'e')] # edit here
    suite = unittest.TestSuite()
    for i, o in cases: 
        suite.addTest(SolutionTest('test_runs', (i, o)))
    unittest.TextTestRunner(verbosity=2).run(suite)
