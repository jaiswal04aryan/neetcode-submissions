class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        count_s = {}
        count_t = {}
        for i in range(len(s)):
            count_s[s[i]] = count_s.get(s[i], 0) + 1
        for i in range(len(t)):
            count_t[t[i]] = count_t.get(t[i], 0) + 1
        for i in count_s:
            if count_s.get(i) != count_t.get(i, 0):
                return False
        return True

# ### Valid Anagram — Notes

# - Use dictionaries (hash maps) to store each character’s frequency.
# - Increment a character’s count with:

# ```python
# counts[ch] = counts.get(ch, 0) + 1
# ```

# - `.get(ch, 0)` returns the current count, or `0` if the character does not exist yet.
# - If the strings have different lengths, they cannot be anagrams.
# - Compare the two frequency dictionaries at the end.

# ### Complexity

# - **Time:** `O(n)`
#   - Multiple sequential loops add together: `O(n + n) = O(n)`.
#   - Dictionary operations are `O(1)` on average.
# - **Space:** `O(1)` under the given constraints
#   - Only lowercase English letters are allowed, so each dictionary has at most 26 keys.
#   - The input itself is not counted as extra space.
#   - With arbitrary characters, the space would be `O(n)`.