class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = [[] for i in range(len(nums) + 1)]
        output = []
        nums_hash = {} 
        for n in range(len(nums)):
            nums_hash[nums[n]] = nums_hash.get(nums[n], 0) + 1
        for c in nums_hash:
            count[nums_hash.get(c)].append(c)
        for j in range(len(count) - 1, 0, -1):
            for a in count[j]:
                output.append(a)
                if len(output) == k:
                    return output
                