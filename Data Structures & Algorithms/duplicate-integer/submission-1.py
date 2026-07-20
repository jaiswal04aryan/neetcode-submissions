class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        count_map = Counter(nums)
        for num in nums:
            if count_map[num] > 1:
                return True
        return False