import unittest


def solution(org: str) -> str: 
    if len(org) == 0: 
        return ''
    comp = ''
    tmp = org[0] # keep it of length 1
    _count = 1
    for c in org[1:]:
        if c == tmp: 
            _count += 1
        else: 
            comp += tmp + str(_count)
            tmp = c
            _count = 1
    comp += tmp + str(_count)

    if len(comp) >= len(org): 
        return org
    else: 
        return comp

class TestSolution(unittest.TestCase):
    def test_runs(self): 
        cases = [
            ('aabcccccaaa', 'a2b1c5a3'), 
            ('abcdef', 'abcdef')
        ]
        for i, o in cases: 
            self.assertEqual(solution(i), o)

if __name__ == '__main__': 
    unittest.main()
