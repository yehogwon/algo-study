import sys
sys.path.append(sys.path[0] + '/../../../library/python')

from typing import Tuple
import unittest


from linear import LinkedList, Node

# Solution (iterative) for the original problem
def _solution(head1: Node, head2: Node) -> Node: 
    ll: LinkedList[int] = LinkedList()
    cursor1, cursor2 = head1, head2
    _up = 0
    while cursor1 or cursor2: 
        num = 0
        if not cursor1: 
            num = cursor2.val
            cursor2 = cursor2.next
        elif not cursor2: 
            num = cursor1.val
            cursor1 = cursor1.next
        else: 
            num = cursor1.val + cursor2.val
            cursor1 = cursor1.next
            cursor2 = cursor2.next
        ll.add((num + _up) % 10)
        _up = (num + _up) // 10
    if _up != 0: 
        ll.add(_up)
    return ll.head

# Solution (recursive) for the original problem
def solution(head1: Node[int], head2: Node[int]) -> Node[int]: 
    def recursion(node1: Node[int], node2: Node[int], up: int) -> Node[int]: 
        if not node1 and not node2: 
            return None if up == 0 else Node(up)
        if not node1: 
            num = node2.val
            node2 = node2.next
        elif not node2: 
            num = node1.val
            node1 = node1.next
        else: 
            num = node1.val + node2.val
            node1 = node1.next
            node2 = node2.next
        node = Node((num + up) % 10)
        node.next = recursion(node1, node2, (num + up) // 10)
        return node
    return recursion(head1, head2, 0)

# Solution for the follow-up problem
def _solution(head1: Node, head2: Node) -> Node: 
    pass


class SolutionTest(unittest.TestCase):
    def __init__(self, methodName: str, param: Tuple) -> None:
        super().__init__(methodName)
        self.input, self.output = param[0], param[1]
    def test_runs(self): 
        self.assertEqual(solution(*self.input).tolist(), self.output.tolist())

if __name__ == '__main__': 
    cases = [
        ((LinkedList(7, 1, 6).head, LinkedList(5, 9, 2).head), LinkedList(2, 1, 9).head), 
        ((LinkedList(8, 1).head, LinkedList(5).head), LinkedList(3, 2).head), 
        ((LinkedList(9, 7, 8).head, LinkedList(6, 8, 5).head), LinkedList(5, 6, 4, 1).head), 
    ] # edit here
    suite = unittest.TestSuite()
    for i, o in cases: 
        suite.addTest(SolutionTest('test_runs', (i, o)))
    unittest.TextTestRunner(verbosity=2).run(suite)
