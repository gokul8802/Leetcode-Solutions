class Solution:
    def earliestFullBloom(self, plantTime, growTime):
        # Combine plantTime and growTime into a list of tuples
        seeds = list(zip(plantTime, growTime))
        
        # Sort seeds by growTime in descending order (largest growTime first)
        seeds.sort(key=lambda x: x[1], reverse=True)
        
        # Track the total plant time and the latest bloom time
        currentDay = 0
        latestBloom = 0
        
        # Process each seed
        for plant, grow in seeds:
            currentDay += plant  # Plant the current seed
            latestBloom = max(latestBloom, currentDay + grow)  # Update the latest bloom day
        
        return latestBloom