import sys
sys.path.append(sys.path[0] + '/../../../library/python')

from typing import Tuple, Union
import unittest


from linear import Node, LinkedList


def solution(root: Node, k: int) -> Union[int, str]: 
    p1, p2 = root, root
    for _ in range(k): 
        if p1 is None: 
            return
        p1 = p1.next
    while p1: 
        p1 = p1.next
        p2 = p2.next
    return p2.val


class SolutionTest(unittest.TestCase):
    def __init__(self, methodName: str, param: Tuple) -> None:
        super().__init__(methodName)
        self.input, self.output = param[0], param[1]
    def test_runs(self): 
        self.assertEqual(solution(*self.input), self.output)

if __name__ == '__main__': 
    cases = [
        ((LinkedList(1, 2, 3, 4, 5).head, 2), 4), 
        ((LinkedList('a', 'b', 'd', 'e', 'g', 'c').head, 3), 'e')
    ] # edit here
    suite = unittest.TestSuite()
    for i, o in cases: 
        suite.addTest(SolutionTest('test_runs', (i, o)))
    unittest.TextTestRunner(verbosity=2).run(suite)
