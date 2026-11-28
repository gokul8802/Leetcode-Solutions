class Solution:
    def distinctAverages(self, nums: list[int]) -> int:
        nums.sort() 

        left, right = 0, len(nums) - 1
        averages = set()

        while left < right:
            averages.add(nums[left] + nums[right])

            left += 1
            right -= 1

        return len(averages)