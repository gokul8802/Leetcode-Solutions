class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        nums.sort() 
        res=set()
        l,r=0,1
        #firt sort the array and use two pointer method
        while(r<len(nums)):
            while(r<len(nums) and nums[r]-nums[l]<k): #difference between two number is <k then increment right pointer
                r+=1
            
            if r<len(nums) and  nums[r]-nums[l]==k: #if difference between two number is exactly to k add pair to set and increment both pointer
                res.add((nums[r],nums[l]))
                l+=1
                r=r+1
                continue
            
            while(r<len(nums) and l<r and nums[r]-nums[l]>k): #increment left pointer if difference is > k
                l+=1
            
            if l==r: #if pointer are overlapping increment right pointer so that i!=j condition satisfied
                r+=1
        

        return len(res)

        