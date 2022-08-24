def solution(url: str, true_length: int) -> str: 
    url = list(url) # In python, string doesn't support index manipulation. 
    
    # replace a single space with three contiguous spaces
    spaces = len(''.join(url).split()) - 1 # find the number of spaces in the url
    i = true_length - 1
    while spaces > 0: # O(n)
        print(i, url)
        if url[i] == ' ': 
            spaces -= 1
        else: 
            url[i + spaces * 2] = url[i]
            url[i] = ' '
        i -= 1
    # replace three contiguous spaces to %20
    i = 0
    while i < len(url) - 2: # O(n)
        if url[i:i + 3] == [' '] * 3: 
            url[i:i + 3] = '%20'
        i += 1
    return ''.join(url) # in-place, but return it to print

if __name__ == '__main__': 
    print(solution("Mr John Smith    ", 13))
