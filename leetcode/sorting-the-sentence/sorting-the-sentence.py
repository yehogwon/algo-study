# solved
class Solution:
    def sortSentence(self, s: str) -> str:
        words = s.split()
        lookup = {}
        for i, word in enumerate(words): 
            j = len(word) - 1
            while j > 0: 
                if not word[j].isnumeric(): 
                    break
                j -= 1
            lookup[int(word[j + 1:])] = word[:j + 1]
        
        result = ''
        for i in range(1, len(words) + 1): 
            result += lookup[i] + ' '
        return result[:-1]
