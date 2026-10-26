class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1Value = [0] * 26
        s2Value = [0] * 26
        L = 0
        for c in s1:
            s1Value[ord(c) - ord('a')] += 1
        for R in range(len(s2)):
            s2Value[ord(s2[R]) - ord('a')] += 1
            if len(s1) == R - L + 1:
                if s1Value == s2Value:
                    return True
                else:
                    s2Value[ord(s2[L]) - ord('a')] -= 1
                    L += 1
            
        return False

            

                

