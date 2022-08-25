# solved
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        def get_alpha(c: str) -> int: 
            return ord(c) - ord('a')
        ransom_count = [0] * 26
        for c in ransomNote: 
            ransom_count[get_alpha(c)] += 1
        magazine_count = [0] * 26
        for c in magazine: 
            magazine_count[get_alpha(c)] += 1
        for rc, mc in zip(ransom_count, magazine_count): 
            if rc > mc: 
                return False
        return True
