class Solution(object):
    def numSmallerByFrequency(self, queries, words):
        def f(queries, words):
            q, w = [], []
            for i in queries:
                sc = min(i)
                q.append(i.count(sc))
            for i in words:
                sc = min(i)
                w.append(i.count(sc))
            return [q, w]

        fret = f(queries, words)
        queries, words = fret[0], fret[1]
        ans = []

        for q in queries:
            cnt = 0
            for w in words:
                if q < w:
                    cnt += 1
            ans.append(cnt)
        return ans