# solved
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        def binary_search(l: List[int], s: int, e: int):
            if s > e: 
                return -1
            mid = s + (e - s) // 2
            if l[mid] == target: 
                return mid
            elif l[mid] > target: 
                return binary_search(l, s, mid - 1)
            else: 
                return binary_search(l, mid + 1, e)
        for row in matrix: # O(nlogn)
            if row[0] <= target and target <= row[-1]: 
                _search = binary_search(row, 0, len(row) - 1)
                if _search != -1: 
                    return True
        return False
