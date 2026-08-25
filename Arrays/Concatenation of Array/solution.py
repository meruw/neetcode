class Solution:
    def getConcatenation(self, nums: list[int]) -> list[int]:
        ans: list[int] = [0] * (2 * len(nums))

        for i in range(len(nums)):
            ans[i] = nums[i]
            ans[i + len(nums)] = nums[i]

        return ans


solution = Solution()
print(solution.getConcatenation([1, 2, 1]))
