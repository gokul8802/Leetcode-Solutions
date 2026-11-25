class Solution:
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
        freq = Counter(arr)
        heap = list(freq.values())

        heapq.heapify(heap)

        while heap and k >= heap[0]:
            k -= heapq.heappop(heap)

        return len(heap)