# solved
class Solution:
    def finalValueAfterOperations(self, operations: List[str]) -> int:
        x = 0
        for cmd in operations: 
            if cmd in ['++X', 'X++']: 
                x += 1
            else: 
                x -= 1
        return x
