class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        maxFreq = 0
        freq = {}
        maxLen = 0
        l = 0
        for r in range(len(s)):
            freq[s[r]] = freq.get(s[r], 0) + 1
            maxFreq = max(freq.get(s[r]), maxFreq)
            while (r - l + 1) - maxFreq > k:
                freq[s[l]] -= 1
                l += 1
            maxLen = max(maxLen, r - l + 1)
        return maxLen
        