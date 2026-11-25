class Solution:
    def maximumGap(self, nums: List[int]) -> int:
        if len(nums) < 2: return 0
        hi, lo, ans = max(nums), min(nums), 0
        bsize = (hi - lo) // (len(nums) - 1) or 1
        buckets = [[] for _ in range(((hi - lo) // bsize) + 1)]
        for n in nums:
            buckets[(n - lo) // bsize].append(n)
        prevhi = buckets[0][0]
        for b in buckets:
            if not len(b):
                continue
            currlo, currhi = b[0], b[0]
            for n in b: 
                currhi, currlo = max(currhi, n), min(currlo, n)
            ans = max(ans, currlo - prevhi)
            prevhi = currhi
        return ans