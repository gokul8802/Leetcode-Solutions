class Solution:
    def get_subset_sums(self, A: List[int]):
        result = set()
        n = len(A)
        limit = (1 << n)
        # Going through all the combinations generated
        for msk in range(limit):
            s = 0
            # Going through the length of the array
            for j in range(0, n):
                # Check if the i'th bit is set, to choose the element from the array
                if msk & (1 << j):
                    s += A[j]
            result.add(s)
        return result
            
        
    def minAbsDifference(self, A: List[int], goal: int) -> int:        
        n = len(A)
        half = n >> 1
        A1, A2 = A[ :half], A[half:]
        s1, s2 = self.get_subset_sums(A1), self.get_subset_sums(A2)
        s2 = sorted(s2)

        
        # Note: s1, s2 are representations of what elements we are selecting from A1, A2
        # let x be the sum we select from s1
        # let y be the sum we select from s2
        # So x + y = sum should be as close to the goal as possible
        #   x (s1) + y (s2) == sum
        # so that - abs(sum - goal) is as minimum as possible
        
        # Hence for every value 'y' in s2, we search for a value 'x' in s1
        # such that x + y is almost goal  - only then sum-goal is as small as possible.
        # So we search "goal-y" in s1
        
        ans = float('inf')
                
        for s in s1:
            remain = goal - s
			# binary search for the value in s2 that's closest to the remaining value
            i2 = bisect_left(s2,remain)
            if i2 < len(s2):
                ans = min(ans, abs(remain - s2[i2]))
            if i2 > 0:
                ans=min(ans,abs(remain- s2[i2-1]))
        return ans