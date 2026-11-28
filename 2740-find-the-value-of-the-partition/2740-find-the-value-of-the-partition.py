class Solution(object):
    def findValueOfPartition(self, nums):
        nums.sort()

        ans, n = 1e9, len(nums)
        for i in range(n-1):
            ans = min(ans, nums[i+1] - nums[i])
        return ans