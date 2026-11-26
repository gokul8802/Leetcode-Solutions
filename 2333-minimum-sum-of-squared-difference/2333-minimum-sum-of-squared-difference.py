class Solution:
    def minSumSquareDiff(self, nums1: list[int], nums2: list[int], k1: int, k2: int) -> int:
        
        k = k1 + k2

        diff = [abs(a - b) for a, b in zip(nums1, nums2)]

        if sum(diff) <= k:
            return 0

        low = 0
        high = max(diff)

        # find smallest possible maximum difference
        while low < high:
            mid = (low + high) // 2

            needed = sum(max(x - mid, 0) for x in diff)

            if needed <= k:
                high = mid
                
            else:
                low = mid + 1

        level = low

        # Operations needed to bring large differences to level
        used = sum(max(x - level, 0) for x in diff)
        remaining = k - used

        ans = 0

        for x in diff:

            # Only reduce values above level
            if x > level:
                x = level

            # Use remaining operations on values at level
            if remaining > 0 and x == level:
                x -= 1
                remaining -= 1

            ans += x * x

        return ans
