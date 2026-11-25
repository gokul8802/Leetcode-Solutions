class Solution:
    def minDifference(self, nums: List[int]) -> int:
        if len(nums) < 5:
            return 0
            
        a, b, c, d, x, y, z, t = inf, inf, inf, inf, -inf, -inf, -inf, -inf
        for num in nums:
            if num < a:
                d, c, b, a = c, b, a, num
            elif num < b:
                d, c, b = c, b, num
            elif num < c:
                d, c = c, num
            elif num < d:
                d = num

            if num > t:
                x, y, z, t = y, z, t, num
            elif num > z:
                x, y, z = y, z, num
            elif num > y:
                x, y = y, num
            elif num > x:
                x = num

        return min(x - a,  y - b,  z - c, t - d)