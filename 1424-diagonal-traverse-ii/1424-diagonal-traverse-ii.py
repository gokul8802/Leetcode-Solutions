class Solution:
    def findDiagonalOrder(self, a: List[List[int]]) -> List[int]:
        return [v for _,_,v in sorted((i+j,j,v) for i,r in enumerate(a) for j,v in enumerate(r))]