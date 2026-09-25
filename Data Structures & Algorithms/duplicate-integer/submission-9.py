class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # result = []
        # for i in range(len(nums)):
        #     if nums[i] not in result:
        #         result.append(nums[i])
        #     else:
        #         return True
        # return False
#         Tuple: Ordered, immutable collection that allows duplicate values.
# Set: Unordered, mutable collection that stores only unique values.
        return len(nums) != len(set(nums))
        