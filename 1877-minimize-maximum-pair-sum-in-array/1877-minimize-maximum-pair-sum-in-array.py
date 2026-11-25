class Solution:
    def minPairSum(self, nums: List[int]) -> int:
        nums.sort()
        n = len(nums)
        mx = 0

        for i in range(n // 2):
            mx = max(mx, nums[i] + nums[n - i - 1])

        return mx