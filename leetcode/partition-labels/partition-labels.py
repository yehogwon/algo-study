# working on it
from typing import List

def debug(m: str, bias=True) -> None: 
    if bias: 
        print(m)

def partitionLabels(s: str, log=False) -> List[int]:
    def in_common(s1: str, s2: str) -> bool: # O(n) : returns True if they don't have common elements
        if len(s1) == 0 or len(s2) == 0: 
            return True
        _s1, _s2 = set(s1), set(s2) # O(n)
        return bool(_s1 & _s2) # O(n)
    
    last = {k: v for v, k in enumerate(s)} # O(n)
    def solve(_s, cut=0): # less than O(n)
        debug('solve(): ' + _s + f', cut={cut}', log)
        i = 0
        _flag = False
        while i < len(_s): 
            debug(i, log)
            if _flag: 
                if in_common(_s[:i + 1], _s[i + 1:]): 
                    return [i] + solve(_s[i:], i + cut)
                i += 1
            else: 
                c = _s[i]
                i = last[c] - cut
                _left, _right = _s[:i + 1], _s[i + 1:]
                debug(f'CHECK: {c} -> {i} == {_left}, {_right}', log)
                _check = in_common(_left, _right)
                debug(f'Do they have in common? : ' + _left + ' = ' + _right + ' => ' + str(_check), log)
                if not _check: # If they satisfy
                    _flag = True
                else: # If they don't satisfy
                    break
        return [len(_s)]
    return solve(s, 0)

def test(args, anss, logs): 
    for arg, ans, log in zip(args, anss, logs): 
        print('=' * 15)
        print(partitionLabels(arg, log), ' -> ', ans)

test(["ababcbacadefegdehijhklij", "eccbbbbdec", "eaaaabaaec", "dccccbaabe"], 
    [[9, 7, 8], [10], [9, 1], [1, 4, 4, 1]], [True, False, False, False])
