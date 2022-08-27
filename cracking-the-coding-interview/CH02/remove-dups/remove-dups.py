from collections import defaultdict
import unittest
from typing import List, Union


class Node: 
    def __init__(self, val: Union[int, str]=None, next=None) -> None: 
        self.val = val
        self.next = next

class LinkedList: 
    @staticmethod
    def create(l: List[Union[int, str]]): 
        if (not len) or len(l) == 0: 
            return 0
        head = Node()
        cur = head
        for val in l: 
            cur.next = Node(val)
            cur = cur.next
        return head.next


def solution(root: Node) -> Node: 
    counts = defaultdict(lambda: 0)
    cursor = root
    while cursor: 
        counts[cursor.val] += 1
        cursor = cursor.next
    if counts[root.val] > 1: 
        root = root.next
    cursor = root
    while cursor.next: 
        if counts[cursor.val] <= 1: 
            continue
        if cursor.next: 
            pass


class TestSolution(unittest.TestCase):
    def test_runs(self): 
        cases = [(LinkedList.create([1, 2, 2, 5, 3, 4, 5, 9, 9, 8]), LinkedList.create([1, 3, 4, 8]))]
        for i, o in cases: 
            self.assertEqual(solution(i), o)

if __name__ == '__main__': 
    unittest.main()
