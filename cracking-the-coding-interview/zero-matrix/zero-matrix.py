import unittest
from typing import List, Tuple


def solution(matrix: List[List[int]]) -> List[List[int]]: 
    M, N = len(matrix), len(matrix[0]) # M: height, N: width
    zeros: List[Tuple[int, int]] = []
    for i, row in enumerate(matrix): 
        for j, val in enumerate(row): 
            if val == 0: 
                matrix[i][j] = -1
    for i, row in enumerate(matrix): 
        for j, val in enumerate(row): 
            for i in range(M): 
                matrix[i][zero_coord[1]] = 0
            for j in range(N): 
                matrix[zero_coord[0]][j] = 0
    return matrix


class TestSolution(unittest.TestCase):
    def test_run(self, i, o): 
        self.assertEqual(solution(i), o)

    def test_runs(self): 
        cases = [
            (
            [[1, 2, 0], 
            [3, 9, 11], 
            [5, 0, 2]], 
            [[0, 0, 0], 
            [3, 0, 0], 
            [0, 0, 0]]
            )
        ]
        for i, o in cases: 
            self.test_run(i, o)

if __name__ == '__main__': 
    unittest.main()
