class Solution(object):
    def latestTimeCatchTheBus(self, buses, passengers, capacity):
        """
        :type buses: List[int]
        :type passengers: List[int]
        :type capacity: int
        :rtype: int
        """
        buses.sort()
        passengers.sort()
        pass_set = set(passengers)
        curr_pass_idx = 0
        m = len(passengers)
        pass_on_bus = 0
        
        for bus_time in buses:
            pass_on_bus = 0
            while pass_on_bus < capacity and curr_pass_idx < m and passengers[curr_pass_idx] <= bus_time:
                curr_pass_idx += 1
                pass_on_bus += 1
        
        if pass_on_bus < capacity:
            latest = buses[-1]
        else:
            latest = passengers[curr_pass_idx - 1]
            
        while latest in pass_set:
            latest -= 1
            
        return latest