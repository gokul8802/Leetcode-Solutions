class Solution:
    def findLHS(self, nums: list[int]) -> int:
        s=sorted(list(set(nums)))
        l=len(s)
        a=[]
        for i in range(l-1,0,-1):
            j=i-1
            if s[i]-s[j]==1:
                a.append(nums.count(s[i])+nums.count(s[j]))
        if len(a)!=0:
            return max(a)
        return 0