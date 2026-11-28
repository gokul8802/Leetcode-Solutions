class Solution:
    def maximizeTheProfit(self, n: int, offers: List[List[int]]) -> int:
        # Group offers by the house where they end
        ends_at = [[] for _ in range(n)]

        for s, e, g in offers:
            ends_at[e].append((s, g))

        # dp[i] = best profit using houses before i
        dp = [0] * (n + 1)

        for e in range(1, n + 1):
            # We can always skip every offer ending here
            dp[e] = dp[e - 1]

            # Try taking each offer that ends at this house
            for s, g in ends_at[e - 1]:
                dp[e] = max(dp[e], dp[s] + g)

        return dp[-1]