class Solution:
    def __init__(self, n: int, blacklist: List[int]):
        self.blacklist = sorted(blacklist)
        self.max = n - len(blacklist)

    def pick(self) -> int:
        v = random.randint(0, self.max-1)
        l, r = 0, len(self.blacklist) - 1
        while l <= r:
            m = (l+r)//2
            if self.blacklist[m] <= v+m:
                l = m+1
            else:
                r = m-1
        return v + r + 1