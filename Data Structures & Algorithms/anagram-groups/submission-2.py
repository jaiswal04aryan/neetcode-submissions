class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = defaultdict(list)
        for i in strs:
            count = [0] * 26
            for n in i:
                count[ord(n) - ord("a")] += 1
            result[tuple(count)].append(i)
        return list(result.values())