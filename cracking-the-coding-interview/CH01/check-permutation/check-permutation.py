# using an additional data structure
def solution(s1: str, s2: str) -> bool: 
    if len(s1) != len(s2): 
        return False
    
    def get_alpha(c: str) -> int: 
        return ord(c) - ord('a')
    s1_count = [0] * 26
    for c in s1: # O(n)
        s1_count[get_alpha(c) - 1] += 1
    s2_count = [0] * 26
    for c in s2: # O(n)
        s2_count[get_alpha(c) - 1] += 1
    
    for c1, c2 in zip(s1_count, s2_count): # O(1)
        if c1 != c2: 
            return False
    return True

# using sort
def solution(s1: str, s2: str) -> bool: 
    _s1, _s2 = sorted(s1), sorted(s2) # O(n log n)
    return (_s1 == _s2) # O(n)

if __name__ == '__main__': 
    print(solution('asdf', 'dfsa'))
