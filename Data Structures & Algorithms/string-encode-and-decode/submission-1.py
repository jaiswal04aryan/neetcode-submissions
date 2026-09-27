class Solution:

    def encode(self, strs: List[str]) -> str:
        s = ""
        for x in strs:
            s += str(len(x)) + '#' + x
        return s

    def decode(self, s: str) -> List[str]:
        i = 0
        decode = []
        while i < len(s):
            j = i
            while s[j] != '#':
                j += 1
            length = int(s[i:j])
            start = j + 1
            end = start + length
            decode.append(s[start:end])
            i = end 
        return decode


