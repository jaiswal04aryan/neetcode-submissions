class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        maxLen = 0
        currSet = set()
        L = 0
        R = 0
        while R < len(s):
            # while L < R and s[R] in currSet: changing this to next line because pay attention, we dont need l<r, because we are literally removnig the element that is duplicate, if it doesnt exist if R doesnt add it, so that means L can never be ahead of R
            while s[R] in currSet:
                currSet.remove(s[L])
                L += 1
            currSet.add(s[R])
            R += 1
            currLen = R - L 
            maxLen = max(currLen, maxLen)
        return maxLen



