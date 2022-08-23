# solved
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        def gen(left: int, opened: int, cur: str): 
            if left < opened: 
                return []
            if left == 0: 
                return [cur]
            _comb = []
            if opened > 0: 
                _comb += gen(left - 1, opened - 1, cur + ')')
            _comb += gen(left - 1, opened + 1, cur + '(')
            return _comb
        return gen(n * 2, 0, '')
