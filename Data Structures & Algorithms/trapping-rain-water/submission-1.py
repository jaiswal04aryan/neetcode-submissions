class Solution:
    def trap(self, height: List[int]) -> int:
        totalVolume = 0
        leftMax = 0
        rightMax = 0
        L = 0
        R = len(height) - 1
        while L < R:
            leftMax = max(leftMax, height[L])
            rightMax = max(rightMax, height[R])
            if leftMax > rightMax:
                totalVolume = totalVolume + rightMax - height[R]
                R -= 1
            elif leftMax < rightMax:
                totalVolume = totalVolume + leftMax - height[L]
                L += 1
            elif leftMax == rightMax:
                totalVolume = totalVolume + leftMax - height[L]
                L += 1
        return totalVolume