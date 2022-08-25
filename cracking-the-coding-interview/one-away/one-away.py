def solution(s1: str, s2: str) -> bool: 
    # check if one can be converted two the other one by a single or zero- edit. 
    # The types of edit are as follows: 
    # Insert a character. 
    # Remove a character. 
    # Replace a character. 
    # Let's say that we try to convert s1 to s2
    alphabets = [chr(i) for i in range(ord('a'), ord('z') + 1)]
    _s1, _s2 = list(s1), list(s2)
    if len(_s1) == len(_s2) + 1: # Try to delete a character
        for i in range(len(_s1)): # O(S1)
            if _s1[:i] + _s1[i + 1:] == _s2: 
                return True
    elif len(_s1) == len(_s2) - 1: # Try to insert a character
        for i in range(len(_s1) + 1): # O(S1 * 26) = O(S1) -> practically, it might matter. 
            for c in alphabets: 
                if _s1[:i] + [c] + _s1[i:] == _s2: 
                    return True
    elif len(_s1) == len(_s2): # Try to replace a character
        diff_count = 0
        for i in range(len(_s1)): # O(S1)
            if _s1[i] != _s2[i]: 
                diff_count += 1
                if diff_count > 1: 
                    return False
        if diff_count <= 1: 
            return True
    return False

if __name__ == '__main__': 
    # test_cases = [('pale', 'ple'), ('pales', 'pale'), ('pale', 'bale'), ('pale', 'bake')]
    # answers = [True, True, True, False]
    # print('\n'.join([str(m) for m in list(zip(test_cases, answers, [solution(*param) for param in test_cases]))]))
    print(solution('pales', 'pale'))
