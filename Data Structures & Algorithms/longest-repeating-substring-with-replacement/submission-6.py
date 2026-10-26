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


# maxF = highest frequency we've seen for any character while expanding.
# We don't decrease maxF when L moves.
#
# Window is valid when:
# window_size - maxF <= k
#
# If window grows AND maxF grows too, replacement cost may stay the same.
# Example: 5 - 3 = 2, then 6 - 4 = 2 -> still valid.
#
# If window grows but maxF does NOT grow, replacement cost increases.
# Example: 6 - 3 = 3 -> if k = 2, shrink from the left.
#
# maxF can be slightly stale after shrinking, and that's okay:
# it represents the best dominant frequency we've seen so far,
# which is enough for finding the maximum valid window length.