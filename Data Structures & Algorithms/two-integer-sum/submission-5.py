class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash = {}
        for i in range(len(nums)):
            other = target - nums[i]
            if other in hash:
                return [hash.get(other), i]
            hash[nums[i]] = i