class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = defaultdict(list) #so that when we call hash that does not have a key:value, it returns an empty list instead of an error
        for s in strs:
            count = [0] * 26
            for c in s:
                count[ord(c) - ord('a')] += 1
            result[tuple(count) ].append(s)
        return(list(result.values()))