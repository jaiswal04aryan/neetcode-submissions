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
