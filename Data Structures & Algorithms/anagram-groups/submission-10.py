class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = defaultdict(list)
        for s in strs:
            pos = [0]*26
            for c in s:
                pos[ord(c) - ord('a')] += 1
            result[tuple(pos)].append(s) # again remember, list cannot be keys in a hash. and this line 8 simply appends the value s to the valye of key pos
        return list(result.values())
            
