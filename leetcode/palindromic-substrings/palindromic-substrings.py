# working on it
class Solution:
    def countSubstrings(self, s: str) -> int:
        def check(m: str) -> bool: 
            i, j = 0, len(m) - 1
            while i < j: 
                if m[i] != m[j]: 
                    return False
                i += 1
                j -= 1
            return True
        def make(ori: str, n: int) -> List[str]: 
            _n_palin = 0
            for i in range(len(ori) - n + 1): 
                if check(ori[i:i+n]): 
                    _n_palin += 1
            return _n_palin
        n_palindromes = 0
        for i in range(1, len(s) + 1): 
            n_palindromes += make(s, i)
        return n_palindromes