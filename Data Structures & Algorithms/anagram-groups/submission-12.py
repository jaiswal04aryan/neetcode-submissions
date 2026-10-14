class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        output = defaultdict(list)
        for s in strs:
            num_array = [0] * 26
            for c in s:
                num_array[ord('a') - ord(c)] += 1
            output[tuple(num_array)].append(s)
        return list(output.values())