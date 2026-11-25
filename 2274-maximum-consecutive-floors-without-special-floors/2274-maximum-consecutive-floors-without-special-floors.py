class Solution:
    def maxConsecutive(self, bottom: int, top: int, special: List[int]) -> int:
        
        special = sorted(special)
        
        c1 = special[0]-bottom
        c2 = top-special[-1]
        
        max_C3 = 0
        for element in range(1,len(special)):
            c3 = (special[element]-special[element-1])-1
            max_C3 = max(max_C3,c3)
      
        
        
        return max(max_C3,c1,c2)