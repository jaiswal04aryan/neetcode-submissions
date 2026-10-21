class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result = set()
        nums = sorted(nums)
        for i in range(len(nums) - 2):
            numsI = nums[i]
            L = i + 1 
            R = len(nums) -1
            while L < R:
                if numsI + nums[L] + nums[R] > 0:
                    R -= 1
                elif numsI + nums[L] + nums[R] < 0:
                    L += 1
                elif numsI + nums[L] + nums[R] == 0:
                    triplet = tuple(sorted((numsI, nums[L], nums[R])))
                    result.add(triplet)
                    L += 1
        return list(result)