def solution(url: str, true_length: int) -> str: 
    url = list(url) # In python, string doesn't support index manipulation. 
    
    # replace a single space with "%20"
    spaces = len(''.join(url).split()) - 1 # find the number of spaces in the url
    idx = true_length + spaces * 2
    for i in range(true_length - 1, -1, -1): 
        if url[i] == ' ': 
            url[idx-3:idx] = ['%', '2', '0']
            idx -= 3
        else: 
            url[idx - 1] = url[i]
            idx -= 1
    return ''.join(url) # in-place, but return it to print

if __name__ == '__main__': 
    print(solution("Mr John Smith    ", 13))
