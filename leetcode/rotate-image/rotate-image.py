# solved
class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        
        N = len(matrix)
        
        # transpose
        for i in range(N): 
            for j in range(i): 
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
        
        # flip
        for i in range(N): 
            for j in range(N // 2): 
                matrix[i][j], matrix[i][N - 1 - j] = matrix[i][N - 1 - j], matrix[i][j]
        