class Solution(object):
    def maxScore(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        sm=sum(nums)
        cnt=0
        for i in nums:
            if sm>0:cnt+=1
            sm-=i
        return cnt