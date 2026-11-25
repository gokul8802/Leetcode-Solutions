from random import randint

class Solution:
    def swap(self, arr, i, j):
        arr[i], arr[j] = arr[j], arr[i]
        
    def quickSelect(self, arr, target, lo, hi):
        while lo < hi:
			# We choose a random element in the range to act as a pivot. It
			# doesn't have to be random for the algorithm to work, but it helps
			# avoid the worst case time complexity of O(n^2).
            self.swap(arr, lo, randint(lo, hi))
            a = lo + 1
            b = hi
            
			# move everything smaller than our pivot to the left, and everything
			# larger to the right.
            while a < b:
                while a < b and arr[a] <= arr[lo]:
                    a += 1
                while a < b and arr[b] > arr[lo]:
                    b -= 1
                self.swap(arr, a, b)
			
			# Make sure we are going to place the pivot in the right spot.
            if arr[a] > arr[lo]:
                a -= 1
            self.swap(arr, a, lo)
            
			# Decide whether to go into the left partition or the right
			# partition.
            if a < target:
                lo = a + 1
            else:
                hi = a - 1

    def trimMean(self, arr: List[int]) -> float:
        n = len(arr)
        forget = n // 20
		
		# move the small values to the left
        self.quickSelect(arr, forget, 0, n - 1)
		# move the large values to the right
        self.quickSelect(arr, n - forget, forget, n - 1)
        
		# average the rest
        return sum(arr[forget:-forget]) / (n - 2 * forget)