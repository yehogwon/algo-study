# solved
class Solution:
    def countVowelPermutation(self, n: int) -> int:
        dp = [[0] * 5] * (n + 1)
        def recursion(num): 
            # a = e + i + u
            # e = a + i
            # i = e + o
            # o = i
            # u = i + o
            if num == 1: 
                return [1] * 5
            if num == 2: 
                return [3, 2, 2, 1, 2]
            if dp[num][0] == 0: 
                _a, _e, _i, _o, _u = recursion(num - 1)
                dp[num] = [_e + _i + _u, _a + _i, _e + _o, _i, _i + _o]
            return dp[num]
        return sum(recursion(n)) % (10 ** 9 + 7)