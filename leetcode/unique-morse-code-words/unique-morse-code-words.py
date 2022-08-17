# solved
class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        def get_morse_char(c: str): 
            assert len(c) == 1
            LOOKUP = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
            return LOOKUP[ord(c) - ord('a')]
        
        def get_morse_str(m: str): 
            return ''.join([str(get_morse_char(_c)) for _c in m])
        
        _set = set()
        for word in words: 
            _set.add(get_morse_str(word))
        return len(_set)
