import unittest
from typing import List, Tuple


def solution(matrix: List[List[int]]) -> List[List[int]]: 
    M, N = len(matrix), len(matrix[0]) # M: height, N: width
    left, top = False, False
    for i in range(M): 
        if matrix[i][0] == 0: 
            left = True
            break
    for j in range(N): 
        if matrix[0][j] == 0: 
            top = True
            break
    for i, row in enumerate(matrix): 
        for j, val in enumerate(row): 
            if val == 0: 
                matrix[i][0] = 0
                matrix[0][j] = 0
                break

    def fill_row(i: int) -> None: 
        for j in range(N): 
            matrix[i][j] = 0
    def fill_column(j: int) -> None: 
        for i in range(M): 
            matrix[i][j] = 0
    
    for i in range(1, M): 
        if matrix[i][0] == 0: 
            fill_row(i)
    for j in range(1, N): 
        if matrix[0][j] == 0: 
            fill_column(j)
    if left: 
        fill_column(0)
    if top: 
        fill_row(0)
    return matrix # it has worked in-place, but it should be returned for the test sake


class SolutionTest(unittest.TestCase):
    def __init__(self, methodName: str, param: Tuple) -> None:
        super().__init__(methodName)
        self.input, self.output = param[0], param[1]
    def test_runs(self): 
        self.assertEqual(solution(self.input), self.output)

if __name__ == '__main__': 
    cases = [
        ([
            [1, 2, 3, 4, 0],
            [6, 0, 8, 9, 10],
            [11, 12, 13, 14, 15],
            [16, 0, 18, 19, 20],
            [21, 22, 23, 24, 25]
        ], [
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0],
            [11, 0, 13, 14, 0],
            [0, 0, 0, 0, 0],
            [21, 0, 23, 24, 0]
        ])
    ] # edit here
    suite = unittest.TestSuite()
    for i, o in cases: 
        suite.addTest(SolutionTest('test_runs', (i, o)))
    unittest.TextTestRunner(verbosity=2).run(suite)
