# solved
class Solution:
    def romanToInt(self, s: str) -> int:
        n = 0
        lookup = {
            'I': 1, 
            'V': 5, 
            'X': 10, 
            'L': 50, 
            'C': 100, 
            'D': 500, 
            'M': 1000, 
            'IV': 4, 
            'IX': 9,
            'XL': 40, 
            'XC': 90, 
            'CD': 400, 
            'CM': 900
        }
        
        it = enumerate(s)
        for i, c in it: 
            if i == len(s) - 1: 
                n += lookup[c]
            elif s[i:i+2] in lookup: 
                n += lookup[s[i:i+2]]
                next(it)
            else: 
                n += lookup[c]
        return n
