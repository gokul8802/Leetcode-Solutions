class Solution:
    def closestRoom(self, rooms: List[List[int]], queries: List[List[int]]) -> List[int]:
        ans = [None] * len(queries)
        queries = sorted([(s, p, i) for i, (p, s) in enumerate(queries)], reverse = True)
        rooms.sort(reverse = True, key = itemgetter(1, 0))
        rms = [-1]    #the -1 helps handle the case when there are no rooms with the right size
        j = 0
        for s, p, i in queries:
            while j < len(rooms) and rooms[j][1] >= s:
                insort(rms, rooms[j][0])
                j += 1
            x = bisect_left(rms,p)
            ans[i] = rms[x - 1] if (x == len(rms) or x != 1 and abs( rms[x - 1] - p) <= abs(rms[x] - p)) else rms[x]
        return ans