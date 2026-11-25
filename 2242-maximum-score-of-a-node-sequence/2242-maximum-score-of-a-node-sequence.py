import heapq

class Pair:
    def __init__(self, node, score):
        self.node = node
        self.score = score
    def __lt__(self, other):
        return self.score < other.score

class Solution:    
    def maximumScore(self, scores: List[int], edges: List[List[int]]) -> int:
        edgeList = [[] for i in range(len(scores))]
        for edge in edges:
            edgeList[edge[0]].append(Pair(edge[1], -1*scores[edge[1]]))
            edgeList[edge[1]].append(Pair(edge[0], -1*scores[edge[0]]))
            
        for nodeEdges in edgeList:
            heapq.heapify(nodeEdges)
            
        best = -1
        for e in edges:
            n0 = []
            n1 = []
            while(len(edgeList[e[0]])>0 and len(n0)<3):
                x = heapq.heappop(edgeList[e[0]])
                n0.append(x)
            while(len(edgeList[e[1]])>0 and len(n1)<3):
                x = heapq.heappop(edgeList[e[1]])
                n1.append(x)
            
            m0 = [x for x in n0 if x.node!=e[1]]
            m1 = [x for x in n1 if x.node!=e[0]]
            score = scores[e[0]] + scores[e[1]]
            
            if(len(m0)!=0 and len(m1)!=0):
                if(m0[0].node==m1[0].node):
                    if(len(m0)>1 and len(m1)==1):
                        score += scores[m0[1].node] + scores[m1[0].node]
                        best = max(best, score)
                    elif(len(m0)==1 and len(m1)>1):
                        score += scores[m0[0].node] + scores[m1[1].node]
                        best = max(best, score)
                    elif(len(m0)>1 and len(m1)>1):
                        score += scores[m0[0].node] + max(scores[m0[1].node], scores[m1[1].node])
                        best = max(best, score)
                else:
                    score += scores[m0[0].node] + scores[m1[0].node]
                    best = max(best, score)
            
            for n in n0:
                heapq.heappush(edgeList[e[0]], n)
            for n in n1:
                heapq.heappush(edgeList[e[1]], n)


        return best