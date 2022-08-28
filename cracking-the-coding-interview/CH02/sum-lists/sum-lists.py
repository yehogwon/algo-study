import sys
sys.path.append(sys.path[0] + '/../../../library/python')

from typing import Tuple
import unittest


from linear import LinkedList, Node

def solution(head1: Node, head2: Node) -> Node: 
    ll: LinkedList[int] = LinkedList()
    cursor1, cursor2 = head1, head2
    _up = 0
    while cursor1 or cursor2: 
        num = 0
        if not cursor1: 
            num = cursor2.val
        elif not cursor2: 
            num = cursor1.val
        else: 
            num = cursor1.val + cursor2.val
        ll.insert(0, (num + _up) % 10)
        _up = (num + _up) // 10
        cursor1 = cursor1.next
        cursor2 = cursor2.next
    return ll.head


class TestSolution(unittest.TestCase):
    def test_runs(self): 
        cases = [((LinkedList(7, 1, 6).head, LinkedList(5, 9, 2).head), LinkedList(9, 1, 2).head)]
        for i, o in cases: 
            self.assertEqual(solution(*i), o)

if __name__ == '__main__': 
    unittest.main()
