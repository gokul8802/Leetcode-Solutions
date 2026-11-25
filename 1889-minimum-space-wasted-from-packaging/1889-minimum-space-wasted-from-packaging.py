class Solution:
    # idea:
    #   1. sort packages, so we can process them from smaller to bigger size
    #   2. push boxes to heap (min priority queue), so that when we process all packages
    #       with smaller size than the heap top, we will be able to compute waste space
    #   3. heap element will have form of (size, i, j) that's boxes[i][j] = size
    #   example:
    #       heaptop is (5, i, j)
    #       we processed 3 packages with sizes 2, 3 and 5, the fourth package has size of 6
    #       package_count = 3 (number of packages)
    #       total_box_size = 3 (package_count) * 5 (box_size) = 15
    #       so write: cache[i] = (3, 15) as (package_count, total_box_size)
    #
    #       when we update: cache[i] = [package_count, cache[i][1] + box_size * (package_count - cache[i][0])]
    
    def minWastedSpace(self, packages: List[int], boxes: List[List[int]]) -> int:
        packages.sort()
        h = []
        for i in range(len(boxes)):
            for box in boxes[i]:
                heappush(h, (box, i))

        package_count = 0
        cache = [[0, 0] for _ in boxes]
        while h:
            while package_count < len(packages) and h[0][0] >= packages[package_count]:
                package_count += 1
            
            size, box_index = heappop(h)
            cache[box_index][1] += size * (package_count - cache[box_index][0])
            cache[box_index][0] = package_count

        if package_count == len(packages):
            total_package_size = sum(packages)
            return min(total_box_size - total_package_size for box_count, total_box_size in cache if box_count == package_count) % (10 ** 9 + 7)
        else:
            return -1