class Solution:
    def FindDissapeared2(self, numbers: list[int]) -> list[int] :
        output : list[int] = []


        for x in numbers:
            if(x < 0):
                x *= -1
            print(f"Evaluating {x}")
            print(numbers)
            if(numbers[x-1] > 0):
                numbers[x-1] *= -1

            print(numbers)

        for i in range(len(numbers)):
            if(numbers[i] > 0):
                output.append(i+1)


        return output






    def FindDissapeared(self, numbers: list[int]) -> list[int] :
        n = len(numbers)
        appearances : list[int] = [0] * (n + 1)
        output: list[int] = []

        for x in numbers:
            appearances[x] += 1

        for i in range(1,len(appearances)):
            if(appearances[i] == 0):
                output.append(i)



        return output





s = Solution()
print(s.FindDissapeared2([4,3,2,7,8,2,3,1]))
