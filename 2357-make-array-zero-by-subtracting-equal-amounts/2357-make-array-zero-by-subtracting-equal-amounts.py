class Solution:
    def minimumOperations(self, nums: List[int]) -> int:        
        # The number of operations is the count of unique positive numbers
        # Each operation removes the current smallest unique positive number
        return len(set(num for num in nums if num != 0))