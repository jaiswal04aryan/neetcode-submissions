class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        maxLength = 0
        numsSet = set(nums)
        for i in numsSet:
            if i - 1 not in numsSet:
                length = 0
                while (i-1) not in numsSet and (i+length) in numsSet:
                    length += 1
                    maxLength = max(maxLength, length)
        return maxLength