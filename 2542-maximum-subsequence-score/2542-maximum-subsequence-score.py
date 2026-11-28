import heapq

class Solution:
    def maxScore(self, nums1, nums2, k):
        n = len(nums1)
        
        # Step 1: Sort indices based on nums2 in descending order
        idx = sorted(range(n), key=lambda i: nums2[i], reverse=True)
        
        # Step 2: Min-heap to maintain top k values from nums1
        pq = []
        total_sum = 0
        max_res = 0
        
        # Step 3: Iterate over indices in nums2-descending order
        for i in idx:
            # Push nums1[i] into heap
            heapq.heappush(pq, nums1[i])
            total_sum += nums1[i]
            
            # If more than k elements, remove the smallest
            if len(pq) > k:
                total_sum -= heapq.heappop(pq)
            
            # When we have exactly k elements, compute score
            if len(pq) == k:
                score = total_sum * nums2[i]  # nums2[i] is the current minimum
                max_res = max(max_res, score)
        
        return max_res