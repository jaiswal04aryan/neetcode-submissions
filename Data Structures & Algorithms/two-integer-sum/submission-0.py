class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        res = []
        hash_map = {}
        for i in range(len(nums)):
            complimentary = target - nums[i]
            if complimentary in hash_map:
                res.append(hash_map[complimentary])
                res.append(i)
                return res
            else:
                hash_map[nums[i]] = i
        return res
