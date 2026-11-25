from typing import List

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        m1 = m2 = 0

        for num in nums:
            if num > m1:
                m2 = m1
                m1 = num
            else:
                m2 = max(m2, num)

        return (m1 - 1) * (m2 - 1)