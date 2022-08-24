from typing import List

# with an extra data structure
def solution(string: str) -> bool: 
    def get_alpha(char: str) -> int: 
        return ord(char) - ord('a')
    count: List[int] = [0] * 26
    for c in string: # O(n)
        alpha_n = get_alpha(c)
        if count[alpha_n] > 0: # O(1)
            return False
        count[alpha_n] += 1
    return True

# without any extra data structure
def solution(string: str): 
    def get_alpha(c: str) -> int: 
        return ord(c) - ord('a')
    check: int = 0
    for c in string: 
        alpha = get_alpha(c)
        if check & (1 << alpha) > 0: 
            return False
        check |= (1 << alpha)
    return True

if __name__ == '__main__': 
    print(solution('abde'))
