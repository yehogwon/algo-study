s = "3[z]2[2[y]pq4[2[jk]e1[f]]]ef"
'''
3[z]
2
'''
'''
3[z]

2[2[y] pq 4[2[jk] e 1[f]]]

ef
'''

coeffs = [] # depth = len(coeffs)
bunches = [] # depth = len(bunchs), so basically, coeffs and bunchs have the same lengths
result = ''
_keep = False
for i, c in enumerate(s): 
    print(i, c, coeffs, bunches, result)
    if c.isnumeric(): # start of a bunch
        coeff = int(c)
        if _keep: 
            coeffs[-1] = 10 * coeffs[-1] + coeff
        else: 
            coeffs.append(coeff)
            _keep = True
    elif c == '[': 
        _keep = False
    elif c == ']': 
        coeff, bunch = coeffs.pop(), bunches.pop()
        _str = coeff * bunch
        if len(coeffs) > 0: 
            if len(bunches) == 0: 
                bunches.append(_str)
            else: 
                bunches[-1] += _str
        else: 
            result += _str
    else: # just a plain character
        if len(coeffs) > 0: 
            if len(bunches) < len(coeffs): 
                bunches.append('')
            bunches[-1] += c
        else: 
            result += c

print(result)