from bisect import bisect_right

class Solution:
    def maxTaxiEarnings(self, n: int, rides: list[list[int]]) -> int:
        rides.sort(key=lambda x: x[1])
        ends = []
        dp = []
        for start, end, tip in rides:
            earn = end - start + tip
            idx = bisect_right(ends, start) - 1
            if idx >= 0:
                earn += dp[idx]
            if dp:
                dp.append(max(dp[-1], earn))
            else:
                dp.append(earn)
            ends.append(end)
        return dp[-1] if dp else 0