# solved
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        min_length = min([len(s) for s in strs])
        
        i = 0
        while i < min_length: 
            _set = set()
            for s in strs: 
                _set.add(s[i])
            if len(_set) > 1: 
                break
            i += 1
            
        return strs[0][:i]
