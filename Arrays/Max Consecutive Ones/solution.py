class Solution:
    def maxConsecutiveOnes(self, nums: list[int]) -> int:
        maximum : int = 0
        counter : int = 0


        for i in range(len(nums)):
            if(nums[i] == 1):
                counter = counter + 1
                maximum = max(maximum,counter)

            if(nums[i] == 0):
                counter = 0

        return maximum

    def maxConsecutiveOnes2(self, nums: list[int]) -> int:
        consecutives : list[int] = []
        counter : int = 0
        highest : int = 0

        for i in range(len(nums)):
            if(nums[i] == 1):
                counter = counter + 1

            if(nums[i] == 0):
                consecutives.append(counter)
                counter = 0

        consecutives.append(counter)

        for consecutive in consecutives:
            highest = max(highest, consecutive)

        return highest
