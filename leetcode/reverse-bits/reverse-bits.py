def reverseBits(n: int) -> int:
    res = 0
    bit_list = [int(s) for s in str(n)]
    bit_list = ([0] * (32 - len(bit_list)) + bit_list)
    print(''.join([str(s) for s in bit_list])) # convert n to list of the corresponding binary bits
    for i, c in enumerate(bit_list): 
        res += c * (2 ** i)
    return res

print(reverseBits(int('00000010100101000001111010011100')))
