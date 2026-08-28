from calendar import c
from multiprocessing.pool import ApplyResult
from operator import le


class Solution:
    def NumbersSmallerThan(self, numbers: list[int]) -> list[int]:
        ordered: list[int] = []
        current: int = 0
        count: int = 0


        for i in range(len(numbers)):
            count = 0
            current = i
            for x in numbers:
                print(f"numero a comparar: {numbers[current]}, numero contra se compara:{x}")
                if(numbers[current] > x):
                    count += 1
            ordered.append(count)
        return ordered

    def NumbersSmallerThan2(self, numbers: list[int]) -> list[int]:

        appearances: list[int] = [0] * 101

        lessNumbers: int = 0
        toBeSummed: int = 0
        cycle: int = 0

        for x in numbers:
            appearances[x] +=1
        print(appearances)

        for i in range(len(appearances)):
            if(appearances[i] >= 1):
                print(f"lessNumbers: {lessNumbers}, i: {i}")
                print(f"entered loop with number:{appearances[i]}")
                toBeSummed += appearances[i]
                print(f"tobeSummed changed:{toBeSummed}")
                appearances[i] = lessNumbers
                print(f"current list: {lessNumbers}")
                lessNumbers = toBeSummed
                print(f"less numbers changed: {lessNumbers}, this was added: {toBeSummed}")
        for x in numbers:
            numbers[cycle] = appearances[x]
            cycle += 1

        return numbers

                                             #1,2,4,8
s = Solution()                               #[1,2,1,1]
print(s.NumbersSmallerThan2([8,1,2,2,4])) #-> [0,1,3,4]
