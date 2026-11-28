class Solution:
    def countWays(self, ranges: List[List[int]]) -> int:

        mx, count = -1, 0

        for beg, end in sorted(ranges):
            count+= (beg > mx)
            mx = max(end, mx)

        return pow(2, count, 1_000_000_007)