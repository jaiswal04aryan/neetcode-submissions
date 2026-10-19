class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        output = [0] * len(temperatures)   
        stack = []
        for i, temp in enumerate(temperatures):
            if not stack:
                stack.append(i)
            else:
                while stack and temp > temperatures[stack[-1]]:
                    output[stack[-1]] = i - stack[-1]
                    stack.pop()
                stack.append(i)
        return output

            