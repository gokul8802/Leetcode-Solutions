class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        result = 0
        costs.sort()
        for cost in costs:
            if coins >= cost:
                result+=1
            coins-=cost
            if coins <= 0:
                break
        return result