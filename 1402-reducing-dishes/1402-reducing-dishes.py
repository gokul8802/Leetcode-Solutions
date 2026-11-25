class Solution:
    def maxSatisfaction(self, satisfaction: List[int]) -> int:
        
		# sort largest to smallest
        satisfaction.sort(reverse=True)
        
        runningSum = 0
        result = 0
        for val in satisfaction:
            runningSum += val
			# if it's no longer beneficial to serve the next dish
            if runningSum < 0:
                break
            result += runningSum
        
        return result