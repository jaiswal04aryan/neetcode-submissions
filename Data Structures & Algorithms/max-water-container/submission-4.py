class Solution:
    def maxArea(self, heights: List[int]) -> int:
        maxVolume = 0
        L = 0
        R = len(heights) - 1
        while L < R:
            volume = (R - L) * min(heights[R], heights[L])
            maxVolume = max(maxVolume, volume)
            if heights[L] > heights[R]:
                R -= 1
            else:
                L += 1
        return maxVolume
        