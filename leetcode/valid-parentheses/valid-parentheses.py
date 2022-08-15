# solved
class Solution:
    def isValid(self, s: str) -> bool:
        def open_to_close(s: str): 
            if s == '(': 
                return ')'
            elif s == '[': 
                return ']'
            elif s == '{': 
                return '}'
        
        stack = []
        for c in s: 
            if c in ['(', '[', '{']: # in the case of opening
                stack.append(c)
            else: # in the case of closing
                try: 
                    top = stack.pop()
                    if c != open_to_close(top): 
                        return False
                except: 
                    return False
        return len(stack) == 0
        