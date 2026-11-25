class Solution(object):
    def allCellsDistOrder(self, rows, cols, rC, cC):
        a=[]
        a1=[]
        a3=[]
        for i in range(rows):
            for j in range(cols):
                a.append([i,j])
                a1.append(abs(i-rC)+abs(j-cC))
        for i in range(len(list(set(a1)))):
            for j in range(rows*cols):
                if i==a1[j]  :
                    a3.append(a[j])
        return a3




        