def solution(string: str) -> bool: 
    string = string.lower().replace(' ', '')
    def get_alpha(c: str) -> int: 
        return ord(c) - ord('a')
    odd = 0
    count = [0] * 26
    for c in string: 
        print(c, odd)
        alpha = get_alpha(c)
        count[alpha] += 1
        if count[alpha] % 2 != 0: 
            odd += 1
        else: 
            odd -= 1
    return odd <= 1

if __name__ == '__main__': 
    print(solution('Tact Coa'))
