class Solution:
    def minimumDifference(self, nums: List[int]) -> int:
        n, n2, res = len(nums) // 2, len(nums) // 4, inf
        def dfs(i: int, end: int, k: int, s: int, sums: List[List[int]]):
            if i == end or k >= n2:
                sums[k].append(s)
                return sums
            return (dfs(i + 1, end, k, s, sums), dfs(i + 1, end, k + 1, s + nums[i], sums))[0]
        sum1, sum2 = sum(nums[:n]), sum(nums[n:])
        s1 = dfs(0, n, 0, 0, [[] for _ in range(n2 + 1)])
        s2 = dfs(n, n * 2, 0, 0, [[] for _ in range(n2 + 1)])
        for k in range(n2 + 1):
            s2[k].sort()
            for s1k in s1[k]:
                comp, diff = (sum1 + sum2) // 2 - (sum1 - s1k), sum1 - sum2 - s1k * 2
                j = bisect.bisect_left(s2[k], comp)
                if j < len(s2[k]):
                    res = min(res, abs(diff + s2[k][j] * 2))
                if j > 0:
                    res = min(res, abs(diff + s2[k][j - 1] * 2))
        return res