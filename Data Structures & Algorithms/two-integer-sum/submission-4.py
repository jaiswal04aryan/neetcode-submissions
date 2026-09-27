class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        result = {}
        for i in range(len(nums)):
            diff = target - nums[i]
            if diff in result:
                return [result.get(diff), i]
            else:
                result[nums[i]] = i