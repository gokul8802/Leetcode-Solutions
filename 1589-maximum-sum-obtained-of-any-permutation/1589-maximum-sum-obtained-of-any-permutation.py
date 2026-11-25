class Solution(object):
    def maxSumRangeQuery(self, nums, requests):
        """
        :type nums: List[int]
        :type requests: List[List[int]]
        :rtype: int
        """
        n = len(nums)
        cnt = [0] * n
        for r in requests:
            cnt[r[0]] += 1
            if r[1] + 1 < n:
                cnt[r[1] + 1] -= 1
        curr = 0
        for i in range(n):
            curr += cnt[i]
            cnt[i] = curr
        nums.sort()
        cnt.sort()
        res = 0
        for i in range(n):
            res += nums[i] * cnt[i]
        return res % (10**9 + 7)