import sys
sys.path.append(sys.path[0] + '/../../../library/python')

from typing import Tuple
import unittest

from linear import Node, LinkedList, Stack

def solution(root: Node) -> bool: 
    stack = Stack()
    length = 1
    cur = root
    while cur: # O(n)
        stack.push(cur.val)
        length += 1
        cur = cur.next
    cur = root
    for _ in range(length // 2): # O(n)
        if cur.val != stack.pop(): 
            return False
        cur = cur.next
    return True


class SolutionTest(unittest.TestCase):
    def __init__(self, methodName: str, param: Tuple) -> None:
        super().__init__(methodName)
        self.input, self.output = param[0], param[1]
    def test_runs(self): 
        self.assertEqual(solution(self.input), self.output)

if __name__ == '__main__': 
    cases = [
        (LinkedList.create(list('palinilap')), True), 
        (LinkedList.create(list('abba')), True), 
        (LinkedList.create(list('asdfljj')), False)
    ] # edit here
    suite = unittest.TestSuite()
    for i, o in cases: 
        suite.addTest(SolutionTest('test_runs', (i, o)))
    unittest.TextTestRunner(verbosity=2).run(suite)
