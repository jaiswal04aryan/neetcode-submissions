class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        maxLen = 0
        freq = {}
        l = 0
        for r in range(len(s)):
            freq[s[r]] = freq.get(s[r], 0) + 1
            while (r - l + 1) - max(freq.values(), default = 0) > k:
                freq[s[l]] = freq.get(s[l]) - 1
                l += 1
            maxLen = max(maxLen, r - l + 1)
        return maxLen



