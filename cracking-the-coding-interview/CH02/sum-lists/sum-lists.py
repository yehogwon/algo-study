from typing import Union, List
import unittest


class Node: 
    def __init__(self, val: Union[None, int, str]=None, next=None) -> None: 
        self.val = val
        self.next = next
    
    def __eq__(self, o) -> bool:
        return self.val == o.val

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

def show_linked_list(root: Node): 
    while root: 
        print(root.val, '->', end=' ')
        root = root.next
    print()

def solution(root1: Node, root2: Node) -> Node: 
    show_linked_list(root1)
    show_linked_list(root2)

    result = Node()
    up = 0
    cur1, cur2, cur = root1, root2, result
    while cur1 or cur2: 
        if not (cur1 and cur2): 
            add = cur1.val if not cur2 else cur2.val
        else: 
            add = cur1.val + cur2.val
        cur.val = (add + up) % 10
        up = (add + up) // 10
        cur1 = cur1.next
        cur2 = cur2.next
        cur.next = Node()
        cur = cur.next
    if up > 0: 
        cur = Node(up)
    show_linked_list(result)
    return result


class TestSolution(unittest.TestCase):
    def test_runs(self): 
        cases = [((LinkedList.create([7, 1, 6]), LinkedList.create([5, 9, 2])), LinkedList.create([9, 1, 2]))]
        for i, o in cases: 
            self.assertEqual(solution(*i), o)

if __name__ == '__main__': 
    unittest.main()
