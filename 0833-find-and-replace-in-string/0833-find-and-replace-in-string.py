class Solution:
    def findReplaceString(self, s: str, indices: List[int], sources: List[str], targets: List[str]) -> str:    
        result=list(s)
        for begin,src,tgt in zip(indices,sources,targets):
            if s.startswith(src,begin):
                result[begin]=tgt
                for idx in range(begin+1,begin+len(src)):
                    result[idx]=''
        return ''.join(result)