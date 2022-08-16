# solved
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # mathematically, the answer is (m + n)! / (m!n!)
        # First, let's make the parameters in order. (We want them to be the case that m > n)
        if m < n: 
            m, n = n, m
        answer = 1
        for i in range(m, m + n - 1): 
            answer *= i
        for i in range(1, n): 
            answer /= i
        return int(answer)
