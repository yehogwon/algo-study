import sys
sys.path.append(sys.path[0] + '/../../../library/python')

from typing import Any, List, Tuple
import unittest


from linear import LinkedList, Node

def solution(head1: Node, head2: Node) -> Node: 
    # find the length of each linked list
    l1, l2 = 0, 0
    cursor = head1
    while cursor: # O(A)
        l1 += 1
        cursor = cursor.next
    cursor = head2
    while cursor: # O(B)
        l2 += 1
        cursor = cursor.next
    # find the difference in length
    long = head1 if l1 > l2 else head2
    short = head2 if l1 > l2 else head1
    diff = abs(l1 - l2)
    
    # move the longer linked list by the difference in length
    while diff > 0: # O(|A - B|)
        long = long.next
        diff -= 1
    # find the intersection
    while long != short and long and short: # O(|A - B|)
        long = long.next
        short = short.next
    return long


class SolutionTest(unittest.TestCase):
    def __init__(self, methodName: str, param: Tuple) -> None:
        super().__init__(methodName)
        self.input, self.output = param[0], param[1]
    def test_runs(self): 
        sol = solution(*self.input)
        if not self.output: 
            self.assertIsNone(sol)
        else: 
            self.assertEqual(list(sol) if sol is None else sol.tolist(), self.output.tolist())

def __make_cases() -> List[Tuple[Tuple[Node, Node], Node]]: 
    def connect_vals(vals_list: List[List[Any]]) -> Node: 
        lls = []
        for vals in vals_list: 
            ll = LinkedList()
            for val in vals:
                ll.add(val)
            lls.append(ll.head)
        return lls

    lls_val: List[List[int]] = [
        [
            [1, 2, 3, 4, 5], # case 1
            [1, 2, 3, 4, 5], 
            [1, 2, 3, 4, 5]
        ], 
        [
            [1, 2, 3, 4, 5], # case 2
            [10, 2, 3, 4, 5], 
            [2, 3, 4, 5]
        ], 
        [
            [1, 2, 3], # case 3
            [4, 5], 
            []
        ],
        [
            [1, 2, 5, 6, 7], # case 4
            [10, 8, 3, 4, 5, 6, 7], 
            [5, 6, 7]
        ]
    ]

    lls = [connect_vals(vals) for vals in lls_val]
    return [((case[0], case[1]), case[2]) for case in lls]

if __name__ == '__main__': 
    cases: List[Tuple[Tuple[Node, Node], Node]] = __make_cases() # edit here

    suite = unittest.TestSuite()
    for i, o in cases: 
        suite.addTest(SolutionTest('test_runs', (i, o)))
    unittest.TextTestRunner(verbosity=2).run(suite)
