import sys
sys.path.append(sys.path[0] + '/../../../library/python')

from typing import Tuple
import unittest


from linear import LinkedList, Node

# Solution of my own
def solution(head: Node, partition: int) -> Node: 
    less, great = Node(0), Node(0)
    p1, p2 = less, great
    cursor = head
    while cursor: 
        if cursor.val < partition: 
            p1.next = Node(cursor.val)
            p1 = p1.next
        else: 
            p2.next = Node(cursor.val)
            p2 = p1.next
        cursor = cursor.next
    p1.next = great.next
    return less.next

# Solution of the textbook
def solution(head: Node, partition: int) -> Node: 
    front, back = head, head
    cursor = head
    while cursor: 
        _next = cursor.next
        if cursor.val < partition: 
            cursor.next = front
            front = cursor
        else: 
            back.next = cursor
            back = cursor
        cursor = _next
    back.next = None
    return front


class SolutionTest(unittest.TestCase):
    def __init__(self, methodName: str, param: Tuple) -> None:
        super().__init__(methodName)
        self.input, self.output = param[0], param[1]
    def test_runs(self): 
        _result, _output = solution(*self.input[:-1]).tolist(), self.output.tolist()
        _index = self.input[-1]
        self.assertCountEqual(_result[:_index], _output[:_index])
        self.assertCountEqual(_result[_index:], _output[_index:])

if __name__ == '__main__': 
    cases = [
        ((LinkedList(3, 5, 8, 5, 10, 2, 1).head, 5, 3), LinkedList(3, 1, 2, 10, 5, 5, 8).head)
    ] # edit here
    suite = unittest.TestSuite()
    for i, o in cases: 
        suite.addTest(SolutionTest('test_runs', (i, o)))
    unittest.TextTestRunner(verbosity=2).run(suite)
