# working on it

s = "ababcbacadefegdehijhklij"
print(' -> -> -> -> -> ', len(s))

import math
from time import sleep

####################################################################3

def ok(s1: set, s2: set): 
    _s1, _s2 = set(s1), set(s2)
    return (not (_s1 & _s2)) and len(s1) > 0 and len(s2) > 0

def sep(m: str): # returns a list of strings whosef length is 2
    i = 0
    _check = False
    _again = False
    while True: 
        print(i)
        sleep(0.1)
        if i > len(m) - 1: 
            _again = True
        if _check is True: 
            i += 1
            if not ok(m[:i], m[i + 1:]): 
                break
        else: 
            if ok(m[:i], m[i + 1:]): 
                _check = True
            else: 
                i *= 2
    if _again: 
        i = 1
    if i <= 0: 
        return len(m) - 1
    else: 
        return i - 1

partitions = []
while len(s) > 0: 
    idx = sep(s)
    s = s[idx:]
    partitions.append(idx)
    print(idx, s)
print(partitions)