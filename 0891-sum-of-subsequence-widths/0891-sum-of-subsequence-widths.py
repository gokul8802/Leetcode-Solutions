class Solution:
    def sumSubseqWidths(self, nums: List[int]) -> int:
        nums.sort()
        max_val = min_val = 0
        MOD = 10 ** 9 + 7
        size = len(nums)
        for index, num in enumerate(nums):
            max_val = (max_val + num * pow(2, index, MOD)) % MOD
            min_val = (min_val + num * pow(2, size - index - 1, MOD)) % MOD
        return (max_val - min_val) % MOD