# solved
class Solution:
    def addBinary(self, a: str, b: str) -> str:
        int_a = [int(i) for i in a][::-1]
        int_b = [int(i) for i in b][::-1]
        
        max_length = max(len(int_a), len(int_b))
        int_a += [0] * (max_length - len(int_a))
        int_b += [0] * (max_length - len(int_b)) # they are in the same length now
        
        sum_list = [(a + b) for a, b in zip(int_a, int_b)]
        
        for i in range(len(sum_list) - 1): 
            if sum_list[i] >= 2: 
                sum_list[i] -= 2
                sum_list[i + 1] += 1
        if sum_list[-1] >= 2: 
            sum_list[-1] -= 2
            sum_list += [1]
        return ''.join([str(i) for i in sum_list[::-1]])
