class Solution(object):
    def minimumRemoval(self, beans):
        """
        :type beans: List[int]
        :rtype: int
        """
        beans.sort()
        total = sum(beans)
        n = len(beans)

        return min(total - beans[i] * (n - i) for i in range(n))