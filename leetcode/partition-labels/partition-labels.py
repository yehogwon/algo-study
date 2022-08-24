# solved
class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        # Compute the index of last element of each element
        last: Dict[str, int] = {k: v for v, k in enumerate(s)} # O(n)

        result = []
        j = anchor = 0 # anchor is a kind of factor of calibration
        for i, c in enumerate(s): 
            j = max(j, last[c])
            if i == j: 
                result.append(i - anchor + 1)
                anchor = i + 1
        return result
