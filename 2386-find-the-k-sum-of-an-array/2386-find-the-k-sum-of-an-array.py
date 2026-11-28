class Solution:
    def kSum(self, nums: list[int], k: int) -> int:
        # Calculate the maximum sum using all positive numbers
        max_sum = sum(x for x in nums if x > 0)
        # Convert all numbers to their absolute values for easier processing
        nums = sorted(abs(x) for x in nums)

        # Priority queue to track the largest sums (negative for max-heap simulation)
        pq = [(-max_sum, 0)]
        
        # Variable to store the current kth largest sum
        result = max_sum

        # Extract the kth largest sum
        for _ in range(k):
            # Pop the largest sum from the priority queue
            result, index = heappop(pq)
            result = -result  # Convert back to positive

            # If possible, add the next subsequence sums to the priority queue
            if index < len(nums):
                heappush(pq, (-(result - nums[index]), index + 1))
                if index > 0:
                    heappush(pq, (-(result - nums[index] + nums[index - 1]), index + 1))

        return result