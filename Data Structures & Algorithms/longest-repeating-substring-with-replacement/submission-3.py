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

# Sliding Window - Original Solution
#
# 1. Add s[r] to the frequency map.
# 2. Replacements needed = window_size - max(freq.values()).
# 3. If replacements > k, shrink from the left and decrement freq[s[l]].
# 4. Once valid, update maxLen with r - l + 1.
#
# Time: O(n) here because there are only 26 uppercase letters.
# Space: O(1) -> at most 26 keys.

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