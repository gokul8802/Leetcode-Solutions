class Solution:
    def minimumTotalDistance(self, R: List[int], F: List[List[int]]) -> int:
        memo = {}
        
        R.sort()
        F.sort()
        rr, ff = len(R), len(F)
        
        def dp(r, f, res):
            if (r, f, res) in memo: 
                return memo[(r, f, res)]
            
			# Edge cases: r = rr, we have finished assigning all robots, return 0;
			# res = 0, the current factory has 0 remaning seats, move to the next factory.
            if r == rr:
                return 0
            if res == 0:
                return dp(r, f + 1, F[f + 1][1]) if f + 1 < ff else math.inf
            
			# Assign the current robot r to the current factory f.
            cur = dp(r + 1, f, res - 1) + abs(R[r] - F[f][0])
			
			# Or assign it to the next factor f + 1, if possible.
            if f + 1 < ff:
                cur = min(cur, dp(r, f + 1, F[f + 1][1]))
                
            memo[(r, f, res)] = cur
            return cur
        
        return dp(0, 0, F[0][1])