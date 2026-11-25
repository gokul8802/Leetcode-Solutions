class Solution:
    def checkIfExist(self, arr: list[int]) -> bool:
        n = len(arr)

        def BS(arr, target, i):
            low = 0
            high = len(arr) - 1

            while low <= high:
                mid = (low + high) // 2

                if arr[mid] == target and mid != i:
                    return True
                elif arr[mid] < target:
                    low = mid + 1
                else:
                    high = mid - 1

            return False

        arr.sort()

        for i in range(n):
            if BS(arr, arr[i] * 2, i):
                return True

        return False