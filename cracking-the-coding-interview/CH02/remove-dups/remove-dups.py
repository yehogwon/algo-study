import sys
sys.path.append(sys.path[0] + '/../../../library/python')

from typing import Tuple
import unittest


from linear import Node, LinkedList

# Solution for the original question
def solution(root: Node) -> Node: 
    ll = LinkedList()
    items = set()
    cursor = root
    while cursor:
        if cursor.val not in items:
            items.add(cursor.val)
            ll.add(cursor.val)
        cursor = cursor.next
    return ll.head

# Solution for the follow-up question
def solution(root: Node) -> Node: 
    p1, p2 = root, root
    while p1: 
        p2 = p1
        while p2 and p2.next: 
            if p1.val == p2.next.val: 
                p2.next = p2.next.next
            else: 
                p2 = p2.next
        p1 = p1.next
    return root

class SolutionTest(unittest.TestCase):
    def __init__(self, methodName: str, param: Tuple) -> None:
        super().__init__(methodName)
        self.input, self.output = param[0], param[1]
    def test_runs(self): 
        self.assertEqual(solution(self.input).tolist(), self.output.tolist())

if __name__ == '__main__': 
    cases = [
        (LinkedList(1, 2, 2, 5, 3, 4, 5, 9, 9, 8).head, LinkedList(1, 2, 5, 3, 4, 9, 8).head),
        (LinkedList(1).head, LinkedList(1).head), 
        (LinkedList(1, 2, 3, 4, 5, 3).head, LinkedList(1, 2, 3, 4, 5).head),
        (LinkedList(1, 1, 2, 3, 4, 5).head, LinkedList(1, 2, 3, 4, 5).head)
    ] # edit here
    suite = unittest.TestSuite()
    for i, o in cases: 
        suite.addTest(SolutionTest('test_runs', (i, o)))
    unittest.TextTestRunner(verbosity=2).run(suite)
