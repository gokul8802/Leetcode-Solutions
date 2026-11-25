import heapq
import math
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        
        #quick select O(n), worst case O(n2)
        def partition(l,r,pivot_index):
		
            #1. move pivot to end
            pivot=points[pivot_index][0]**2 +points[pivot_index][1]**2
            points[pivot_index],points[r]=points[r],points[pivot_index]
            
            #2. now start moving elements less than pivot to left and greater to right
            store_index=l
            for i in range(l,r):
                if (points[i][0]**2+points[i][1]**2)<pivot:
                    points[store_index],points[i]=points[i],points[store_index]
                    store_index+=1
					
            #3. now store_index has the place that pivot should be stored in, swap with pivot elemnted which is stored in index r (last element)
            points[store_index],points[r]=points[r],points[store_index]
            return store_index

        
        def select(l,r,k):
            if l<r:
                pivot_index=random.randint(l,r)
                pivot_index=partition(l,r,pivot_index)
				
                if pivot_index==k:
                    return 
                if pivot_index<k:
                    select(pivot_index+1,r,k)
                else:
                    select(l,pivot_index-1,k)
                

        select(0,len(points)-1,k)
        
        return points[:k]