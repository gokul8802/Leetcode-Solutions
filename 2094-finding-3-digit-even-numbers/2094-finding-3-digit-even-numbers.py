class Solution:
    def findEvenNumbers(self, digits: List[int]) -> List[int]:
        freq = [0] * 10
        ans = []

        for num in digits:
            freq[num] += 1

        for i in range(1, 10):
            for j in range(10):
                for k in range(0, 9, 2):
                    freq[i] -= 1
                    freq[j] -= 1
                    freq[k] -= 1

                    if freq[i] >= 0 and freq[j] >= 0 and freq[k] >= 0:
                        num = i * 100 + j * 10 + k
                        ans.append(num)

                    freq[i] += 1
                    freq[j] += 1
                    freq[k] += 1

        return ans