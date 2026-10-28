class Solution:
    def minWindow(self, s: str, t: str) -> str:
        tHash = {}
        sHash = {}
        counter = len(t)
        l = 0
        minLength = float("inf")
        found = False
        for i in t:
            tHash[i] = tHash.get(i, 0) + 1
        for r in range(len(s)):
            sHash[s[r]] = sHash.get(s[r], 0) + 1
            if s[r] in tHash and sHash.get(s[r]) <= tHash.get(s[r]):
                counter -= 1
            while counter == 0:
                if r - l + 1 < minLength:
                    minLength = r - l + 1
                    start = l
                    end = r + 1
                    found = True
                sHash[s[l]] = sHash.get(s[l], 0) - 1
                if s[l] in tHash and sHash.get(s[l]) < tHash.get(s[l], 0):
                    counter += 1
                l += 1
            
        if not found:
            return ""
        else:
            return s[start:end]


        
        
 