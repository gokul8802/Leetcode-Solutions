class Solution(object):
    def smallestTrimmedNumbers(self, nums, queries):
        """
        :type nums: List[str]
        :type queries: List[List[int]]
        :rtype: List[int]
        """
        ans = []
        for k, trim in queries:
            trimmed_list = []
            for i, num in enumerate(nums):
                trimmed_list.append((num[-trim:], i))
            trimmed_list.sort()
            ans.append(trimmed_list[k - 1][1])
        return ans