import sys
sys.path.append(sys.path[0] + '/../../../library/python')

from typing import Tuple, List, Union
import unittest


from collections import defaultdict
from linear import Node, LinkedList


def solution(root: Node) -> Node: 
    if not (root and root.next): 
        return root
    p1, p2 = root, root.next
    while p1 and p1.next: 
        p2 = p1.next
        while p2: 
            if p1.val == p2.val: 
                p2.val = p2.next
                p2.next = p2.next.next
            else: 
                p2 = p2.next
        p1 = p1.next
    return root


class TestSolution(unittest.TestCase):
    def test_runs(self): 
        cases = [(LinkedList.create([1, 2, 2, 5, 3, 4, 5, 9, 9, 8]), LinkedList.create([1, 2, 5, 3, 4, 9, 8]))]
        for i, o in cases: 
            self.assertEqual(str(solution(i)), str(o))

if __name__ == '__main__': 
    unittest.main()
