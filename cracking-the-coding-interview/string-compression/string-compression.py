from typing import Tuple
import unittest


def solution(org: str) -> str: 
    comp = ''
    count = 0
    for i, c in enumerate(org):
        if i != 0 and c != org[i - 1]: 
            comp += org[i - 1] + str(count)
            count = 0
        count += 1
    comp += org[-1] + str(count)
    return min(org, comp, key=len)


class SolutionTest(unittest.TestCase):
    def __init__(self, methodName: str, param: Tuple) -> None:
        super().__init__(methodName)
        self.input, self.output = param[0], param[1]
    def test_runs(self): 
        self.assertEqual(solution(self.input), self.output)

if __name__ == '__main__': 
    cases = [('aabcccccaaa', 'a2b1c5a3'), ('abcdef', 'abcdef')] # edit here
    suite = unittest.TestSuite()
    for i, o in cases: 
        suite.addTest(SolutionTest('test_runs', (i, o)))
    unittest.TextTestRunner(verbosity=2).run(suite)
