class Solution(object):
    def filterRestaurants(self, restaurants, veganFriendly, maxPrice, maxDistance):
        """
        :type restaurants: List[List[int]]
        :type veganFriendly: int
        :type maxPrice: int
        :type maxDistance: int
        :rtype: List[int]
        """
        return [id for id, _, _, _, _ in sorted(
            [r for r in restaurants if (not veganFriendly or r[2]) and r[3] <= maxPrice and r[4] <= maxDistance],
            key=lambda x: (-x[1], -x[0])
        )]