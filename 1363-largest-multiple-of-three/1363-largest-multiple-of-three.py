import numpy as np

class Solution:
    def largestMultipleOfThree(self, digits: List[int]) -> str:
        # 1. Frequency Vectorization (The Basis)
        counts = np.zeros(10, dtype=np.int32)
        unique, c = np.unique(digits, return_counts=True)
        counts[unique] = c
            
        v1_idx = np.array([1, 4, 7])
        v2_idx = np.array([2, 5, 8])
        
        sum_v1 = counts[v1_idx].sum()
        sum_v2 = counts[v2_idx].sum()
        total_rem = (sum_v1 + 2 * sum_v2) % 3
        
        # 2. Fully Vectorized Symmetric Reduction
        def vectorized_remove(target_indices, k):
            c_subset = counts[target_indices]
            # Calculate prefix sums to find the 'cut point'
            pref = np.cumsum(c_subset)
            # Find how many to remove from each index in one shot
            to_remove = np.zeros_like(c_subset)
            
            # Logic: If pref[i] < k, remove all at that index. 
            # If it's the first index where pref[i] >= k, remove (k - pref[i-1]).
            to_remove[0] = min(c_subset[0], k)
            if len(target_indices) > 1:
                to_remove[1:] = np.clip(k - pref[:-1], 0, c_subset[1:])
            
            counts[target_indices] -= to_remove

        if total_rem == 1:
            if sum_v1 >= 1: vectorized_remove(v1_idx, 1)
            else:          vectorized_remove(v2_idx, 2)
        elif total_rem == 2:
            if sum_v2 >= 1: vectorized_remove(v2_idx, 1)
            else:          vectorized_remove(v1_idx, 2)
                
        # 3. String Synthesis via Vectorized Repetition
        # Sort descending for the largest value
        res = "".join(str(i) * counts[i] for i in range(9, -1, -1))
        
        if res.startswith('0'):
            return '0' if '0' in res else ""
        return res  