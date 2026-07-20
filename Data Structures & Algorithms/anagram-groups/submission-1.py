class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)
        for s in strs:
            count = [0] * 26 #since we have 26 characters
            for i in s:
                count[ord(i) - ord("a")] += 1
            res[tuple(count)].append(s)
        return list(res.values())