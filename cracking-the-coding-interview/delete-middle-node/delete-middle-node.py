from typing import List, Tuple, Union
import unittest


class Node: 
    def __init__(self, val: Union[int, str]=None, next=None) -> None: 
        self.val = val
        self.next = next
    
    def __str__(self) -> str:
        text = ''
        cursor = self
        while cursor is not None: 
            text += str(cursor.val) + ' -> '
            cursor = cursor.next
        if len(text) > 0: 
            text = text[:-4]
        return text

class LinkedList: 
    @staticmethod
    def create(l: List[Union[int, str]]) -> Node: 
        if (not l) or len(l) == 0: 
            return
        head = Node()
        cur = head
        for val in l: 
            cur.next = Node(val)
            cur = cur.next
        return head.next
    
    @staticmethod
    def append(root: Node, l: List[Union[int, str]]) -> None: 
        if (not l) or len(l) == 0: 
            return
        head = Node()
        cur = head
        for i, val in enumerate(l): 
            cur.next = Node(val)
            cur = cur.next
        root.next = head.next


def solution(node: Node) -> None: 
    node.val = node.next.val
    node.next = node.next.next


class SolutionTest(unittest.TestCase):
    def __init__(self, methodName: str, param: Tuple) -> None:
        super().__init__(methodName)
        self.input, self.output = param[0], param[1]
    def test_runs(self): 
        self.assertEqual(solution(self.input), self.output)

if __name__ == '__main__': 
    cases = [] # edit here
    suite = unittest.TestSuite()
    for i, o in cases: 
        suite.addTest(SolutionTest('test_runs', (i, o)))
    unittest.TextTestRunner(verbosity=2).run(suite)
