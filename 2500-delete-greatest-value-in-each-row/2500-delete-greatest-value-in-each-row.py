class Solution:
    def deleteGreatestValue(self, grid: List[List[int]]) -> int:

        for i in range(len(grid)): grid[i].sort()   # <-- sort each row

        grid = list(zip(*grid))                     # <-- transpose grid; rows become
                                                    #     cols and cols become rows

        return sum(max(row) for row in grid)        # <-- sum the maxs from each row
                                                    #_________________________________
                                                    #    Example: grid  = [[4,1,2]
                                                    #                      [3,3,1]]

                                                    #  Sort rows: grid  = [[1,2,4]
                                                    #                      [1,3,3]]
                                                    #
                                                    #  Transpose: grid  = [[1,1]  <-- max: 1
                                                    #                      [2,3]  <-- max: 3
                                                    #                      [4,3]] <-- max: 4
                                                    #                                     –––
                                                    #        Sum:              return ––>  8                          
                                                    