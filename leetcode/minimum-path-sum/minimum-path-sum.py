# solved
# iteration
class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        h, w = len(grid), len(grid[0])
        dp = [[0 for _ in range(w)] for _ in range(h)]

        dp[0][0] = grid[0][0]
        for i in range(1, h): # O(h)
            dp[i][0] = grid[i][0] + dp[i - 1][0]

        for j in range(1, w): # O(wh)
            dp[0][j] = grid[0][j] + dp[0][j - 1]
            for i in range(1, h): 
                dp[i][j] = grid[i][j] + min(dp[i - 1][j], dp[i][j - 1])
        return dp[h - 1][w - 1]
# recursion
class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        h, w = len(grid), len(grid[0])
        dp = [[-1 for _ in range(w)] for _ in range(h)]
        def _min(l: list): 
            return min(l) if len(l) > 0 else 0
        def solve(i, j): # (i, j) is the target point
            if dp[i][j] != -1: 
                return dp[i][j]
            candidates = []
            if i > 0: 
                candidates.append(solve(i - 1, j))
            if j > 0: 
                candidates.append(solve(i, j - 1))
            dp[i][j] = _min(candidates) + grid[i][j]
            return dp[i][j]
        return solve(h - 1, w - 1)
