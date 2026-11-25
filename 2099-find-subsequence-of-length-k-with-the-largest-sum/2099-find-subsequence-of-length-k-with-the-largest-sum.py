class Solution:
    def maxSubsequence(self, nums: List[int], k: int) -> List[int]:
        minheap = []
        # Use minheap to store the k largest values as we iterate nums
        for idx, val in enumerate(nums):
            if len(minheap) < k:
                heappush(minheap, (val, idx))
            else:
                if val > minheap[0][0]:
                    heappop(minheap)
                    heappush(minheap, (val, idx))
            
        # Sort minheap by index and put every value into ans array in order of index
        ans = []
        minheap.sort(key=lambda x: x[1])
        for val, _ in minheap:
            ans.append(val)
        
        return ans