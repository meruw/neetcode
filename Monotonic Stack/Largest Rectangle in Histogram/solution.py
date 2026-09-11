class Solution:
    def largestRectangleArea(self, heights: list[int]) -> int:
        stack = []
        highest = 0
        current = 0

        for i in range(len(heights)):

            while stack and heights[stack[-1]] > heights[i]: #cannot extend more to the right
                print(f"Current stack: {stack}")
                print(f"evaluating: {heights[stack[-1]]} > {heights[i]}")
                index = stack.pop()
                if stack:
                    width = i - stack[-1] - 1
                else:
                    width = i
                print(f"new index: {index}")
                current = heights[index] * width
                print(f"new current: {current} obtained from {heights[index]} * {width}")
                if current > highest:
                    highest = current
                    print(f"New highest: {highest}")

            stack.append(i)


            print(f"New entry in the stack: {stack}, {heights}")
        while stack:
            index = stack.pop()

            if stack:
                width = len(heights) - stack[-1] - 1
            else:
                 width = len(heights)

            current = heights[index] * width
            if current > highest:
                highest = current


        return highest




s = Solution()
print(s.largestRectangleArea([3,2,1,2,3]))
