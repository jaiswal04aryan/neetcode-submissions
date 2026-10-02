class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # result = []
        # for i in range(len(nums)):
        #     number = 1
        #     for j in range(len(nums)):
        #         if i == j:
        #             pass
        #         else:
        #             number *= nums[j]
        #     result.append(number)
        # return result
        prefix = 1
        output = [1] * len(nums)
        for i in range(len(nums)):
            output[i] = prefix
            prefix *= nums[i]
        postfix = 1
        for i in range(len(nums) - 1, -1, -1):
            output[i] *= postfix
            postfix *= nums[i]
        return output
