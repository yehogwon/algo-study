import sys
sys.path.append(sys.path[0] + '/../../../library/python')

from typing import Tuple, Union
import unittest


from linear import Node, LinkedListTool


def solution(root: Node, k: int) -> Union[int, str]: 
    length = -1
    cursor = root
    while cursor is not None: # O(n)
        length += 1
        cursor = cursor.next
    cursor = root
    for _ in range(length - k + 1): 
        cursor = cursor.next
    return cursor.val


class SolutionTest(unittest.TestCase):
    def __init__(self, methodName: str, param: Tuple) -> None:
        super().__init__(methodName)
        self.input, self.output = param[0], param[1]
    def test_runs(self): 
        self.assertEqual(solution(*self.input), self.output)

if __name__ == '__main__': 
    cases = [((LinkedListTool.create([1, 2, 3, 4, 5]), 2), 4), ((LinkedListTool.create(['a', 'b', 'd', 'e', 'g', 'c']), 3), 'e')] # edit here
    suite = unittest.TestSuite()
    for i, o in cases: 
        suite.addTest(SolutionTest('test_runs', (i, o)))
    unittest.TextTestRunner(verbosity=2).run(suite)
