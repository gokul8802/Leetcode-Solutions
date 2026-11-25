class Solution(object):
    def intersection(self, nums):
        l=[]
        for i in nums[0]:
            v="t"
            for j in range(1,len(nums)):
                if i not in nums[j]:
                    v="f"
                    break
            if v=="t":
                l.append(i)
        return sorted(l)
            

            
        