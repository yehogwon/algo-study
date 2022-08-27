from typing import Tuple
import unittest

def solution(s1: str, s2: str) -> bool: 
    alphabets = [chr(i) for i in range(ord('a'), ord('z') + 1)]
    _s1, _s2 = list(s1), list(s2)
    if len(_s1) == len(_s2) + 1: # Try to delete a character
        for i in range(len(_s1)): # O(S1)
            if _s1[:i] + _s1[i + 1:] == _s2: 
                return True
    elif len(_s1) == len(_s2) - 1: # Try to insert a character
        for i in range(len(_s1) + 1): # O(S1 * 26) = O(S1) -> practically, it might matter. 
            for c in alphabets: 
                if _s1[:i] + [c] + _s1[i:] == _s2: 
                    return True
    elif len(_s1) == len(_s2): # Try to replace a character
        diff_count = 0
        for i in range(len(_s1)): # O(S1)
            if _s1[i] != _s2[i]: 
                diff_count += 1
                if diff_count > 1: 
                    return False
        return True
    return False


class SolutionTest(unittest.TestCase):
    def __init__(self, methodName: str, param: Tuple) -> None:
        super().__init__(methodName)
        self.input, self.output = param[0], param[1]
    def test_runs(self): 
        self.assertEqual(solution(*self.input), self.output)

if __name__ == '__main__': 
    cases = [
        (('pale', 'ple'), True),
        (('pales', 'pale'), True),
        (('pale', 'bale'), True),
        (('paleabc', 'pleabc'), True),
        (('pale', 'ble'), False),
        (('a', 'b'), True),
        (('d', 'de'), True),
        (('pale', 'pale'), True),
        (('pale', 'ple'), True),
        (('ple', 'pale'), True),
        (('pale', 'bale'), True),
        (('pale', 'bake'), False),
        (('pale', 'pse'), False),
        (('ples', 'pales'), True),
        (('pale', 'pas'), False),
        (('pas', 'pale'), False),
        (('pale', 'pkle'), True),
        (('pkle', 'pable'), False),
        (('pal', 'palks'), False),
        (('palks', 'pal'), False), 
        (('', 'd'), True)
    ] # edit here
    suite = unittest.TestSuite()
    for i, o in cases: 
        suite.addTest(SolutionTest('test_runs', (i, o)))
    unittest.TextTestRunner(verbosity=2).run(suite)
