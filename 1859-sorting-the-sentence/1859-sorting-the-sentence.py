class Solution(object):
    def sortSentence(self, s):
       word = s.split()
       result =[""] * len(word)
       for word in word:
        postion = int(word[-1])
        result[postion - 1] = word[:-1]
        
       return " ".join(result)  
         

        