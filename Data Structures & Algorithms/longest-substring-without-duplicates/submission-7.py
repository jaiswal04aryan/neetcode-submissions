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


#
# 1. Sequential loops usually ADD:
#    O(n) + O(n) = O(n)
#
# 2. Nested loops only MULTIPLY when the inner loop can do
#    a full O(n) amount of work for EACH outer-loop iteration:
#    O(n) * O(n) = O(n^2)
#
# 3. In sliding window / two-pointer problems, even if there is
#    a while-loop inside another while-loop, L and R usually only
#    move forward and never reset.
#
#    R moves at most n times total
#    L moves at most n times total
#
#    So total work is:
#    O(n) + O(n) = O(n)
#
# Key idea:
# Nested syntax does NOT automatically mean O(n^2).
# Ask: "How many total times can this inner operation happen
# across the entire algorithm?"
