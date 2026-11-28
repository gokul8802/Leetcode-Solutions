class Solution:
    def topStudents(self, positive_feedback: List[str], negative_feedback: List[str], report: List[str], student_id: List[int], k: int) -> List[int]:
        # converting the both positive_feedback and negative_feedback for fast accessing.
        pos= set(positive_feedback)
        neg= set(negative_feedback)
        d={}   #dictionary to store every student points 


        for i in range(len(report)):
            pts=0
            lst=report[i].split()
            for j in lst:
                if j in pos:    # if positive feedback
                    pts+=3
                if j in neg:    # if negative feedback
                    pts-=1
            d[student_id[i]]=pts  #storing the final points
        
        #sorting the dictionary accoring to max points
        final_lst=list(sorted(d.items(),key=lambda x : (x[-1],-x[0]),reverse=True))   
        ans=[]  #to store final answer
        for i in range(k):
            ans.append(final_lst[i][0])
        return ans
                    