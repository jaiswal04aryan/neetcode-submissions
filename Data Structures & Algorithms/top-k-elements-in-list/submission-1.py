class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        final = []
        count = {}
        frequency = [[] for i in range(len(nums) + 1)]
        for j in nums:
            count[j] = count.get(j, 0) + 1
        for c in count:
            frequency[count.get(c)].append(c)
        for x in range(len(frequency) - 1, 0, -1):
            for a in frequency[x]:
                final.append(a)
                if len(final) == k:
                    return final
        