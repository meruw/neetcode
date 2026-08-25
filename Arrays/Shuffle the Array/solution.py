class Solution:
    def shuffleArray(self, nums: list[int]) -> list[int]:
        ans: list[int] = [0] * len(nums)
        n = len(nums) // 2


        for i in range(n):
            ans[i * 2] = nums[i]
            ans[i * 2 + 1] = nums[i + n]
        return ans

solution = Solution()
print(solution.shuffleArray([2,5,1,3,4,7]))
