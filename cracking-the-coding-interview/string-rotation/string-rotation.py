import unittest

def isSubstring(s1: str, s2: str) -> bool: 
    '''
    returns True if and only if s1 contains s2
    '''
    return s1 in s2

def solution() -> bool: 
    return True


class TestSolution(unittest.TestCase):
    def test_runs(self): 
        self.assertEqual(solution(self.input), self.output)

if __name__ == '__main__': 
    cases = [('waterbottle', 'erbottlewat')]
    for i, o in cases:
