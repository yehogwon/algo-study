# solved
import math

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        global source
        source = nums[:]
        def binary_search(head, tail, target): 
            # head and tail are the indicies
            global source

            mid = math.ceil(tail + (head - tail) / 2)
            if (head > tail): 
                return head
            elif source[mid] == target: 
                return mid
            elif (source[mid] > target): 
                return binary_search(head, mid - 1, target)
            else: 
                return binary_search(mid + 1, tail, target)
        return binary_search(0, len(source) - 1, target)
        