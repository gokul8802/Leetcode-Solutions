class Solution(object):
    def maximumElementAfterDecrementingAndRearranging(self, l):
        l.sort()
        for i in range(len(l)):
            if i==0 :
                if l[i]==1:
                    pass
                else:
                    l[i]=1
            else:
                if abs(l[i]-l[i-1])<=1:
                    pass
                else:
                    l[i]=l[i-1]+1
        return max(l)
        