class Solution:
    def gcdSort(self, nums: List[int]) -> bool:
        sortedNums = sorted(nums)
        s = set(nums)
        
	    # UFDS
        UF = {num:num for num in nums}
        def find(x):
            if x != UF[x]:
                UF[x] = find(UF[x])
            return UF[x]
        def union(x, y):
            UF[find(x)] = find(y)
        
	    # SieveOfErathosthenes
        prime = [True for _ in range(100001)]
        for p in range(2, 100001):
            if prime[p]:
                prev = -1
                for j in range(p, 100001, p):
                    if j in s:
                        if prev == -1:
                            prev = j
                        union(prev, j)
                    prime[j] = False
        
        for i in range(len(nums)):
            if find(nums[i]) != find(sortedNums[i]):
                return False
        
        return True