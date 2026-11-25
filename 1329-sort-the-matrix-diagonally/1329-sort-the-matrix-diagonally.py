class Solution(object):
    def diagonalSort(self, mat):
        rows = len(mat)
        cols = len(mat[0])

        def sortDiagonal(si, sj):
            i, j = si, sj
            diagonal = []
            
            # Step 1: Collect elements along the diagonal
            while i < rows and j < cols:
                diagonal.append(mat[i][j])
                i += 1
                j += 1
                
            # Step 2: Sort collected elements
            diagonal.sort()
            
            # Step 3: Write sorted elements back into the matrix
            i, j, k = si, sj, 0
            while i < rows and j < cols:
                mat[i][j] = diagonal[k]
                i += 1
                j += 1
                k += 1

        # Process diagonals starting along the first column
        sj = 0
        for si in range(1, rows):
            sortDiagonal(si, sj)

        # Process diagonals starting along the first row
        si = 0
        for sj in range(cols):
            sortDiagonal(si, sj)
        
        return mat