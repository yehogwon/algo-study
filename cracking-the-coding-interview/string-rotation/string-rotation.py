from typing import Tuple
import unittest


def isSubstring(s1: str, s2: str) -> bool: 
    """
    returns True if and only if s1 contains s2
    """
    return s1 in s2

def solution(s1: str, s2: str) -> bool: 
    if len(s1) != len(s2) or len(s1) == 0: 
        return False
    return isSubstring(s1, s2 * 2)


class SolutionTest(unittest.TestCase):
    def __init__(self, methodName: str, param: Tuple) -> None:
        super().__init__(methodName)
        self.input, self.output = param[0], param[1]
    def test_runs(self): 
        self.assertEqual(solution(*self.input), self.output)

if __name__ == '__main__': 
    cases = [(('waterbottle', 'erbottlewat'), True)] # edit here
    suite = unittest.TestSuite()
    for i, o in cases: 
        suite.addTest(SolutionTest('test_runs', (i, o)))
    unittest.TextTestRunner(verbosity=2).run(suite)

