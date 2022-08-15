class Solution:
    def climbStairs(self, n: int) -> int:
        dp = [0] * 50
        def recursion(n: int) -> int: 
            if n <= 3: 
                return n
            elif dp[n] == 0: 
                dp[n] = recursion(n - 1) + recursion(n - 2)
            return dp[n]
        return recursion(n)
