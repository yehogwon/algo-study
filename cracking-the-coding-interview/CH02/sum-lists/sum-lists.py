import sys
sys.path.append(sys.path[0] + '/../../../library/python')

from typing import Tuple
import unittest


from linear import LinkedList, Node

# Solution (iterative) for the original problem
def solution(head1: Node, head2: Node) -> Node: 
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
def solution(head1: Node, head2: Node) -> Node: 
    def _len(node: Node) -> int: 
        if not node: 
            return 0
        return 1 + _len(node.next)
    l1, l2 = _len(head1), _len(head2)
    longer = head1 if l1 > l2 else head2
    shorter = head2 if l1 > l2 else head1
    for _ in range(abs(l1 - l2)):
        shorter = Node(0, shorter)
    _sum = 0
    c1, c2 = longer, shorter
    while c1 and c2:
        _sum = _sum * 10 + (c1.val + c2.val)
        c1 = c1.next
        c2 = c2.next
    return LinkedList(*[int(item) for item in str(_sum)]).head


class SolutionTest(unittest.TestCase):
    def __init__(self, methodName: str, param: Tuple) -> None:
        super().__init__(methodName)
        self.input, self.output = param[0], param[1]
    def test_runs(self): 
        self.assertEqual(solution(*self.input).tolist(), self.output.tolist())

if __name__ == '__main__': 
    cases = [ # cases for the original problem
        ((LinkedList(7, 1, 6).head, LinkedList(5, 9, 2).head), LinkedList(2, 1, 9).head), 
        ((LinkedList(8, 1).head, LinkedList(5).head), LinkedList(3, 2).head), 
        ((LinkedList(9, 7, 8).head, LinkedList(6, 8, 5).head), LinkedList(5, 6, 4, 1).head), 
    ] # edit here

    cases = [ # cases for the follow-up problem
        ((LinkedList(6, 1, 7).head, LinkedList(2, 9, 5).head), LinkedList(9, 1, 2).head), 
        ((LinkedList(8, 1).head, LinkedList(5).head), LinkedList(8, 6).head), 
        ((LinkedList(9, 7, 8).head, LinkedList(6, 8, 5).head), LinkedList(1, 6, 6, 3).head), 
    ] # edit here

    suite = unittest.TestSuite()
    for i, o in cases: 
        suite.addTest(SolutionTest('test_runs', (i, o)))
    unittest.TextTestRunner(verbosity=2).run(suite)
