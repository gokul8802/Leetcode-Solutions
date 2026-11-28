class Solution(object):
    def answerQueries(self, nums, queries):
        s=sorted(nums)
        a=[]
        for i in queries:
            v=0
            c=0
            for j in s:
                v+=j
                if v>i:
                    break
                c+=1
            a.append(c)
        return a
                        
                
        