import sys
sys.path.append(sys.path[0] + '/../../../library/python')

from typing import Tuple
import unittest

from linear import LinkedList, Node, Stack

# using backtracking with a stack
def solution(head: Node) -> bool: 
    stack = Stack()
    length = 1
    cur = head
    while cur: # O(n)
        stack.push(cur.val)
        length += 1
        cur = cur.next
    cur = head
    for _ in range(length // 2): # O(n)
        if cur.val != stack.pop(): 
            return False
        cur = cur.next
    return True

# using two pointers teechnique and a stack
def solution(head: Node[str]) -> bool: 
    slow, fast = head, head
    stack = Stack[str]()
    while fast and fast.next:
        stack.push(slow.val)
        slow = slow.next
        fast = fast.next.next
    if fast: # odd number of nodes
        slow = slow.next
    while slow:
        if slow.val != stack.pop():
            return False
        slow = slow.next
    return True

class SolutionTest(unittest.TestCase):
    def __init__(self, methodName: str, param: Tuple) -> None:
        super().__init__(methodName)
        self.input, self.output = param[0], param[1]
    def test_runs(self): 
        self.assertEqual(solution(self.input), self.output)

if __name__ == '__main__': 
    cases = [
        (LinkedList(*list('palinilap')).head, True), 
        (LinkedList(*list('abba')).head, True), 
        (LinkedList(*list('asdfljj')).head, False)
    ] # edit here
    suite = unittest.TestSuite()
    for i, o in cases: 
        suite.addTest(SolutionTest('test_runs', (i, o)))
    unittest.TextTestRunner(verbosity=2).run(suite)
