class Solution:
    def absDifference(self, arr: list[int], k: int) -> int:
        arr.sort()
        smallSum = sum(arr[:k])      
        largeSum = sum(arr[-k:])    
        return abs(largeSum - smallSum)
