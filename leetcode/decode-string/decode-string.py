# solved
class Solution:
    def decodeString(self, s: str) -> str:
        coeffs = [] # depth = len(coeffs)
        stack = [''] # depth = len(bunchs), so basically, coeffs and bunchs have the same lengths

        i = 0
        while i < len(s): 
            c = s[i]
            # print(i, c, coeffs, stack)
            if c.isnumeric(): 
                start_n, end_n = i, i + 1
                while s[end_n - 1].isnumeric(): 
                    end_n += 1
                i = end_n - 2
                coeffs.append(int(s[start_n:end_n - 1]))
            elif c == '[': # end stack
                stack.append('')
            elif c == ']': # start stack
                coeff, _m = coeffs.pop(), stack.pop()
                stack[-1] += coeff * _m
            else: # c is a plain character
                stack[-1] += c
            i += 1
        return stack[0]
