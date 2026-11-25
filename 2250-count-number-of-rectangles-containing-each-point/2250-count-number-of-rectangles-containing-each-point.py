class Solution(object):
    def countRectangles(self, rectangles, points):
        """
        :type rectangles: List[List[int]]
        :type points: List[List[int]]
        :rtype: List[int]
        """
        rect_by_height = defaultdict(list)
        for l, h in rectangles:
            rect_by_height[h].append(l)

        for h in rect_by_height:
            rect_by_height[h].sort()

        result = []
        for x, y in points:
            count = 0
            for h in range(y, 101):
                if h in rect_by_height:
                    arr = rect_by_height[h]
                    idx = bisect_left(arr, x)
                    count += len(arr) - idx
            result.append(count)

        return result