class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        maxLen = 0
        currSet = set()
        L = 0
        R = 0
        while R < len(s):
            while L < R and s[R] in currSet:
                currSet.remove(s[L])
                L += 1
            currSet.add(s[R])
            R += 1
            currLen = R - L 
            maxLen = max(currLen, maxLen)
        return maxLen



