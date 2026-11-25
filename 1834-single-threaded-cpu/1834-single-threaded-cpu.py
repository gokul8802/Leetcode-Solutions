import heapq

class Solution:

    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        n = len(tasks)

        ev = [(e, p, i) for i, (e, p) in enumerate(tasks)]
        ev.sort()

        heap = []
        ans = []
        time = 0
        i = 0

        while i < n or heap:

            if not heap:
                time = max(time, ev[i][0])

            while i < n and ev[i][0] <= time:
                e, p, idx = ev[i]
                heapq.heappush(heap, (p, idx))
                i += 1

            p, idx = heapq.heappop(heap)

            ans.append(idx)
            time += p

        return ans