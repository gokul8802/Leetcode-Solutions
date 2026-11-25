class Solution:
    def canBeEqual(self, target, arr):
        # Intuition: if sorted arrays match, they contain the same elements
        target.sort()
        arr.sort()
        for i in range(len(target)):
            if target[i] != arr[i]:
                return False
        return True