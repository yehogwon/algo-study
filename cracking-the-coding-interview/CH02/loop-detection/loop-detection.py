from typing import List, Union
import unittest


class Node: 
    def __init__(self, val: Union[int, str]=None, next=None) -> None: 
        self.val = val
        self.next = next

class LinkedList: 
    @staticmethod
    def create(l: List[int], cycle: int=-1): 
        if (not len) or len(l) == 0: 
            return 0
        head = Node()
        cur = head
        _cycle = None
        for i, val in enumerate(l): 
            cur.next = Node(val)
            cur = cur.next
            if i == cycle: 
                _cycle = cur
        cur.next = _cycle
        return head


def solution(head: Node) -> Union[None, int, str]: 
    tortoise, hare = head, head
    while hare and hare.next: # O(n)
        tortoise = tortoise.next
        hare = hare.next.next
        if hare == tortoise: 
            break
    if not hare or not hare.next: # in the case that the linked list doesn't have a cycle
        return None
    hare = head
    while tortoise != hare: # less than O(n)
        tortoise = tortoise.next
        hare = hare.next
    return hare.val


class TestSolution(unittest.TestCase):
    def test_runs(self): 
        cases = [
            (LinkedList.create(['A', 'B', 'C', 'D', 'E'], 2), 'C'), 
            (LinkedList.create(['A', 'B', 'C', 'D', 'E'], -1), None)]
        for i, o in cases: 
            self.assertEqual(solution(i), o)

if __name__ == '__main__': 
    unittest.main()
