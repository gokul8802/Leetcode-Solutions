class Solution(object):
    def maximumBags(self, capacity, rocks, additionalRocks):
        """
        :type capacity: List[int]
        :type rocks: List[int]
        :type additionalRocks: int
        :rtype: int
        """
        needed = [c - r for c, r in zip(capacity, rocks)]
        needed.sort()

        full_bags = 0
        for n in needed:
            if additionalRocks >= n:
                additionalRocks -= n
                full_bags += 1
            else:
                break

        return full_bags