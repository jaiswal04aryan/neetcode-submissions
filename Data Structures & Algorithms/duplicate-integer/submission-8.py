class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # result = []
        # for i in range(len(nums)):
        #     if nums[i] not in result:
        #         result.append(nums[i])
        #     else:
        #         return True
        # return False
        return len(nums) != len(set(nums))
        