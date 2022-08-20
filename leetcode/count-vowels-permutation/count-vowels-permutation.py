# solved
class Solution:
    def countVowelPermutation(self, n: int) -> int:
        dp = {'a': 1, 'e': 1, 'i': 1, 'o': 1, 'u': 1}
        for i in range(2, n + 1): 
            dp = {
                'a': dp['e'] + dp['i'] + dp['u'], 
                'e': dp['a'] + dp['i'],
                'i': dp['e'] + dp['o'], 
                'o': dp['i'], 
                'u': dp['i'] + dp['o']
            }
        return sum(dp.values()) % (10 ** 9 + 7)
