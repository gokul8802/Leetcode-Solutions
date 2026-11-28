class Solution:
    def lastNonEmptyString(self, s: str) -> str:
        freq = {}
        for c in s:
            freq[c] = freq.get(c, 0) + 1
        mx = max(freq.values())
        keep = {c for c in freq if freq[c] == mx}
        res = []
        for i in range(len(s)-1, -1, -1):
            if s[i] in keep:
                res.append(s[i])
                keep.remove(s[i])
        return ''.join(reversed(res))