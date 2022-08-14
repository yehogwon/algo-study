# solved
class Solution:
    def reverseBits(self, n: int) -> int:
        res = 0
        bit_list = [int(s) for s in bin(n)[2:]]
        bit_list = ([0] * (32 - len(bit_list)) + bit_list)
        for i, c in enumerate(bit_list): 
            res += c * (2 ** i)
        return res