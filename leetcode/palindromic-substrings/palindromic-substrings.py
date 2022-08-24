# solved
class Solution:
    def countSubstrings(self, s: str) -> int:
        lookup = {k: v for k, v in zip(list(s), [True] * len(s))}
        def check(m: str) -> bool: 
            assert len(m) > 0, 'length of m must be greater than zero'
            lookup[m] = m[0] == m[-1] and lookup[m[1:-1]]
            return lookup[m]
        count = len(s)
        lookup[''] = True
        for i in range(2, len(s) + 1): # O(n) : iterate from 2 to len(s), inclusively <- length
            for j in range(0, len(s) - i + 1): 
                if check(s[j:j+i]): 
                    count += 1
        return count
