class Solution:
    def longestSquareStreak(self, nums: List[int]) -> int:

        nums = sorted(set(nums))
        cands = {n for n in nums if n%4 < 2}
        ans = 0

        for n in nums:
            square = n*n
            tally = 1

            while square in cands:
                cands.remove(square)
                tally+= 1
                square*= square

            ans = max(ans, tally)
   
        return ans if ans > 1 else -1