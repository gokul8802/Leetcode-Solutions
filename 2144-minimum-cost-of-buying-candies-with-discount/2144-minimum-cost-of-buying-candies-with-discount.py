class Solution:
    def minimumCost(self, cost: List[int]) -> int:
        cost.sort()
        n = len(cost)
        min_cost = 0

        while cost and len(cost) >= 3:
            min_cost += (cost.pop() + cost.pop())
            cost.pop()

        if cost:
            min_cost += sum(cost)

        return min_cost
