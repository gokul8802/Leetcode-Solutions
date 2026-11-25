class Solution:
    def visiblePoints(self, points: List[List[int]], angle: int, location: List[int]) -> int:
        Lx, Ly = location
        angles = []
        same = 0
        # populate the angles array with angles relative to our position
        for x, y in points:
            # my current location is the same as this point
            if Lx - x == 0 and Ly - y == 0:
                same += 1
                continue
            # atan2 gives you a result in radians - convert to degrees
            angle_radians = math.atan2(y-Ly, x-Lx)
            angle_degrees = math.degrees(angle_radians)
            # make sure the angle is positive
            if angle_degrees < 0:
                angle_degrees += 360
            # add this angle (in deegrees, >0)
            angles.append(angle_degrees)

        # case 1: no angles, meaning all points were at same location
        if not angles:
            return same

        # in order to do this with a sliding window, we must sort
        angles.sort()

        # extend the angles array to consider full circle (not arc)
        # this is to handle a special wrap around case
        extended = angles + [a + 360 for a in angles]

        window = deque()
        maxPoints = float('-inf')

        # go through angles with a sliding window approach
        for a in extended:
            window.append(a)
            # if the current window is wider than the angle, adjust
            while (window[-1] - window[0]) > angle:
                window.popleft()
            # at this point we have a valid window, calculate max
            maxPoints = max(maxPoints, len(window))
        
        # if this is true, we know the max window includes every point
        if maxPoints > len(angles):
            maxPoints = len(angles)
        
        return maxPoints + same