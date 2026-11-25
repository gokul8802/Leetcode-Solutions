class Solution:
    def isPossibleDivide(self, nums: List[int], k: int) -> bool:
        if len(nums) % k != 0:
            return False
        
        nums.sort()

        nums_freq = []

        for i in range(len(nums)):
            if len(nums_freq) == 0 or nums[i] != nums_freq[-1][0]:
                nums_freq.append([nums[i], 0])
            nums_freq[-1][1] += 1
        
        i = 0

        # print(nums_freq)

        while i <= len(nums_freq) - k:
            if nums_freq[i][1] == 0:
                i += 1
                continue
            nums_freq[i][1] -= 1
            for j in range(1, k):
                if nums_freq[i+j][0] != nums_freq[i+j-1][0] + 1:
                    return False
                nums_freq[i+j][1] -= 1
                if nums_freq[i+j][1] < 0:
                    return False
        
        # print(nums_freq)

        if nums_freq[-1][1] > 0:
            return False

        return True