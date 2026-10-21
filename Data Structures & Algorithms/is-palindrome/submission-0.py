class Solution:
    def isPalindrome(self, s: str) -> bool:
        finalString = ''
        for c in s:
            if c.isalnum():
                finalString += c.lower()
        l = 0
        r = len(finalString) - 1
        while l < r:
            if finalString[r] == finalString[l]:
                r -= 1
                l += 1
            else:
                return False
        return True


        