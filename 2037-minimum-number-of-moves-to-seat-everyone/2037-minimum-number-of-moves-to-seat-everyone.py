class Solution:
    def minMovesToSeat(self, bs: List[int], cs: List[int]) -> int:
        return sum(abs(b - c) for b, c in zip(sorted(bs), sorted(cs)))