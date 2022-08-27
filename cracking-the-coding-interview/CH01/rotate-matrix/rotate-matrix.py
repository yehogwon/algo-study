from typing import List


def solution(matrix: List[List[int]]) -> List[List[int]]: 
    N = len(matrix)
    
    for i in range(N): # O(n^2) : transpose
        for j in range(i): 
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
    
    for i in range(N): # O(n^2) : flip
        for j in range(N // 2): 
            matrix[i][j], matrix[i][N - 1 - j] = matrix[i][N - 1 - j], matrix[i][j]
    return matrix # in-place, but should be returned though

if __name__ == '__main__': 
    print(solution([
        [1, 2, 3, 4, 5],
        [6, 7, 8, 9, 10],
        [11, 12, 13, 14, 15],
        [16, 17, 18, 19, 20],
        [21, 22, 23, 24, 25]]))
